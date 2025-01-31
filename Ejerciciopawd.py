#escribe un programa que pida al usuario una contraseña y la valide el 
#programa debe seguir pidiendo la constraseña hasta que sea correcta
pswd_real="Python" ##Definimos la contraseña del usuario
#Declaramos la variable que guardara la contraseña que el usuario ingrese

pswd_user="" ##Definimos la variable para introducir la contraseña por medio de un input

while pswd_user != pswd_real:   ##validamos a traves de un while que sean iguales las contraseñas
    pswd_user = input("Ingresa contraseña: ") ##Muestra el mensaje para ingresar contraseña
    
    if pswd_user != pswd_real:  ##Valida si las contraseñas coinciden
        print("incorrecto")     ##Señala contraseña incorreta
        
print("contraseña correcta") ##Si la contraseña es correcta inprime la contraseña