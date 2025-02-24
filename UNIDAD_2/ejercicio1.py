import numpy as np

# Definir la matriz de coeficientes 
A = np.array([[2,1],[3,2]])

# Definir el vector de términos independientes
B = np.array([5,8])

# Reolver el sistema de ecuaciones
X = np.linalg.solve(A, B)

# Imprimir los resultados con dos decimales
print(f"Solución del sistema: X = {X[0]:.2f}, Y = {X[1]:.2F}")