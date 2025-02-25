import numpy as np 

# Número de simulaciones 
num_simulaciones = 100000

# simular lanzamientos de dados 
lanzamientos = np.random.randint(1, 7, (num_simulaciones, 6))

# Contar cuántas simulaciones tienen al menos un "6"
casos_exitosos = np.sum(np.any(lanzamientos == 6, axis=1))

# Calcular la probabilidad 
probabilidad = casos_exitosos / num_simulaciones

# Mostrar el resultado 
print(f"Probabilidad de obtener al menos un '6' en seis lanzamientos: {probabilidad:.4f}")