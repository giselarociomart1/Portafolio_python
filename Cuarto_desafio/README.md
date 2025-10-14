# 🧑‍🚀 Cuarto Desafío - Tipos y Estructuras de Datos (Parte II)

Este desafío forma parte de mi curso de **Data Science**, en el cual continúo desarrollando habilidades en análisis y manipulación de datos utilizando Python y la librería **pandas**.

## 📘 Descripción

El objetivo del desafío es trabajar con un conjunto de datos de **postulantes a astronautas**, evaluando sus condiciones físicas y de rendimiento mediante cálculos y filtrados sobre un DataFrame.  
El enfoque principal está en aplicar transformaciones, crear nuevas columnas y exportar los resultados en un formato adecuado para su análisis posterior.

## 🎯 Objetivos del Desafío

1. Crear un **DataFrame** a partir del archivo `resumen_resultados_astronautas.csv`.  
2. Calcular el **IMC (Índice de Masa Corporal)** de cada astronauta utilizando la fórmula:  
   \[
   IMC = \frac{m}{h^2}
   \]
   donde `m` es el peso (kg) y `h` la altura (m).  
3. Calcular el **promedio de evaluaciones** de cada postulante.  
4. Filtrar los candidatos que:
   - Tengan un IMC entre **18.5 y 24.9**.  
   - Obtengan un **promedio de evaluaciones mayor o igual a 87**.  
5. Reiniciar el índice del DataFrame filtrado.  
6. Modificar la columna `"califica"` para que indique `"Sí"` en los candidatos seleccionados.  
7. Exportar el DataFrame final a un archivo **`astronautas_calificados.csv`**.

## 🧰 Tecnologías Utilizadas

- **Python 3**
- **pandas**
- **Jupyter Notebook**

## 📊 Resultados

El resultado final es un archivo CSV con los astronautas que cumplen con los criterios establecidos.  
Este ejercicio permitió aplicar conocimientos sobre:
- Creación y manipulación de DataFrames.  
- Operaciones con columnas.  
- Filtros condicionales.  
- Exportación de datos.

## 💡 Aprendizajes

Durante este desafío consolidé el uso de **pandas** para el análisis de datos, comprendiendo mejor cómo:
- Calcular métricas derivadas a partir de datos existentes.  
- Aplicar condiciones lógicas para filtrar información.  
- Exportar resultados limpios y listos para uso posterior.  

---

📁 **Archivo principal:** `Cuarto_Desafío-Gisela_martinez.ipynb`  
📄 **Datos utilizados:** `resumen_resultados_astronautas.csv`

---

