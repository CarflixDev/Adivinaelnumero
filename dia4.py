# Programa Dia 4
# CarReel
# Fecha: 16/02/2024

from random import randint

# Declaracion de las variable del numero elegido por la cpu con valor inicial 0
numero_cpu = 0
# Declaracion de la variable del numero de la cpu aleatorio
numero_cpu = randint(1, 100)

# Declaracion de la variable que solicita un nombre al jugador
nombre = input("Dime tu nombre: ")
# Funcion que imprime el nombre del usuario por pantalla y le realiza la pregunta del numero secreto.
print(f"Bueno {nombre},he pensado un numero entre 1-100\nTienes 8 oportunidades para adivinarlo: ")

# Creacion del contador del bucle con el numero de intentos = 0 hasta 8
intentos = 0
while intentos < 8:
    numero_usuario = int(input("Cual es el numero?: "))
    intentos += 1
    # Creamos las condiciones con If para el primer caso
    ###Si el usuario elige un numero mas alto que la cpu indica que mi numero es mas alto"""
    if numero_usuario < numero_cpu:
        print(f"Mi numero es mas alto")
    ###Si el usuario elige un numero mas bajo que la cpu indica que mi numero es mas alto"""
    elif numero_usuario > numero_cpu:
        print(f"Mi numero es mas bajo")
    ###Si el usuario adivina el numero que la cpu indica has ganado"""
    else:
        print(f"Felicidades {nombre}! has adivinado en {intentos} intentos")
        break
###Si el usuario ha realizado los 8 intentos pierde"""
if numero_usuario != numero_cpu:
    print("Lo siento se han agotado los intentos")
