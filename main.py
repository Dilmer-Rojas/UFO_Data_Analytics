import pandas as pd
import yaml

# Cargar configuración
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Cargar datos
df = pd.read_csv(config["data_paths"]["raw"] + "dataset1.csv")

# Análisis rápido
print(df.info())
print(df.describe())

# Guardar resumen
df.describe().to_csv(config["data_paths"]["outputs"] + "resumen.csv")

print("✅ Análisis completado y guardado en outputs/")
