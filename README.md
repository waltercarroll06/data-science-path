# 📊 Data Science Path - Mi Camino de Aprendizaje

## 🎯 Propósito

Este repositorio documenta **mi viaje de aprendizaje en Data Science**. Aquí muestro **día a día** lo que voy aprendiendo, los conceptos que exploro y las habilidades que voy desarrollando. Este es un camino de crecimiento continuo hacia lo que quiero lograr.

## 📅 Registro de Aprendizaje

### Día 1 - Repaso de POO
- Creé una clase `Experimiento` con atributos `name` y `mediciones`
- Métodos: `Promedio()` y `Describir()` 
- Ejercicio: calcular promedio de 5 mediciones

### Día 2 - Bases de NumPy
- **shape**: obtener dimensiones de arrays
- **mean()**: calcular promedio por axis (filas o columnas)
- **argmax() / argmin()**: índice del valor máximo/mínimo
- **max() / min()**: valor mayor/menor
- **std()**: desviación estándar
- **sum()**: suma de elementos
- **unravel_index()**: convertir índice lineal a coordenadas multidimensionales
- 3 ejercicios: notas estudiantes, ventas vendedores, ventas por producto

### Día 3 - 🆕 Pandas: DataFrames y Análisis de Datos

#### Comparación: Día 1 → Día 3
| Aspecto | Día 1 | Día 3 |
|--------|-------|-------|
| **Complejidad de clases** | Clases simples (1-2 métodos) | Clases integradas con DataFrames |
| **Manejo de datos** | Listas simples | DataFrames con índices y columnas nombrados |
| **Filtrado** | Loops manually | Filtrado con condiciones: `df[df["col"] > valor]` |
| **Cálculos** | sum() / len() manual | `.mean()`, `.sum()`, `.idxmax()` integrados |
| **Visualización** | Print simple | DataFrames formateados automáticamente |

#### Lo Nuevo en Pandas (Día 3)
- **¿Qué es un DataFrame?**: Tabla de Excel dentro de Python con filas, columnas y nombres
- **Crear DataFrames**: Desde arrays de NumPy con `pd.DataFrame(data, index=..., columns=...)`
- **Acceso a datos**:
  - `df["columna"]` - acceder a columna
  - `df.loc[índice]` - acceder a fila por nombre
  - `df.loc[fila, columna]` - acceder a celda específica
  - `df.iloc[posición]` - acceder por posición numérica
- **Métodos clave**:
  - `.mean()` / `.sum()` / `.max()` - cálculos por filas (axis=1) o columnas (axis=0)
  - `.idxmax()` / `.idxmin()` - encontrar índice del máximo/mínimo
  - `.argmin()` - posición del mínimo
  - Filtrado: `df[df["columna"] > valor]`
  - `.shape` - dimensiones del DataFrame
- **Agregar columnas**: 
  - Directamente: `df["nueva_col"] = valores`
  - Condicional: `df["estado"] = np.where(condición, "valor1", "valor2")`
- **Ejercicios realizados**:
  1. Análisis de salarios por mes (promedios, filtrados)
  2. Análisis de ventas de productos (totales, promedios, clasificación "estrella")
  3. Análisis de temperaturas por ciudades (máximas, promedios)
  4. Clase `Artistas` → conversión a DataFrame → filtrado por ranking

#### 🎯 Crecimiento Observado
- De usar **loops y operaciones manuales** (Día 1-2) a **métodos automáticos de análisis** (Día 3)
- De **arrays simples** a **estructuras nombradas** que facilitan la interpretación
- Inicio de **análisis real de datos** con filtrado, aggregación y clasificación

---

## 📚 Temas en Exploración

- Fundamentos de Python para Data Science
- Librerías principales: NumPy, Pandas, Matplotlib, Scikit-learn
- Análisis exploratorio de datos (EDA)
- Visualización de datos
- Machine Learning básico

## 🛠️ Herramientas

- Python 3.x
- Jupyter Notebooks
- Git & GitHub

## 📌 Notas

Este repositorio es un registro vivo de mi aprendizaje. Cada día agregará nuevos insights, ejercicios y descubrimientos. El objetivo es documentar el proceso de transformación de principiante a profesional en Data Science.
