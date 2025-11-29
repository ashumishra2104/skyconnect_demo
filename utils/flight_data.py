import pandas as pd
import random
from datetime import datetime, timedelta

AIRLINES = [
    {"name": "IndiGo", "code": "6E"},
    {"name": "Air India", "code": "AI"},
    {"name": "SpiceJet", "code": "SG"},
    {"name": "Vistara", "code": "UK"},
    {"name": "AirAsia", "code": "I5"}
]

def generate_flights(date, origin, destination):
    """Generates mock flights for a given date and route."""
    flights = []
    # Generate 15 flights per day
    for i in range(15):
        airline = random.choice(AIRLINES)
        flight_num = f"{airline['code']}-{random.randint(100, 999)}"
        
        # Random departure time between 5 AM and 10 PM
        hour = random.randint(5, 22)
        minute = random.choice([0, 15, 30, 45])
        dept_time = datetime.combine(date, datetime.min.time()) + timedelta(hours=hour, minutes=minute)
        
        # Duration between 1h 15m and 1h 45m for HYD-GOI
        duration_minutes = random.randint(75, 105)
        arrival_time = dept_time + timedelta(minutes=duration_minutes)
        
        stops = random.choice(["Non-stop", "Non-stop", "Non-stop", "1 Stop"]) # Mostly non-stop
        
        base_price = 3500 # Base reference price
        
        flights.append({
            "id": f"FL-{i}",
            "airline": airline["name"],
            "flight_number": flight_num,
            "origin": origin,
            "destination": destination,
            "departure_time": dept_time,
            "arrival_time": arrival_time,
            "duration": f"{duration_minutes // 60}h {duration_minutes % 60}m",
            "stops": stops,
            "base_price": base_price
        })
        
    return pd.DataFrame(flights)
