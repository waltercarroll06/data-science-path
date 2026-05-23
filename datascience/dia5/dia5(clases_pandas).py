import pandas as pd
import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Estudiante:
    def __init__(self,nombre,edad , notas = None):
        self.notas = notas if notas is not  None else []
        self.nombre = nombre
        self.edad = edad
        
    def promedio(self):
        promedio = sum(self.notas) / len(self.notas)
        return round(promedio , 2)
        
    def estado(self):
        if   sum(self.notas) / len(self.notas) >= 3.0:
            return "aprobado"
        else:
            return "reprobado"
        
class Salon:
    def __init__(self,nombre):
        self.nombre = nombre 
        self.notas = []
    
    def agregar_estudiante(self,estudiante):
        dic = {
            "nombre" : estudiante.nombre,
            "edad" : estudiante.edad, 
            "promedio" : estudiante.promedio(),
            "estado" : estudiante.estado()
        }
        self.notas.append(dic)
        
    def a_dataframe(self):
        df = pd.DataFrame(self.notas)
        return df
    
    
    def guardar_csv(self):
       df = self.a_dataframe()
       df.to_csv("dia_5.csv" , index = False)

    
    def leer_csv(self):
          df = pd.read_csv("dia_5.csv")
          return df
    
        
        
e1 = Estudiante("juan", 14, [3.3 , 3.5 , 4.5])
e2 = Estudiante("maria",15,  [3.8 , 4.5 , 1.5])
e3 = Estudiante("walter", 16, [4.3 , 2.5 , 3.5])
e4 = Estudiante("aleja", 16, [1.3 , 2.5 , 3.5])
e5 = Estudiante("mario", 16, [2.3 , 2.5 , 3.5])
salon = Salon("11a")
salon.agregar_estudiante(e1)
salon.agregar_estudiante(e2)
salon.agregar_estudiante(e3)
salon.agregar_estudiante(e4)
salon.agregar_estudiante(e5)
salon.guardar_csv()
df = salon.leer_csv()
print(df[df["estado"] == "aprobado"])

print("")


class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio


class Tienda:
    def __init__(self,nombre):
        self.nombre = nombre 
        self.carrito = []
        
    def agregar_carrito(self , productos):
        for i in productos:
            self.carrito.append(i)
    
    def info(self):
        for index,i  in enumerate(self.carrito, 1):
            print(f"{index}. nombre: {i.nombre} precio: {i.precio}") 
    
    def total(self):
        total = 0
        for i in self.carrito:
            total += i.precio
        return total
            
    def a_dataframe(self):
        df = pd.DataFrame(vars(c)for c in self.carrito)
        return df
    
    def guardar_csv(self):
        df = self.a_dataframe()
        df.to_csv("dia_5(ejericicio2).csv" , index = False)
    
    def filtrar(self):
        df = pd.read_csv("dia_5(ejericicio2).csv")
        return df
        
        
        
        
        
        
        
p1 = Producto("manzana", 15000)
p2 = Producto("pera", 13000)
p3 = Producto("sandia", 18000)

tienda = Tienda("D1")
tienda.agregar_carrito([p1,p2,p3])
print(tienda.info())
print(f"total de tu compra es {tienda.total()}")
df = tienda.a_dataframe()
linea_total = df["precio"].sum()
df.loc["total"] = ["-",linea_total]
tienda.guardar_csv()
total = tienda.filtrar()
print(total[total["precio"] != "-"])