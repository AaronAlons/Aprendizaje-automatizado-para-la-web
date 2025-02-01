#escribe un programa que pida al usuario una contraseña y la valide el 
#programa debe seguir pidiendo la constraseña hasta que sea correcta
escribirContraseña = 5
for i in range(escribirContraseña):
    contraseña = input("Ingresa contraseña: ")
    if contraseña == 'Hola mundo':
        print("Gracias, bienvenido")
        break
    print('Incorrecto.  %d intentos restantes' % (escribirContraseña-i-1))