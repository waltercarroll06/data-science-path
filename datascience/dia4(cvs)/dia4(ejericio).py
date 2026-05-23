

class Tienda:
    
    def __init__(self,nombre):
        self.nombre = nombre
        
    
    
    def menu():
        menu = {
        "1": {"nombre": "Manzana", "precio": 1500},
        "2": {"nombre": "Banano", "precio": 800},
        "3": {"nombre": "Naranja", "precio": 1200},
        "4": {"nombre": "Mango", "precio": 2000},
        "5": {"nombre": "Fresa", "precio": 3500},
        "6": {"nombre": "Uva", "precio": 4000},
        "7": {"nombre": "Sandia", "precio": 5000},
        
        }
        print(menu)
        
class Fruta:
    
    def __init__(self,nombre,cantidad,precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        
    def info(self):
        print(f"{self.nombre} x{self.cantidad}, cada {self.nombre} tiene el precio de {self.precio}.")


class Venta:
    
    def __init__(self,opcion,cantidad):
        self.nombre = opcion
        self.cantidad = cantidad
    
    
    def agregar_carrito(self):
        pass