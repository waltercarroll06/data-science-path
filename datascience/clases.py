import numpy as np


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

class Estudiantes:
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
            if promedio > 3.0:
                return "aprobado"
            else:
                return "reprobado"

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print("Carrera: ingenieria de sistemas")
        print(f"promedio: {np.mean(self.notas):.1f}")
        print(f"estado: {self.estado()}\n")
        
        
estudiante1 = Estudiantes("Juan")
estudiante1.agregar_nota()
estudiante1.estado()
estudiante2 = Estudiantes("ana")
estudiante2.agregar_nota()
estudiante2.estado()

estudiante1.mostrar_info()
estudiante2.mostrar_info()

