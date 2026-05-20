import pandas as pd
import numpy as np

#$ ¿Qué es un DataFrame?Es la estructura principal de Pandas.
# Piénsalo como una tabla de Excel pero dentro de Python — tiene filas, columnas y nombres para todo.


ventas = np.array([
    [150, 200, 180, 220],
    [130, 170, 190, 210],
    [180, 160, 200, 190]
])
vendedores = ["carlos", "diana", "elena"]
semanas = ["sem1", "sem2", "sem3", "sem4"]
df = pd.DataFrame(ventas, index=vendedores, columns=semanas)
print(df)


salario = np.array([
    [3500,3700,3600],
    [4200,4100,4300],
    [3800,3900,4000],
    [3100,3200,3150]
])

vendedoresss = ["ana", "luis", "maria", "pedro"]
mes = ["enero", "febrero", "marzo"]

df_salarios = pd.DataFrame(salario , index=vendedoresss, columns=mes)
print(df_salarios)
print(df_salarios.shape)

print(df_salarios["enero"])
print(df_salarios.loc["luis"])
print(df_salarios.loc["maria", "febrero"])

sal_promedio = df_salarios.mean(axis=1)
sal_promedio_mes = df_salarios.mean()
print(sal_promedio_mes)
print(sal_promedio)
print(sal_promedio.idxmax())
df_salarios["promedio"] = sal_promedio
print(df_salarios)

print(df_salarios[df_salarios["promedio"] > 3600])
print(df_salarios[df_salarios["marzo"] > 4000])
df_salarios["Estado"] = np.where(df_salarios["promedio"] > 3600, "Alto", "Bajo")
print(df_salarios)

ventas = ([
    [1200,1350,1100],
    [800,750,900],
    [950,1000,980],
    [650,700,680],
    [1100,1200,1150]      
])

productos = ["arroz","aceite","leche","azucar","cafe"]
mes = ["enero", "febrero", "marzo"]
df_ventas = pd.DataFrame(ventas,index=productos, columns=mes)
col_total = df_ventas.sum(axis = 1)
df_ventas["Total"] = col_total
print(df_ventas)
col_promedio = df_ventas.mean(axis = 1)
df_ventas["Promedio"] = col_promedio
print(df_ventas)
col_estado = np.where(df_ventas["Total"] > 3000, "estrella", "nromal")
df_ventas["Estado"] = col_estado
print(df_ventas)   
print(df_ventas["Total"].idxmax())  
print(df_ventas[df_ventas["Estado"] == "estrella"])
mes_mayor_ventas = df_ventas[["enero","febrero","marzo"]].sum()
df_ventas.loc["totalXmes"] = mes_mayor_ventas
print(df_ventas[mes_mayor_ventas.idxmax()])

#  * voy a empzar a poner comentarios para que se vea mas organizado el codigo y
#  * se entienda mejor lo que estoy haciendo en cada paso 


# ! parte 1(base)
datos = np.array([
    [14,16,13,15,17],
    [24,26,25,23,27],   
    [28,30,29,31,28],
    [28,33,29,31,28]
])

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
ciudades = ["bogota", "medellin", "cali", "cartagena"]

df_temperaturas = pd.DataFrame(datos, index=ciudades, columns=dias)
print(df_temperaturas)
print(df_temperaturas.shape)

# ! parte 2 (analisis con pandas)


col_promedio = df_temperaturas.mean(axis=1)
df_temperaturas["Promedio"] = col_promedio
col_max_temp = df_temperaturas.max(axis=1)
df_temperaturas["Maxima"] = col_max_temp
print(df_temperaturas["Promedio"].idxmax())
print(df_temperaturas[df_temperaturas["Promedio"] > 25 ])

# ! parte 3 (numpy directo)

temp_mayor = np.argmax(datos)
print(temp_mayor)
ciaudad_mayor_temp = np.unravel_index(temp_mayor, datos.shape)
print(ciaudad_mayor_temp)

c = ciaudad_mayor_temp[0]
d = ciaudad_mayor_temp[1]

print(f"La ciudad con la temperatura más alta es: {ciudades[c]} y el día es: {dias[d]} con una temperatura de {datos[c][d]} grados" )