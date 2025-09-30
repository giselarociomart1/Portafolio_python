
# 📊 Desafío 3 - Tipos y Estructuras de Datos (Parte I)

Este desafío se centra en la aplicación práctica de las estructuras de datos nativas de Python (**Listas** y **Diccionarios**) y en la introducción a la librería **NumPy** para el análisis estadístico de datos, un componente clave del Control Estadístico de Procesos (CEP).

---

## 🚀 Actividades Desarrolladas

### Actividad 1: Manipulación de Listas y Diccionarios

Se aplicaron diversas operaciones fundamentales para demostrar el manejo de las estructuras de datos:

* **Manipulación de Listas:** Se realizaron operaciones como la indexación, el *slicing*, eliminación de elementos, adición de nuevos elementos y ordenamiento alfabético.
* **Creación de Diccionarios:** Se utilizó la función `zip()` junto con `dict()` para crear un diccionario a partir de dos listas, estableciendo una relación directa entre una lista de números ordinales (llaves) y la lista de valores.

---

### Actividad 2: Control Estadístico de Procesos (CEP) con NumPy

Se utilizó la librería **NumPy** para realizar un análisis estadístico de datos relacionados con la fabricación de cerveza artesanal, específicamente el contenido de alcohol.

El objetivo fue determinar si el proceso se encuentra bajo control, calculando los Límites de Control Superior e Inferior (LSC y LIC), que definen el rango esperado para la mayoría de los datos.

* **Cálculos Estadísticos:** Se calcularon la **media** (`np.mean`) y la **desviación estándar** (`np.std`) del conjunto de datos.
* **Cálculo de Límites de Control:** Se implementaron las fórmulas de CEP:
    * **LIC:** $\text{Media} - 3 \times \text{Desviación Estándar}$
    * **LSC:** $\text{Media} + 3 \times \text{Desviación Estándar}$
* **Filtro de Valores Atípicos:** Se aplicó un filtro lógico (`np.logical_or`) para identificar y aislar los valores que caen **fuera de los límites de control**, señalando posibles anomalías en el proceso.

---

## 🛠️ Tecnologías y Librerías

* **Lenguaje de programación:** Python 3
* **Entorno de desarrollo:** Jupyter Notebook
* **Librerías:** **NumPy** (`import numpy as np`) para manejo eficiente de arrays y cálculos estadísticos.
