import pandas as pd
import requests

from datetime import datetime as dt
from pandas import json_normalize

from config import *


if __name__ == '__main__':

    df_todas_ciudades = pd.DataFrame()

    # Lista con las coordenadas en formato "latitud&longitud"
    coord_list = ["lat=51.5156177&lon=0.0919983", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64",
                  "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]
    city_list = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico City", "Dublin", "Tbilisi", "Bogota", "Tokio"]

    def get_weather_data(city):
        api_key = API_KEY
        url = f"{url1}?q={city}&units=metric&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            response_json = response.json()
            return response_json

    for city in city_list:
        weather_data = get_weather_data(city)
        normalize_weather = json_normalize(weather_data)

        # Convertir los datos del clima directamente a un DataFrame de pandas
        df = pd.DataFrame(normalize_weather)

        #modificar tiempo a datetime
        timestamp_columns = ["sys.sunset", "dt", "sys.sunrise"]  # Agrega aquí el resto de las columnas con timestamps

        for col in timestamp_columns:
            df[col] = df[col].apply(lambda x: dt.utcfromtimestamp(x))
            
        # Agregar una columna con el nombre de la ciudad
        df = df.assign(City=city)

        # Concatenar el DataFrame de la ciudad actual con el DataFrame grande
        df_todas_ciudades = pd.concat([df_todas_ciudades, df])

    print(df_todas_ciudades)

