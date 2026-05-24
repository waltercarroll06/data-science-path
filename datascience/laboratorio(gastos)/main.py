import pandas as pd
import os 
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Usuario:
    def __init__(self,nombre,salario):
        self.nombre = nombre
        self.salario = salario
        


class Gastos:

    def __init__(self,usuario):
            self.usuario = usuario
            if not os.path.exists("gastos_personales.csv"):
                with open("gastos_personales.csv", "w") as f:
                    f.write("categoria,nombre,precio\n")
        
    def agregar(self):
        try:
            categorias = {
                "1": "Comida",
                "2": "Transporte",
                "3": "Entretenimiento",
                "4": "Salud",
                "5": "Ropa",
                "6": "Educacion",
                "7": "Servicios",
                "8": "Otro"
            }
            for i , c in categorias.items():
                print(f"{i}. {c}")
            opcion_categoria = int(input("ingresa la opcion de la categoria: "))
            if opcion_categoria >= len(categorias):
                return "ingresa un numero valido"
            nombre_gasto = input("ingresa nombre del gasto: ")
            cantidad_gasto = int(input("ingresa el precio del gasto: "))
            if cantidad_gasto < 0:
                return f"ingresa solo precio mayores a 0"
            # si todo esta bien se agrega al with open
            
            with open ("gastos_personales.csv", "a") as f:
                f.write(f"{categorias[f"{opcion_categoria}"]},{nombre_gasto},{cantidad_gasto}\n")
            
        except ValueError:
            print("error")
            
    def ver_gastos(self):
        df = pd.read_csv("gastos_personales.csv")
        print(df)
    
    
    def total(self):
        df = pd.read_csv("gastos_personales.csv")
        total = df["precio"].sum()
        print(f"total a pagar: {total}")
    
    def total_categotoria(self):
        df = pd.read_csv("gastos_personales.csv")
        total = df.groupby("categoria")["precio"].sum()
        print(total) 
    
    def resumen_usuario(self,salario):
        df = pd.read_csv("gastos_personales.csv")
        suma = df["precio"].sum()
        total = salario - suma
        print(f"salario: {salario}\ngastos: {suma}\nrestante: {total}")
    
    

    # creamos el objeto usuario
try:
        n_usuario = input("ingresa tu nombre de usuario: ")
        s_usuario = int(input("ingresa tu salario: "))
        u1 = Usuario(n_usuario,s_usuario)
        g = Gastos(u1)
except ValueError:
        print("error")
        exit()
        
print(f"bienvenido {u1.nombre}\n")

while True:
    menu = {
    "1": "Agregar gasto",
    "2": "Ver todos los gastos",
    "3": "Ver total gastado",
    "4": "Ver gastos por categoría",
    "5": "Ver resumen",
    "6": "Salir"
    }
    #mostar menu
    for i,c in menu.items():
        print(f"{i}. {c}")
    # opciones 
    opcion = input("ingresa el numero de la opcion que desee: ")
    if opcion == "6":
        print("vuelva pronto")
        break
    elif opcion == "1":
        g.agregar()
    elif opcion == "2":
        g.ver_gastos()
    elif opcion == "3":
        g.total()
    elif opcion == "4":
        g.total_categotoria()
    elif opcion == "5":
        g.resumen_usuario(u1.salario)
    else:
        print("opcion no valida")








