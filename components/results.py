import streamlit as st
from datetime import datetime

def render_results():
    st.subheader("Select your flights")
    
    # Mock data
    outbound_flights = [
        {'id': 1, 'airline': 'IndiGo', 'flight_number': '6E-532', 'origin': 'HYD', 'destination': 'GOI', 'departure_time': datetime.now().replace(hour=10, minute=0), 'arrival_time': datetime.now().replace(hour=12, minute=15), 'duration': '2h 15m', 'stops': 'Non-stop', 'price': 4500, 'base_price': 4000},
        {'id': 2, 'airline': 'Air India', 'flight_number': 'AI-840', 'origin': 'HYD', 'destination': 'GOI', 'departure_time': datetime.now().replace(hour=14, minute=30), 'arrival_time': datetime.now().replace(hour=16, minute=45), 'duration': '2h 15m', 'stops': 'Non-stop', 'price': 5200, 'base_price': 4800},
        {'id': 3, 'airline': 'Vistara', 'flight_number': 'UK-890', 'origin': 'HYD', 'destination': 'GOI', 'departure_time': datetime.now().replace(hour=18, minute=0), 'arrival_time': datetime.now().replace(hour=20, minute=15), 'duration': '2h 15m', 'stops': 'Non-stop', 'price': 6000, 'base_price': 5500},
    ]
    
    return_flights = [
        {'id': 4, 'airline': 'IndiGo', 'flight_number': '6E-533', 'origin': 'GOI', 'destination': 'HYD', 'departure_time': datetime.now().replace(hour=11, minute=0), 'arrival_time': datetime.now().replace(hour=13, minute=15), 'duration': '2h 15m', 'stops': 'Non-stop', 'price': 4600, 'base_price': 4100},
        {'id': 5, 'airline': 'Air India', 'flight_number': 'AI-841', 'origin': 'GOI', 'destination': 'HYD', 'departure_time': datetime.now().replace(hour=15, minute=30), 'arrival_time': datetime.now().replace(hour=17, minute=45), 'duration': '2h 15m', 'stops': 'Non-stop', 'price': 5300, 'base_price': 4900},
    ]

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Outbound")
        st.caption(f"{st.session_state.search_params['origin']} to {st.session_state.search_params['destination']}")
        
        selected_outbound_id = st.session_state.selected_outbound['id'] if st.session_state.selected_outbound else None
        
        for flight in outbound_flights:
            is_selected = selected_outbound_id == flight['id']
            render_flight_card(flight, is_selected, select_outbound, "outbound")
            
    with col2:
        st.markdown("### Return")
        st.caption(f"{st.session_state.search_params['destination']} to {st.session_state.search_params['origin']}")
        
        selected_return_id = st.session_state.selected_return['id'] if st.session_state.selected_return else None
        
        for flight in return_flights:
            is_selected = selected_return_id == flight['id']
            render_flight_card(flight, is_selected, select_return, "return")
            
    # Continue Button
    st.markdown("---")
    if st.session_state.selected_outbound and st.session_state.selected_return:
        if st.button("Continue to Passenger Details", type="primary", use_container_width=True):
            st.session_state.step = 3
            st.rerun()
    else:
        st.warning("Please select both outbound and return flights to continue.")

def render_flight_card(flight, is_selected, on_select, context):
    """
    Renders a single flight card with premium styling.
    """
    # Format times
    dep_time = flight['departure_time'].strftime("%H:%M")
    arr_time = flight['arrival_time'].strftime("%H:%M")
    duration = "2h 15m" # Placeholder
    
    card_class = "flight-card"
    if is_selected:
        card_class += " selected"
        
    # Using HTML for finer control over layout and styling
    st.markdown(f"""
    <div class="{card_class}">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="background: #e3f2fd; padding: 10px; border-radius: 50%;">
                    <span style="font-size: 1.5rem;">✈️</span>
                </div>
                <div>
                    <h4 style="margin: 0; color: #172b4d;">{flight['airline']}</h4>
                    <p style="margin: 0; color: #5e6c84; font-size: 0.9rem;">{flight['flight_number']}</p>
                </div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.2rem; font-weight: 700; color: #172b4d;">{dep_time}</div>
                <div style="font-size: 0.8rem; color: #5e6c84;">{flight['origin']}</div>
            </div>
            <div style="text-align: center; color: #5e6c84;">
                <div style="font-size: 0.8rem;">{duration}</div>
                <div style="border-top: 1px solid #dfe1e6; width: 60px; margin: 5px auto;"></div>
                <div style="font-size: 0.8rem;">Non-stop</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.2rem; font-weight: 700; color: #172b4d;">{arr_time}</div>
                <div style="font-size: 0.8rem; color: #5e6c84;">{flight['destination']}</div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 1.5rem; font-weight: 700; color: #0052cc;">${flight['price']}</div>
                <div style="font-size: 0.8rem; color: #5e6c84;">per person</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Selection button (Streamlit widget for interaction)
    btn_label = "Selected" if is_selected else "Select Flight"
    btn_type = "primary" if is_selected else "secondary"
    
    # Unique key for the button
    if st.button(btn_label, key=f"btn_{context}_{flight['id']}", type=btn_type, use_container_width=True):
        on_select(flight)

def select_outbound(flight):
    st.session_state.selected_outbound = flight
    st.rerun()

def select_return(flight):
    st.session_state.selected_return = flight
    st.rerun()

def calculate_price(base_price, flight, travel_class, days_in_advance):
    # Simplified price calculation
    multiplier = 1.0
    if travel_class == "Premium Economy": multiplier = 1.5
    elif travel_class == "Business": multiplier = 2.5
    elif travel_class == "First": multiplier = 4.0
    
    # Advance booking discount
    if days_in_advance > 30: multiplier *= 0.8
    elif days_in_advance < 7: multiplier *= 1.2
    
    return int(base_price * multiplier)
