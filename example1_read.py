from src import tkv

# Lire les données avec read_tkv
data = tkv.read_tkv("data.tkv")

# Convertir en DataFrame
df = tkv.tkv_to_df(data)
print(df)
