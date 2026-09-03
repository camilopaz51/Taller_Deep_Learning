import requests
import pandas as pd

# URL de la API de SECOP II
url = "https://www.datos.gov.co/resource/jbjy-vk9h.json"

# Consulta agrupada por año
params = {
    "$select": """
        date_extract_y(fecha_de_firma) as anio,
        count(*) as cantidad_contratos,
        sum(valor_del_contrato) as valor_total
    """,
    "$where": """
        fecha_de_firma >= '2016-01-01T00:00:00'
        AND fecha_de_firma < '2026-01-01T00:00:00'
    """,
    "$group": "anio",
    "$order": "anio",
    "$limit": 100
}

# Realizar consulta
respuesta = requests.get(url, params=params)

print("Código de respuesta:", respuesta.status_code)

# Convertir respuesta
datos = respuesta.json()

# Convertir a DataFrame
df = pd.DataFrame(datos)

# Convertir columnas numéricas
df["anio"] = pd.to_numeric(df["anio"], errors="coerce")
df["cantidad_contratos"] = pd.to_numeric(
    df["cantidad_contratos"], errors="coerce"
)
df["valor_total"] = pd.to_numeric(
    df["valor_total"], errors="coerce"
)

print("\nResultados:")
print(df)


print("\nPrimer año disponible:", int(df["anio"].min()))
print("Último año disponible:", int(df["anio"].max()))
print("Cantidad de años:", df["anio"].nunique())

# Guardar resultados
df.to_csv(
    "datos/procesados/secop_ii_resumen_anual.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nArchivo guardado correctamente.")