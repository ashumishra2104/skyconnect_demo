import streamlit as st
from datetime import datetime, timedelta

def render_search():
    st.markdown("### 🔍 Search Flights")
    
    with st.container():
        st.markdown('<div class="flight-card">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_input("From", value="Hyderabad (HYD)", disabled=True)
        with col2:
            st.text_input("To", value="Goa (GOI)", disabled=True)
            
        col3, col4 = st.columns(2)
        
        with col3:
            dept_date = st.date_input(
                "Departure Date",
                value=st.session_state.search_params['dept_date'],
                min_value=datetime.now().date()
            )
            
        with col4:
            return_date = st.date_input(
                "Return Date",
                value=st.session_state.search_params['return_date'],
                min_value=dept_date
            )
            
        col5, col6 = st.columns(2)
        
        with col5:
            passengers = st.number_input(
                "Passengers",
                min_value=1,
                max_value=9,
                value=st.session_state.search_params['passengers']['Adults']
            )
            
        with col6:
            flight_class = st.selectbox(
                "Class",
                ["Economy", "Premium Economy", "Business"],
                index=["Economy", "Premium Economy", "Business"].index(st.session_state.search_params['class'])
            )
            
        if st.button("Search Flights", use_container_width=True):
            # Update session state
            st.session_state.search_params['dept_date'] = dept_date
            st.session_state.search_params['return_date'] = return_date
            st.session_state.search_params['passengers']['Adults'] = passengers
            st.session_state.search_params['class'] = flight_class
            
            st.session_state.step = 2
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)
