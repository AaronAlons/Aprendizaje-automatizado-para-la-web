import time #importamos la libreria para el reloj

while True: #le damos la varable true
    tiempo = time.strftime("%H:%M:%S")  # Obtener la hora actual
    print(f"\rHora actual: {tiempo}", end="", flush=True)  # Imprimir en la misma línea
    time.sleep(1)  # Esperar un segundo antes de actualizar