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