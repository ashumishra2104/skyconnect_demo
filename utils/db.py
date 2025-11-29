import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import streamlit as st

# Database Connection
# Using the connection string provided by the user
DB_CONNECTION_STRING = "postgresql://neondb_owner:npg_GSrgbJz4M9FN@ep-flat-rain-a48iwje7-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(DB_CONNECTION_STRING)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    pnr = Column(String, unique=True, index=True)
    booking_date = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Float)
    contact_email = Column(String)
    contact_phone = Column(String)
    status = Column(String, default="CONFIRMED")
    
    passengers = relationship("Passenger", back_populates="booking")
    segments = relationship("FlightSegment", back_populates="booking")

class Passenger(Base):
    __tablename__ = "passengers"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    title = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(String) # Storing as string for simplicity
    seat_number = Column(String, nullable=True)
    
    booking = relationship("Booking", back_populates="passengers")

class FlightSegment(Base):
    __tablename__ = "flight_segments"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    segment_type = Column(String) # 'outbound' or 'return'
    airline = Column(String)
    flight_number = Column(String)
    origin = Column(String)
    destination = Column(String)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    
    booking = relationship("Booking", back_populates="segments")

def init_db():
    """Initializes the database tables."""
    Base.metadata.create_all(bind=engine)

def save_booking_to_db(booking_data):
    """Saves the booking data to the database."""
    session = SessionLocal()
    try:
        # Create Booking
        booking = Booking(
            pnr=booking_data['pnr'],
            total_amount=booking_data['total_amount'],
            contact_email=booking_data['contact_email'],
            contact_phone=booking_data['contact_phone']
        )
        session.add(booking)
        session.flush() # Get ID

        # Create Passengers
        for p_data in booking_data['passengers']:
            passenger = Passenger(
                booking_id=booking.id,
                title=p_data['title'],
                first_name=p_data['first_name'],
                last_name=p_data['last_name'],
                dob=str(p_data['dob']),
                seat_number=p_data.get('seat')
            )
            session.add(passenger)

        # Create Flight Segments
        for seg_type, flight in booking_data['flights'].items():
            if flight:
                segment = FlightSegment(
                    booking_id=booking.id,
                    segment_type=seg_type,
                    airline=flight['airline'],
                    flight_number=flight['flight_number'],
                    origin=flight['origin'],
                    destination=flight['destination'],
                    departure_time=flight['departure_time'],
                    arrival_time=flight['arrival_time']
                )
                session.add(segment)

        session.commit()
        return True
    except Exception as e:
        session.rollback()
        st.error(f"Error saving booking: {e}")
        return False
    finally:
        session.close()
