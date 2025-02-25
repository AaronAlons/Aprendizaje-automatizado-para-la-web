import numpy as np 

# Definir el conjunto de datos 
datos = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])

# Calcular la media, mediana y desviación estándar 
media = np.mean(datos)
mediana = np.median(datos)
desviacion = np.std(datos)

# Mostrar los resultados 
print(f"Media = {media:.2f}")
print(f"Mediana = {mediana}")
print(f"Desviación estándar = {desviacion:.2f}")