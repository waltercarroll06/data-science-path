import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


df = pd.read_csv("ventas_tienda.csv")

print(df.head())
print(df.shape)
print(df.dtypes)
print(df.describe())
print(df.loc[df["precio"].idxmax(), "producto"])
ciudad = df.loc[df["ciudad"] == "Bogota"]
print(ciudad["cantidad"].sum())

col_venta = df["precio"] * df["cantidad"]
df["total_venta"] = col_venta
print(df)
print(df.loc[df["total_venta"].idxmax(), "ciudad"])
print(df.groupby("ciudad")["total_venta"].sum().idxmax())