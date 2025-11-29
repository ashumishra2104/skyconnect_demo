import streamlit as st
from utils.flight_data import generate_flights
from utils.pricing import calculate_price

def render_flight_card(flight, is_selected, on_select, context):
    """Renders a single flight card."""
    
    card_style = """
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    margin-bottom: 0.5rem;
    background-color: {bg_color};
    cursor: pointer;
    """
    bg_color = "#e3f2fd" if is_selected else "white"
    
    with st.container():
        st.markdown(f'<div style="{card_style.format(bg_color=bg_color)}">', unsafe_allow_html=True)
        
        c1, c2, c3, c4, c5 = st.columns([2, 2, 2, 2, 2])
        
        with c1:
            st.markdown(f"**{flight['airline']}**")
            st.caption(flight['flight_number'])
            
        with c2:
            st.markdown(f"**{flight['departure_time'].strftime('%H:%M')}**")
            st.caption(flight['origin'])
            
        with c3:
            st.markdown(f"**{flight['duration']}**")
            st.caption(flight['stops'])
            
        with c4:
            st.markdown(f"**{flight['arrival_time'].strftime('%H:%M')}**")
            st.caption(flight['destination'])
            
        with c5:
            # Calculate dynamic price
            days_in_advance = (flight['departure_time'].date() - datetime.now().date()).days
            price = calculate_price(
                flight['base_price'],
                flight,
                st.session_state.search_params['class'],
                days_in_advance
            )
            st.markdown(f"**₹{price:,}**")
            if st.button("Select", key=f"btn_{flight['id']}_{context}", type="primary" if is_selected else "secondary"):
                on_select(flight)
                
        st.markdown('</div>', unsafe_allow_html=True)

from datetime import datetime

def render_results():
    st.markdown("### ✈️ Select Flights")
    
    # Generate flights if not already generated or if params changed (simplified for now)
    # In a real app, we'd cache this better.
    outbound_flights = generate_flights(
        st.session_state.search_params['dept_date'],
        "HYD", "GOI"
    )
    
    return_flights = generate_flights(
        st.session_state.search_params['return_date'],
        "GOI", "HYD"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Outbound: HYD → GOI")
        st.caption(f"{st.session_state.search_params['dept_date'].strftime('%d %b %Y')}")
        
        for _, flight in outbound_flights.iterrows():
            is_selected = st.session_state.selected_outbound and st.session_state.selected_outbound['id'] == flight['id']
            def select_outbound(f):
                st.session_state.selected_outbound = f.to_dict()
                st.rerun()
            render_flight_card(flight, is_selected, select_outbound, "outbound")
            
    with col2:
        st.subheader("Return: GOI → HYD")
        st.caption(f"{st.session_state.search_params['return_date'].strftime('%d %b %Y')}")
        
        for _, flight in return_flights.iterrows():
            is_selected = st.session_state.selected_return and st.session_state.selected_return['id'] == flight['id']
            def select_return(f):
                st.session_state.selected_return = f.to_dict()
                st.rerun()
            render_flight_card(flight, is_selected, select_return, "return")

    # Footer Action
    st.markdown("---")
    c1, c2 = st.columns([6, 1])
    with c2:
        disabled = not (st.session_state.selected_outbound and st.session_state.selected_return)
        if st.button("Continue", disabled=disabled, type="primary"):
            st.session_state.step = 3
            st.rerun()
    with c1:
        if st.button("Back"):
            st.session_state.step = 1
            st.rerun()
