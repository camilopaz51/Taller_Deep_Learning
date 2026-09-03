import requests

url = "https://www.datos.gov.co"

respuesta = requests.get(url)

print("Código de respuesta:", respuesta.status_code)