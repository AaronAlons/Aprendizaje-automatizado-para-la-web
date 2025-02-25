import sympy as sp

# Definir la variable simbólica
x = sp.Symbol('x')

# Definir la función 
f = x*3 - 4*x*2 +6*x - 2

# Calcular la derivada 
f_derivada = sp.diff(f, x)

# Evaluar la derivada en x=2
valor_derivada = f_derivada.subs(x, 2)

# Mostrar los resultados 
print("Derivada de la función:", f_derivada)
print(f"Valor de la derivada en x=2: {valor_derivada}")