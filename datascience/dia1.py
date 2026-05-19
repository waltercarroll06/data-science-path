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