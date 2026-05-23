import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Fruta:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

class Tienda:
    def __init__(self,nombre):
        self.nombre = nombre
        self.menu = []
    
    def mostrar_menu(self):
      for index ,producto in enumerate(self.menu):
          print(f"{index}. {producto.nombre} --> precio: {producto.precio}")
          
    def agregar_inventario(self, fruta):
        for f in fruta:
            self.menu.append(f)
     
    def selecionar(self,opcion,cantidad):
        return self.menu[opcion], cantidad
            

class Venta:
    def __init__(self):
        self.items = []
    
    def agregar(self,fruta,cantidad):
        self.items.append({"fruta" : fruta , "cantidad": cantidad})
    
    def a_dataframe(self):
        lista = []
        for f in self.items:
            lista.append({"fruta": f["fruta"],
            "cantidad": f["cantidad"]
            })
        df = pd.DataFrame(lista)
        return df
    
    
    def guardar_csv(self):
        df = self.a_dataframe()
        df.to_csv("tienda_frutas.csv" , index = False)
        
    def leer_csv(self):
        df = pd.read_csv("tienda_frutas.csv") 
        return df
        
venta = Venta()
tienda = Tienda("D1")
f1 = Fruta("Manzana", 1500)
f2 = Fruta("Banano", 800)
f3 = Fruta("Naranja", 1200)
f4 = Fruta("Mango", 2000)
f5 = Fruta("Fresa", 3500)
f6 = Fruta("Uva", 4000)
f7 = Fruta("Sandia", 5000)
# ! opcion y cantidad del usuario 
tienda.agregar_inventario([f1,f2,f3,f4,f5,f6,f7])
tienda.mostrar_menu()
while True:
    try:
            
            opcion = int(input("ingresa el numero del producto que quiere(enter para salir): "))
            cantidad = int(input("ingresa la cantidad que quiere: "))
            if opcion >= len(tienda.menu):
                print("error")
                break
            else:
                fruta , cantidad = tienda.selecionar(opcion,cantidad)
                venta.agregar(fruta.nombre,cantidad)
    except ValueError:
            print("solo puede ingresa los numeros del menu")
            break
venta.a_dataframe()
venta.guardar_csv()
df = venta.leer_csv()

mas_vendida = df.groupby("fruta")["cantidad"].sum().idxmax()
menos_vendida = df.groupby("fruta")["cantidad"].sum().idxmin()
print(f"Fruta más vendida: {mas_vendida}")
print(f"Fruta menos vendida: {menos_vendida}")
