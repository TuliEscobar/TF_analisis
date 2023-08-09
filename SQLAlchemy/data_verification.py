from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import WeatherData

engine = create_engine('sqlite:///weather_database.db')
Session = sessionmaker(bind=engine)
session = Session()

inserted_records = session.query(WeatherData).all()

for record in inserted_records:
    print(f"ID: {record.id}, Date: {record.date}, Lat: {record.lat}, Lon: {record.lon}, Temp: {record.temp}, Feels Like: {record.feels_like}, ...")

session.close()
