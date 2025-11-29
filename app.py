import streamlit as st
import os

# Set page config
st.set_page_config(
    page_title="SkyConnect - Flight Booking",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
def load_css():
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

from utils.session import init_session_state
from components.search import render_search
from components.results import render_results

from components.details import render_details
from components.seats import render_seats
from components.addons import render_addons
from components.payment import render_payment, render_confirmation

# Initialize session state
init_session_state()

# Header
st.title("✈️ SkyConnect")
st.markdown("---")

# Progress Indicator
steps = ["Search", "Select Flights", "Passenger Details", "Review & Pay"]
current_step = st.session_state.step
# Calculate progress, capping at 1.0 for completion (step 5)
progress_value = min((current_step - 1) / (len(steps) - 1), 1.0)
st.progress(progress_value)

# Navigation logic
if st.session_state.step == 1:
    render_search()

elif st.session_state.step == 2:
    render_results()

elif st.session_state.step == 3:
    render_details()

elif st.session_state.step == 3.5:
    render_seats()

elif st.session_state.step == 3.8:
    render_addons()

elif st.session_state.step == 4:
    render_payment()

elif st.session_state.step == 5:
    render_confirmation()
