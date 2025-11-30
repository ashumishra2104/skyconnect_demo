import streamlit as st
from datetime import datetime

def render_details():
    st.subheader("Passenger Details")
    
    # Container for form
    st.markdown('<div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.12);">', unsafe_allow_html=True)
    
    num_passengers = st.session_state.search_params['passengers']['Adults'] # Kept original logic for num_passengers
    
    # Initialize passenger details if not present or size mismatch
    if 'passenger_details' not in st.session_state or len(st.session_state.passenger_details) != num_passengers:
        st.session_state.passenger_details = [{'title': 'Mr', 'first_name': '', 'last_name': '', 'email': '', 'phone': '', 'dob': datetime(1990, 1, 1)} for _ in range(num_passengers)]

    with st.form("passenger_form"):
        for i in range(num_passengers):
            st.markdown(f"#### Passenger {i+1}")
            col1, col2, col3 = st.columns([1, 2, 2])
            
            with col1:
                st.session_state.passenger_details[i]['title'] = st.selectbox(f"Title", ["Mr", "Ms", "Mrs", "Dr"], key=f"title_{i}", index=["Mr", "Ms", "Mrs", "Dr"].index(st.session_state.passenger_details[i]['title']) if st.session_state.passenger_details[i]['title'] in ["Mr", "Ms", "Mrs", "Dr"] else 0)
            with col2:
                st.session_state.passenger_details[i]['first_name'] = st.text_input(f"First Name", value=st.session_state.passenger_details[i]['first_name'], key=f"fname_{i}")
            with col3:
                st.session_state.passenger_details[i]['last_name'] = st.text_input(f"Last Name", value=st.session_state.passenger_details[i]['last_name'], key=f"lname_{i}")
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.session_state.passenger_details[i]['dob'] = st.date_input(f"Date of Birth", value=st.session_state.passenger_details[i]['dob'], min_value=datetime(1900, 1, 1), max_value=datetime.now(), key=f"dob_{i}")
            with col5:
                st.session_state.passenger_details[i]['email'] = st.text_input(f"Email", value=st.session_state.passenger_details[i]['email'], key=f"email_{i}")
            with col6:
                st.session_state.passenger_details[i]['phone'] = st.text_input(f"Phone", value=st.session_state.passenger_details[i]['phone'], key=f"phone_{i}")
            
            if i < num_passengers - 1:
                st.divider()

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Continue to Seat Selection", type="primary", use_container_width=True)
        
        if submitted:
            # Basic validation
            valid = True
            for p in st.session_state.passenger_details:
                if not p['first_name'] or not p['last_name']:
                    valid = False
                    st.error("Please fill in all names.")
                    break
            
            if valid:
                st.session_state.step = 3.5 # Intermediate step for seats
                st.rerun()
