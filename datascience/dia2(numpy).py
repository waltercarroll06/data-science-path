
import numpy as np

notas = np.array([
    [85, 92, 78],
    [90, 88, 95],
    [72, 85, 80],
    [88, 91, 87]
])

Estudiantes = ['Ana', 'Luis', 'María', 'Carlos']
for i,nombre in enumerate(Estudiantes):
    print(f"Notas de {nombre}: {notas[i]}")
    
promedioxestudiantes = np.mean(notas, axis=1)
promediomasalto= np.argmax(promedioxestudiantes)
for i,nombre in enumerate(Estudiantes):
    print(f"Promedio de {nombre}: {promedioxestudiantes[i]:.2f}")
print(f"El estudiante con el promedio más alto es: {Estudiantes[promediomasalto]} con un promedio de {promedioxestudiantes[promediomasalto]:.2f}")
    

print(notas.shape)
materias = ['Matemáticas', 'Física', 'Química']
promedio_materia = np.mean(notas,axis = 0)
for i, materia in enumerate(materias):
    print(f"Promedio de {materia}: {promedio_materia[i]:.2f}")


# ejercicio 2
print("\nEjercicio 2:")

ventas = np.array([
    [150, 200, 180,220],
    [130, 170, 190, 210],    
    [180, 160, 200, 190]
])

print(ventas.shape)

vendedores = ["carlos", "diana", "elena"]
semana = ["semana 1 ", "semana 2 ", "semana 3 ", "semana 4 "]
promedio_venta = np.mean(ventas , axis = 1)
promedio_mayor = 0
for i, nombre in enumerate(vendedores):
    print(f"promedio de ventas de cada vendedor: {nombre} = {promedio_venta[i]:.2f}")
    if promedio_mayor < promedio_venta[i]:
        promedio_mayor = promedio_venta[i]
        vendedor_mayor = nombre
print(f"El vendedor con el promedio de ventas más alto es: {vendedor_mayor} con un promedio de {promedio_mayor:.2f}\n")

promedio_mayor_semana = 0
promedio_venta_semana = np.mean(ventas, axis=0)
for i, j in enumerate(semana):
    print(f"promedio de ventas por semana: {j} = {promedio_venta_semana[i]:.2f}")
    if promedio_mayor_semana < promedio_venta_semana[i]:
        promedio_mayor_semana = promedio_venta_semana[i]
        semana_mayor = j
print(f"La semana con el promedio de ventas más alto es: {semana_mayor} con un promedio de {promedio_mayor_semana:.2f}")

venta_mayor = np.max(ventas)
venta_menor = np.min(ventas)
print(f"La venta más baja es: {venta_menor}")
print(f"La venta más alta es: {venta_mayor}")
print(ventas.std())

peordelopeor = np.argmin(promedio_venta_semana)
peor_vendedor = vendedores[peordelopeor]
peor_semana = semana[peordelopeor]
print(peordelopeor)
print(peor_vendedor)
print(peor_semana)


# ejercicio 3 
print("\nEjercicio 3:")

ventas = np.array([
    [120, 150, 100, 130, 170],
    [80,  90,  95,  100, 110],
    [200, 210, 190, 220, 230],
    [50,  60,  55,  65,  70]
])

print(ventas.shape)
dia = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
producto = ["Producto A", "Producto B", "Producto C", "Producto D"]

ventas_totales = np.sum(ventas, axis=1)
for i, p in enumerate(producto):
    print(f"Ventas totales del {p}: {ventas_totales[i]}")
ventas_semanal = np.sum(ventas, axis=0)
for i, d in enumerate(dia):
    print(f"Ventas totales de {d}: {ventas_semanal[i]}")
    
producto_vendido = np.argmax(ventas_totales)
producto_menor = np.argmin(ventas_totales)
producto_peor = producto[producto_menor]
producto_mejor = producto[producto_vendido]
print(f"El producto menos vendido es: {producto_peor}")
print(f"El producto más vendido es: {producto_mejor}")


indice_venta_mayor = np.argmax(ventas)
producto_mayor_venta = np.unravel_index(indice_venta_mayor, ventas.shape)
print(producto_mayor_venta)

         
p = producto_mayor_venta[0]
d = producto_mayor_venta[1]
print(f"La venta más alta corresponde al {producto[p]} el día {dia[d]} y la venta fue de: {np.max(ventas)}")