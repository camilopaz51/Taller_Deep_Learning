import requests
import pandas as pd

# URL de SECOP II
url = "https://www.datos.gov.co/resource/jbjy-vk9h.json"

# Consulta de contratos con los valores más altos
params = {
    "$select": """
        id_contrato,
        nombre_entidad,
        fecha_de_firma,
        valor_del_contrato,
        departamento,
        sector,
        tipo_de_contrato,
        modalidad_de_contratacion
    """,
    "$where": """
        fecha_de_firma >= '2016-01-01T00:00:00'
        AND fecha_de_firma < '2026-01-01T00:00:00'
        AND valor_del_contrato is not null
    """,
    "$order": "valor_del_contrato DESC",
    "$limit": 20
}

# Realizar consulta
respuesta = requests.get(url, params=params)

print("Código de respuesta:", respuesta.status_code)

# Convertir respuesta
datos = respuesta.json()

# DataFrame
df = pd.DataFrame(datos)

# Convertir valor a número
df["valor_del_contrato"] = pd.to_numeric(
    df["valor_del_contrato"],
    errors="coerce"
)

print("\n20 contratos con mayor valor:")
print(df.to_string(index=False))

print("\nTipos de datos:")
print(df.dtypes)

print("\nInformación general:")
print(df.info())