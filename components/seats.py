import streamlit as st

def render_seats():
    st.markdown("### 💺 Select Seats")
    
    # Mock seat map layout (6 columns: ABC - DEF)
    rows = 10
    cols = ["A", "B", "C", "D", "E", "F"]
    
    st.info("Select seats for Outbound Flight")
    
    # Simple grid for seats
    # In a real app, this would be more visual
    
    selected_seats = st.session_state.seat_selection.get('outbound', [])
    
    # Create a visual representation using columns
    for r in range(1, rows + 1):
        c_cols = st.columns(7) # 6 seats + 1 aisle
        for idx, c in enumerate(cols):
            col_idx = idx if idx < 3 else idx + 1
            seat_id = f"{r}{c}"
            
            # Determine seat type and price
            price = 0
            if r == 1: price = 500 # Front row
            elif c in ['A', 'F']: price = 200 # Window
            elif c in ['C', 'D']: price = 200 # Aisle
            
            style = "secondary"
            if seat_id in selected_seats:
                style = "primary"
            
            with c_cols[col_idx]:
                if st.button(f"{seat_id}\n₹{price}", key=f"seat_{seat_id}", type=style):
                    if seat_id in selected_seats:
                        selected_seats.remove(seat_id)
                    else:
                        if len(selected_seats) < st.session_state.search_params['passengers']['Adults']:
                            selected_seats.append(seat_id)
                        else:
                            st.warning("Max seats selected")
                    
                    st.session_state.seat_selection['outbound'] = selected_seats
                    st.rerun()
                    
        with c_cols[3]:
            st.write("") # Aisle
            
    c1, c2 = st.columns([6, 1])
    with c2:
        if st.button("Continue to Add-ons", type="primary"):
            st.session_state.step = 3.8 # Addons
            st.rerun()
    with c1:
        if st.button("Back"):
            st.session_state.step = 3
            st.rerun()
