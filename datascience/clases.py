import numpy as np
import pandas as pd


# ! ejericico 1 dia 1

class Experimiento:
    def __init__(self, name,mediciones = None):
        self.name = name
        self.mediciones = mediciones if mediciones is not None else []

    def Promedio(self):
        promedio = sum(self.mediciones) / len(self.mediciones)
        return promedio
    def Describir(self):
            print(f"nombre: {self.name} | Medición: {self.mediciones} | Promedio: {round(self.Promedio(), 2)}")


experimento1 = Experimiento("Experimento 1", [10, 20, 30, 40, 50])
experimento1.Promedio()
experimento1.Describir()



# ! ejercicio 2 dia 2
class Estudiante:
    def __init__(self, nombre,  notas = None):
        self.nombre = nombre
        self.notas = notas if notas is not None else np.array([])
    
    
    def agregar_nota(self):
        print(f"Agregando nota para {self.nombre}")
        while True:
            opcion= input("¿Desea agregar una nota? (s/n): ")
            if opcion.lower() == 's':
                try:
                    nota = float(input("Ingrese la nota del estudiante: "))
                    if 0 <= nota <= 5.0:
                        self.notas = np.append(self.notas, nota)
                    else:
                        print("La nota debe estar entre 0 y 5.0.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
            elif opcion.lower() == 'n':
                break
            else:
                print("Opción no válida. Por favor, ingrese 's' o 'n'.")


    def promedio(self):
        if len(self.notas) > 0:
            print(f"Promedio de {self.nombre}: {np.mean(self.notas):.1f}")
        else:
            return f"El estudiante {self.nombre} no tiene notas registradas."
        
    def nota_mayor(self):
        if len(self.notas) == 0:
            return f"El estudiante {self.nombre} no tiene notas registradas."
        else:
            nota_mayor = np.max(self.notas)
            print(f"La nota mayor de {self.nombre} es: {nota_mayor:.1f}")
    
    def estado(self):
        if len(self.notas) == 0:
            return f"El estudiante {self.nombre} no tiene notas registradas."
        else:
            promedio = np.mean(self.notas)
            if promedio >= 3.0:
                return "aprobado"
            else:
                return "reprobado"

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print("Carrera: ingenieria de sistemas")
        print(f"promedio: {self.promedio()}")
        print(f"estado: {self.estado()}\n")
        
        
estudiante1 = Estudiante("Juan")
estudiante1.agregar_nota()
estudiante1.estado()
estudiante1.promedio()
estudiante2 = Estudiante("ana")
estudiante2.agregar_nota()
estudiante2.estado()
estudiante2.promedio()


estudiante1.mostrar_info()
estudiante2.mostrar_info()

# ! ejericcio 3 dia 3 ( solo numpy)

# Crea un DataFrame con tus 5 canciones o artistas favoritos

# Columnas:
# "artista"
# "genero"
# "popularidad"  → número del 1 al 100 tú mismo
# "año"

# Luego:
# 1. Filtra los que tienen popularidad mayor a 70
# 2. ¿Cuál tiene la mayor popularidad? — idxmax()
# 3. Agrega columna "era" → "clásico" si el año es menor a 2010, si no "moderno"

artistas = np.array([
    ["The Beatles", "Rock", 95, 1965],
    ["Beyoncé", "Pop", 90, 2013],
    ["Bob Marley", "Reggae", 85, 1975],
    ["Taylor Swift", "Pop", 80, 2015]
])

df_artistas = pd.DataFrame(artistas, columns=["artista", "genero", "popularidad", "año"])
print(df_artistas)
popularidad_alta = df_artistas.loc[df_artistas["popularidad"].idxmax()]
print(df_artistas["artista"].iloc[popularidad_alta.name])
#iloc se usa para saber el indice de una fila o columan (utlizando [: x numero de columan o columnas ]) en este caso para saber la popularidad 
# mas alta la varibale pupularidad_alta nos da 0 es signifca que al hacer iloc [0] quiere decir que es la fila 0

col_era = np.where(df_artistas["año"].astype(int) < 2010, "clasico", "moderno")
df_artistas["era"] = col_era
print(df_artistas)




# ! ejercicio 4 dia 3 (clases, numpy y pandas)

class Artistas:
    
    lista = []
    
    def __init__(self,nombre,cancion,año,ranking):
        self.nombre = nombre
        self.cancion = cancion
        self.año = año
        self.ranking = ranking

lista = []
    
def listas(cancion):
    lista.append(cancion)
        


c1 = Artistas("Bad Bunny", "Monaco", 2023, 12)
c2 = Artistas("The Weeknd", "Blinding Lights", 2020, 4)
c3 = Artistas("Queen", "Bohemian Rhapsody", 1975, 8)
c4 = Artistas("Taylor Swift", "Cruel Summer", 2019, 45)

listas(c1)
listas(c2)
listas(c3)
listas(c4)



df_artistas = pd.DataFrame([vars(c) for c in lista])
print(df_artistas)
ranking = df_artistas[df_artistas["ranking"] < 20]
print(ranking)
print(f"artista con la cancion con mejor rankin es: {df_artistas.loc[df_artistas["ranking"].argmin(), "nombre"]}")



class Videojuego:
    def __init__(self,nombre,genero,año,horas_jugadas):
        self.nombre = nombre
        self.año = año
        self.horas_jugadas = horas_jugadas
        self.genero = genero


juegos = []

def agregar_juego(v):
    juegos.append(v)

v1 = Videojuego("minecraft", "superviviencia",2011, 46)
v2 = Videojuego("fortnite", "pvp",2015, 100)
v3 = Videojuego("lol", "pvp",2006, 20)
v4 = Videojuego("brawhall", "pvp",2010, 55)
v5 = Videojuego("zelda", "mundo abierto",1999, 32)
agregar_juego(v1)
agregar_juego(v2)
agregar_juego(v3)
agregar_juego(v4)
agregar_juego(v5)

lista = []


for v in juegos:
    
    lista.append({
        "titulo": v.nombre,
        "genero" : v.genero,
        "año": v.año,
        "horas jugadas": v.horas_jugadas
    })

df_videojugo = pd.DataFrame(lista)
print(df_videojugo)
print(df_videojugo[df_videojugo["horas jugadas"] > 40])
mas_jugado  = df_videojugo["horas jugadas"].argmax()
print(mas_jugado)
print(df_videojugo.loc[mas_jugado,"titulo"])
fil_promedio = df_videojugo["horas jugadas"].mean()
df_videojugo.loc["promedio"] = ["-","-","-", fil_promedio]
print(df_videojugo)


# ! ejericcio 5 (restaruante)


# * class madre
class Restaurante:
    
    def __init__(self,nombre,tipo_comida,clasificacion ,ciudad):
        self.nombre = nombre
        self.tipoComida = tipo_comida
        self.clasificacion = float(clasificacion)
        self.ciudad = ciudad
        
 
# * creamos la funcion para agragar los objetos en una lista para luego agregarlos al dataframe
 
restaurantes = []
def agregar_restaurante(r):
    restaurantes.append(r)
 
r1 = Restaurante("Arabe Gourmet", "Arabe", 4.8, "Medellin")
r2 = Restaurante("Narcobollo", "Costeña", 4.5, "Barranquilla")
r3 = Restaurante("Pizzeria Italiana", "Italiana", 4.2, "Bogota")
r4 = Restaurante("La Cueva", "Internacional", 4.7, "Valledupar")
r5 = Restaurante("KFC", "Comida Rapida", 4.0, "Barranquilla")
r6 = Restaurante("Dominos Pizza", "Pizza", 4.3, "Bogota")
r7 = Restaurante("Burger King", "Hamburguesas", 3.9, "Barranquilla")
r8 = Restaurante("Subway", "Sandwiches", 4.1, "Medellin")
r9 = Restaurante("Sarab", "Arabe", 4.9, "Cali")
r10 = Restaurante("Cuzco Cocina Peruana", "Peruana", 4.6, "Cali")

agregar_restaurante(r1)
agregar_restaurante(r2)
agregar_restaurante(r3)
agregar_restaurante(r4)
agregar_restaurante(r5)
agregar_restaurante(r6)
agregar_restaurante(r7)
agregar_restaurante(r8)
agregar_restaurante(r9)
agregar_restaurante(r10)

lista = []

for r in restaurantes:
    
    lista.append({
        "nombre": r.nombre,
        "tipo de comida": r.tipoComida,
        "clasificacion" : r.clasificacion,
        "ciudad": r.ciudad
    })
    
# * creamos el data frame

df_restaurante = pd.DataFrame(lista)


# variables para filtrar por ciudades 
barranquilla = df_restaurante.loc[df_restaurante["ciudad"] == "Barranquilla"]
cali = df_restaurante[df_restaurante["ciudad"] == "Cali"]
medellin = df_restaurante[df_restaurante["ciudad"] == "Medellin"]
bogota = df_restaurante[df_restaurante["ciudad"] == "Bogota"]


promedio = round(barranquilla["clasificacion"].mean(), 2)
barranquilla.loc["promedio"] = ["-","-", promedio,"-"]
print(barranquilla)

promedio = round(cali["clasificacion"].mean(), 2)
cali.loc["promedio"] = ["-","-", promedio,"-"]
print(cali)


mejor_cl = df_restaurante["clasificacion"].argmax()
print(f"el mejor restaurante claisificado es: {df_restaurante.loc[mejor_cl,"nombre"]} de la ciudad de {df_restaurante.loc[mejor_cl,"ciudad"]} ")