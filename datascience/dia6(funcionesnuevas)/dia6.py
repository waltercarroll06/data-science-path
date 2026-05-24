import pandas as pd
import os 
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))



df = pd.read_csv("estudiantes.csv")
print(df.shape)
print(df.head())        # primeras 5 filas
print(df.dtypes)        # tipos de columnas

bogota = df[df["ciudad"] == "Bogota"]
print(bogota)
print(df[df["nota"] > 4.0])
m = df[df["materia"] == "Matematicas"]
print(m[m["nota"] > 3.0])
print(f"otra forma es:\n")
print(df[(df["materia"] == "Matematicas") & (df["nota"] > 3.0 )])


print(df[(df["ciudad"] == "Cali") | (df["ciudad"] == "Medellin")])



df2 = pd.read_csv("ventas.csv")
print(df2.shape)
col_total = df2[["enero","febrero","marzo","abril","mayo"]].sum(axis = 1)
df2["total"] = col_total
col_prom =df2[["enero","febrero","marzo","abril","mayo"]].mean(axis = 1)
df2["promedio"] = col_prom
col_estado = np.where(df2["promedio"] > 1200,"estrella","regular")
df2["estado"] = col_estado
print(df2)
df2.to_csv('ventas.csv', index=False)
print(f"vendedor con mas ventas fue: {df2.loc[df2['total'].idxmax(),'vendedor']}")