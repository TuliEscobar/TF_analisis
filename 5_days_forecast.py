import pandas as pd
import requests
import datetime

from pandas import json_normalize
from datetime import datetime as dt

from config import *


if __name__ == '__main__':

    lat = -27.4606  # Latitud de la ubicación
    lon = -58.9839   # Longitud de la ubicación

    # Obtener la fecha actual en formato Unix (UTC)
    current_time = datetime.datetime.utcnow()
    end_time = current_time.timestamp()

    # Crear una lista para almacenar los datos de los últimos 5 días junto con la fecha
    weather_data_list = []

    # Generar las fechas para los últimos 5 días
    for i in range(1, 6):
        # Restar i días a la fecha actual
        date = current_time - datetime.timedelta(days=i)
        start_time = date.timestamp()

        # Llamada a la API con la fecha correspondiente
        url = f"{url2}?lat={lat}&lon={lon}&units=metric&lang=es&dt={int(start_time)}&appid={API_KEY}"
        response = requests.get(url)
        weather_data = response.json()
        
        # Normalizar la estructura dentro de "Clima" y agregarla a la lista
        climate_data = weather_data["data"]
        normalized_climate_data = json_normalize(climate_data)
        
        # Agregar la fecha a los datos del clima y agregarlos a la lista
        for item in weather_data["data"]:
            
            weather_data_with_date = {
                "date": date.strftime("%Y-%m-%d %H:%M:%S"),
                "lat": weather_data["lat"],
                "lon": weather_data["lon"],
                **item
            }
            weather_data_list.append(weather_data_with_date)

    # Crear un DataFrame a partir de la lista de datos
    df = pd.DataFrame(weather_data_list)
    
    #modificar tiempo a datetime
    timestamp_columns = ["sunset", "dt", "sunrise"]  # Agrega aquí el resto de las columnas con timestamps

    for col in timestamp_columns:
        df[col] = df[col].apply(lambda x: dt.utcfromtimestamp(x))

    print(df)

    # Guardar el DataFrame en un archivo CSV
    csv_filename = "datos_clima_ultimos_5_dias.csv"
    df.to_csv(csv_filename, index=False)

    print(f"Datos guardados en {csv_filename}")


