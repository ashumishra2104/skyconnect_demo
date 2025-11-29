import streamlit as st
import random
import string
from utils.pricing import calculate_price, calculate_taxes_and_fees

def generate_pnr():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def render_payment():
    st.markdown("### 💳 Review & Pay")
    
    # Calculate totals
    outbound_price = calculate_price(
        st.session_state.selected_outbound['base_price'],
        st.session_state.selected_outbound,
        st.session_state.search_params['class'],
        (st.session_state.selected_outbound['departure_time'].date() - datetime.now().date()).days
    )
    
    return_price = calculate_price(
        st.session_state.selected_return['base_price'],
        st.session_state.selected_return,
        st.session_state.search_params['class'],
        (st.session_state.selected_return['departure_time'].date() - datetime.now().date()).days
    )
    
    num_passengers = st.session_state.search_params['passengers']['Adults']
    base_fare = (outbound_price + return_price) * num_passengers
    
    taxes = calculate_taxes_and_fees(base_fare, num_passengers)
    
    # Add-ons cost
    addons_cost = 0
    if st.session_state.addons['meals']: addons_cost += 350 * num_passengers
    if st.session_state.addons['insurance']: addons_cost += 299 * num_passengers
    if st.session_state.addons['priority_checkin']: addons_cost += 400 * num_passengers
    if st.session_state.addons['lounge']: addons_cost += 1500 * num_passengers
    
    # Baggage
    bag_price = 0
    if "15kg" in st.session_state.addons['baggage']: bag_price = 1200
    elif "20kg" in st.session_state.addons['baggage']: bag_price = 1500
    elif "30kg" in st.session_state.addons['baggage']: bag_price = 2000
    addons_cost += bag_price * num_passengers
    
    # Seats
    seat_cost = 0
    # Simplified seat cost calculation
    for flight_type in ['outbound']: # Add return logic if needed
        for seat in st.session_state.seat_selection.get(flight_type, []):
            if seat.startswith('1'): seat_cost += 500
            elif 'A' in seat or 'F' in seat: seat_cost += 200
            elif 'C' in seat or 'D' in seat: seat_cost += 200
            
    total_amount = base_fare + taxes['total_fees'] + addons_cost + seat_cost
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Flight Summary")
        st.info(f"Outbound: {st.session_state.selected_outbound['airline']} {st.session_state.selected_outbound['flight_number']}")
        st.info(f"Return: {st.session_state.selected_return['airline']} {st.session_state.selected_return['flight_number']}")
        
        st.subheader("Passenger Details")
        for p in st.session_state.passenger_details:
            st.write(f"{p['title']} {p['first_name']} {p['last_name']}")
            
        st.subheader("Payment Method")
        payment_method = st.radio("Select Payment Method", ["Credit/Debit Card", "UPI", "Net Banking"])
        
        if payment_method == "Credit/Debit Card":
            c1, c2 = st.columns(2)
            c1.text_input("Card Number")
            c2.text_input("CVV", type="password")
        elif payment_method == "UPI":
            st.text_input("UPI ID")
            
    with col2:
        st.markdown("### Fare Breakdown")
        st.write(f"Base Fare ({num_passengers} pax): ₹{base_fare:,}")
        st.write(f"Taxes & Fees: ₹{taxes['total_fees']:,}")
        st.write(f"Add-ons: ₹{addons_cost:,}")
        st.write(f"Seat Selection: ₹{seat_cost:,}")
        st.markdown("---")
        st.markdown(f"### Total: ₹{total_amount:,}")
        
        if st.button("PAY NOW", type="primary", use_container_width=True):
            # Prepare data for DB
            booking_data = {
                'pnr': generate_pnr(),
                'total_amount': total_amount,
                'contact_email': st.session_state.passenger_details[0]['email'],
                'contact_phone': st.session_state.passenger_details[0]['phone'],
                'passengers': st.session_state.passenger_details,
                'flights': {
                    'outbound': st.session_state.selected_outbound,
                    'return': st.session_state.selected_return
                }
            }
            
            # Add seat info to passengers (simplified mapping)
            # In a real app, we'd map seats to specific passengers more robustly
            outbound_seats = st.session_state.seat_selection.get('outbound', [])
            for i, p in enumerate(booking_data['passengers']):
                if i < len(outbound_seats):
                    p['seat'] = outbound_seats[i]
            
            # Save to DB
            from utils.db import init_db, save_booking_to_db
            try:
                init_db() # Ensure tables exist
                if save_booking_to_db(booking_data):
                    st.session_state.booking_id = booking_data['pnr']
                    st.session_state.step = 5
                    st.rerun()
                else:
                    st.error("Failed to save booking. Please try again.")
            except Exception as e:
                st.error(f"Database Error: {e}")

from datetime import datetime

def render_confirmation():
    st.balloons()
    st.success(f"Booking Confirmed! PNR: {st.session_state.booking_id}")
    
    st.markdown("### 🎫 Your Ticket")
    st.info("Ticket details have been sent to your email.")
    
    if st.button("Book Another Flight"):
        from utils.session import reset_booking
        reset_booking()
        st.rerun()
