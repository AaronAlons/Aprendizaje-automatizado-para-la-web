#Realiza el codigo para la elaboracion de un sandwich
#ingredientes pan crema, jitomate, jamon, queso, queso de puerco, lechuga y picante.

#Declaramos nuesta pila
sandwich = []
#Declaramos las variables que guardaran los ingredientes
sandwich.append("Pan_inferior")
sandwich.append("Crema")
sandwich.append("Jamon")
sandwich.append("Lechuga")
sandwich.append("Rodaja_de_jitomate")
sandwich.append("Picante")
sandwich.append("Queso_de_puerco")
sandwich.append("Queso")
sandwich.append("Pan_superior")

#Imprimimos los ingredientes
print("Sandwich:")
while sandwich:
    action = sandwich.pop()
    print(f"- {action}")
