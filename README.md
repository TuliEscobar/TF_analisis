# Weather Data Analysis - Últimos 5 Días
Este proyecto se centra en la obtención y análisis de datos climáticos para una ubicación geográfica específica en los últimos 5 días. Se utiliza la API de clima para recopilar información meteorológica y luego se procesa y almacena en un archivo CSV para su posterior análisis. Este proyecto es parte de un curso de análisis de datos y utiliza herramientas como Pandas, Requests y SQLAlchemy.

## Requisitos
Antes de ejecutar el código, asegúrate de tener instaladas las siguientes bibliotecas de Python:

* pandas
* requests
* sqlalchemy

Además, necesitas obtener una clave de API de la fuente de datos meteorológicos. Puedes obtener una clave registrándote en la plataforma que proporciona los datos meteorológicos y luego configurarla en un archivo llamado config.py de la siguiente manera:
API_KEY = "tu_clave_de_api_aqui"

## Configuración de la Ubicación
El código está configurado para obtener datos climáticos para una ubicación geográfica específica. Puedes ajustar la latitud y longitud en las variables lat y lon respectivamente, para obtener datos para la ubicación de tu interés.

## Ejecución del Código
Para ejecutar el código, simplemente inicia el archivo Python. El script realizará lo siguiente:

Generará fechas para los últimos 5 días a partir de la fecha actual.
Realizará llamadas a la API de clima para cada día y obtendrá los datos meteorológicos.
Normalizará los datos obtenidos y los almacenará en un DataFrame de Pandas.
Convertirá las marcas de tiempo a formato de fecha y hora.
Guardará los datos en un archivo CSV llamado datos_clima_ultimos_5_dias.csv.

## Resultados
Después de la ejecución, obtendrás un archivo CSV que contiene datos climáticos para los últimos 5 días. Puedes usar esta información para análisis posterior y visualización de datos.