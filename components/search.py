import streamlit as st
from datetime import datetime, timedelta

def render_search():
    # Hero Section
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Where to next?</h1>
            <p class="hero-subtitle">Discover amazing places at exclusive deals</p>
        </div>
    """, unsafe_allow_html=True)

    # Search Container
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    
    st.subheader("Find your flight")
    
    col1, col2 = st.columns(2)
    
    with col1:
        origin = st.selectbox("From", ["New York (JFK)", "London (LHR)", "Dubai (DXB)", "Mumbai (BOM)", "Delhi (DEL)", "Hyderabad (HYD)", "Goa (GOI)"], index=5)
        departure_date = st.date_input("Departure", min_value=datetime.today())
        
    with col2:
        destination = st.selectbox("To", ["New York (JFK)", "London (LHR)", "Dubai (DXB)", "Mumbai (BOM)", "Delhi (DEL)", "Hyderabad (HYD)", "Goa (GOI)"], index=6)
        return_date = st.date_input("Return", min_value=departure_date)

    col3, col4 = st.columns(2)
    with col3:
        passengers = st.number_input("Passengers", min_value=1, max_value=9, value=1)
    with col4:
        travel_class = st.selectbox("Class", ["Economy", "Premium Economy", "Business", "First"])

    if st.button("Search Flights", type="primary", use_container_width=True):
        if origin == destination:
            st.error("Origin and Destination cannot be the same.")
        else:
            st.session_state.search_params = {
                'origin': origin.split('(')[1].strip(')'),
                'destination': destination.split('(')[1].strip(')'),
                'dept_date': departure_date, # Fixed key name to match usage in other files
                'return_date': return_date,
                'passengers': {'Adults': passengers}, # Fixed structure
                'class': travel_class
            }
            st.session_state.step = 2
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)
