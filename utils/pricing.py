from datetime import datetime

def calculate_price(base_price, flight_data, booking_class="Economy", days_in_advance=30):
    """
    Calculates the final price based on various factors.
    """
    price = base_price
    
    # 1. Advance Booking Discount/Surcharge
    if days_in_advance >= 30:
        price *= 0.8  # -20%
    elif 15 <= days_in_advance < 30:
        price *= 0.9  # -10%
    elif 7 <= days_in_advance < 15:
        pass # 0%
    else:
        price *= 1.25 # +25%
        
    # 2. Weekend Surcharge (Friday, Saturday, Sunday)
    # Assuming flight_data['departure_time'] is a datetime object
    dept_time = flight_data['departure_time']
    if dept_time.weekday() in [4, 5, 6]: # 4=Fri, 5=Sat, 6=Sun
        price *= 1.2 # +20%
        
    # 3. Time of Day Pricing
    hour = dept_time.hour
    if 6 <= hour < 8: # Early Morning
        price *= 1.15
    elif 8 <= hour < 12: # Morning
        price *= 1.10
    elif 12 <= hour < 16: # Afternoon
        pass
    elif 16 <= hour < 20: # Evening
        price *= 1.15
    else: # Night
        price *= 0.90
        
    # 4. Class Multiplier
    if booking_class == "Premium Economy":
        price *= 1.5
    elif booking_class == "Business":
        price *= 2.5
        
    return round(price)

def calculate_taxes_and_fees(base_fare, passengers):
    """Calculates taxes and fees breakdown."""
    convenience_fee = 200
    fuel_surcharge = 500
    psf = 150 * passengers
    gst = base_fare * 0.05
    
    total_fees = convenience_fee + fuel_surcharge + psf + gst
    
    return {
        "convenience_fee": convenience_fee,
        "fuel_surcharge": fuel_surcharge,
        "passenger_service_fee": psf,
        "gst": gst,
        "total_fees": total_fees
    }
