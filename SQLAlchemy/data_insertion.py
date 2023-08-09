from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from datetime import datetime
from database_setup import Base, WeatherData

engine = create_engine('sqlite:///weather_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

data = pd.read_csv('../datos_clima_ultimos_5_dias.csv')

for index, row in data.iterrows():
    date = datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S')
    sunset = datetime.strptime(row['sunset'], '%Y-%m-%d %H:%M:%S')
    dt = datetime.strptime(row['dt'], '%Y-%m-%d %H:%M:%S')
    sunrise = datetime.strptime(row['sunrise'], '%Y-%m-%d %H:%M:%S')

    weather_entry = WeatherData(
        date=date,
        lat=row['lat'],
        lon=row['lon'],
        sunset=sunset,
        dt=dt,
        sunrise=sunrise,
        temp=row['temp'],
        feels_like=row['feels_like'],
        # ...
    )
    session.add(weather_entry)

session.commit()
session.close()
