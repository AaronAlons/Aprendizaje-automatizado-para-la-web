import turtle  # Importamos la biblioteca turtle para dibujar
import math    # Importamos la biblioteca math para funciones matemáticas

# Configuración de la tortuga
t = turtle.Turtle()  # Creamos un objeto tortuga
t.speed(0)           # Establecemos la velocidad máxima
t.color("green")       # Color rojo para el dibujo
turtle.bgcolor("black")  # Fondo negro

# Función para calcular los puntos de la figura con ecuaciones matemáticas
def corazon(n):
    x = 16 * math.sin(n) ** 3  # Cálculo de la coordenada x
    y = 13 * math.cos(n) - 5 * \
        math.cos(2 * n) - 2 * math.cos(3 * n) - \
        math.cos(4 * n)  # Cálculo de la coordenada y
    return x, y  # Retorna las coordenadas x e y

# Movimiento inicial de la tortuga
t.penup()  # Levanta el lápiz para mover sin dibujar

# Bucle para dibujar múltiples capas del corazón
for i in range(15):  # Se repite 15 veces para crear el efecto de expansión
    t.goto(0, 0)  # La tortuga regresa al centro
    t.pendown()  # Baja el lápiz para empezar a dibujar
    
    for n in range(0, 100, 2):  # Recorre valores para formar la curva del corazón
        x, y = corazon(n / 10)  # Obtiene coordenadas del corazón
        t.goto(x * i, y * i)  # Dibuja el punto escalado
    
    t.penup()  # Levanta el lápiz para evitar líneas adicionales

# Oculta la tortuga después de dibujar
t.hideturtle()

# Mantiene la ventana abierta
turtle.done()