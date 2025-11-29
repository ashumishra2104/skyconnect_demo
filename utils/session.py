import streamlit as st
from datetime import datetime, timedelta

def init_session_state():
    """Initializes all session state variables."""
    defaults = {
        'step': 1,
        'search_params': {
            'origin': 'Hyderabad (HYD)',
            'destination': 'Goa (GOI)',
            'dept_date': datetime.now().date() + timedelta(days=1),
            'return_date': datetime.now().date() + timedelta(days=3),
            'passengers': {'Adults': 1, 'Children': 0, 'Infants': 0},
            'class': 'Economy'
        },
        'selected_outbound': None,
        'selected_return': None,
        'passenger_details': [],
        'seat_selection': {}, # {flight_id: {passenger_index: seat_id}}
        'addons': {
            'baggage': {},
            'meals': {},
            'insurance': False,
            'priority_checkin': False,
            'lounge': False
        },
        'booking_id': None
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def reset_booking():
    """Resets the booking flow."""
    keys_to_reset = ['step', 'selected_outbound', 'selected_return', 'passenger_details', 'seat_selection', 'addons', 'booking_id']
    for key in keys_to_reset:
        if key in st.session_state:
            del st.session_state[key]
    init_session_state()
