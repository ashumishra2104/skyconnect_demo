import streamlit as st
from datetime import datetime

def render_details():
    st.markdown("### 👤 Passenger Details")
    
    num_passengers = st.session_state.search_params['passengers']['Adults']
    
    # Initialize passenger details if not present or count changed
    if len(st.session_state.passenger_details) != num_passengers:
        st.session_state.passenger_details = [{'title': 'Mr', 'first_name': '', 'last_name': '', 'dob': None, 'email': '', 'phone': ''} for _ in range(num_passengers)]
        
    with st.form("passenger_form"):
        for i in range(num_passengers):
            st.markdown(f"#### Passenger {i+1}")
            c1, c2, c3 = st.columns([1, 2, 2])
            with c1:
                st.session_state.passenger_details[i]['title'] = st.selectbox(f"Title {i}", ["Mr", "Ms", "Mrs"], key=f"title_{i}")
            with c2:
                st.session_state.passenger_details[i]['first_name'] = st.text_input(f"First Name {i}", key=f"fname_{i}")
            with c3:
                st.session_state.passenger_details[i]['last_name'] = st.text_input(f"Last Name {i}", key=f"lname_{i}")
                
            c4, c5 = st.columns(2)
            with c4:
                 st.session_state.passenger_details[i]['dob'] = st.date_input(f"Date of Birth {i}", key=f"dob_{i}", max_value=datetime.now().date(), min_value=datetime(1900, 1, 1).date())
            with c5:
                if i == 0: # Contact info only for primary passenger
                    st.session_state.passenger_details[i]['email'] = st.text_input("Email", key=f"email_{i}")
                    st.session_state.passenger_details[i]['phone'] = st.text_input("Phone", key=f"phone_{i}")
            
            st.markdown("---")
            
        if st.form_submit_button("Continue to Seats"):
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
