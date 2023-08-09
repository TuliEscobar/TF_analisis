from sqlalchemy import Column, Integer, Float, DateTime, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    lat = Column(Float)
    lon = Column(Float)
    sunset = Column(Integer)
    dt = Column(Integer)
    sunrise = Column(Integer)
    temp = Column(Float)
    feels_like = Column(Float)
    pressure = Column(Integer)
    humidity = Column(Integer)
    dew_point = Column(Float)
    uvi = Column(Float)
    clouds = Column(Integer)
    visibility = Column(Integer)
    wind_speed = Column(Float)
    wind_deg = Column(Integer)
    weather = Column(JSON)
