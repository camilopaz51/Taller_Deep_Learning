import requests
import pandas as pd

# URL de la API de SECOP II
url = "https://www.datos.gov.co/resource/jbjy-vk9h.json"

# Parámetros de la consulta
params = {
    "$limit": 10
}

# Realizar consulta
respuesta = requests.get(url, params=params)

# Verificar que la consulta fue exitosa
print("Código de respuesta:", respuesta.status_code)

# Convertir la respuesta JSON en una lista de datos
datos = respuesta.json()

# Convertir los datos a un DataFrame
df = pd.DataFrame(datos)

# Mostrar los datos
print("\nPrimeros registros:")
print(df)

# Mostrar las columnas disponibles
print("\nColumnas:")
print(df.columns.tolist())