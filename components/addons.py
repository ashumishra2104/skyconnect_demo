import streamlit as st

def render_addons():
    st.markdown("### ➕ Add-ons & Services")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Baggage")
        baggage_opt = st.radio(
            "Select Check-in Baggage",
            ["15kg (₹1200)", "20kg (₹1500)", "30kg (₹2000)"],
            index=0,
            help="Choose additional baggage allowance. Standard allowance is 15kg."
        )
        st.session_state.addons['baggage'] = baggage_opt
        
        st.subheader("Meals")
        meal = st.checkbox(
            "Add Meal (+₹350)",
            help="Includes a choice of Veg/Non-Veg gourmet meal, beverage, and dessert served onboard."
        )
        st.session_state.addons['meals'] = meal
        
    with col2:
        st.subheader("Other Services")
        ins = st.checkbox(
            "Travel Insurance (+₹299)",
            help="Comprehensive coverage for trip cancellation, medical emergencies, and baggage loss/delay."
        )
        st.session_state.addons['insurance'] = ins
        
        prio = st.checkbox(
            "Priority Check-in (+₹400)",
            help="Skip the long queues! Get dedicated counters for check-in and priority boarding."
        )
        st.session_state.addons['priority_checkin'] = prio
        
        lounge = st.checkbox(
            "Lounge Access (+₹1500)",
            help="Relax before your flight with complimentary food, drinks, WiFi, and comfortable seating in our partner lounges."
        )
        st.session_state.addons['lounge'] = lounge
        
    st.markdown("---")
    
    c1, c2 = st.columns([6, 1])
    with c2:
        if st.button("Review & Pay", type="primary"):
            st.session_state.step = 4
            st.rerun()
    with c1:
        if st.button("Back"):
            st.session_state.step = 3.5
            st.rerun()
