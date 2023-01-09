######  Ejercicio 1 #####

'''
El programa debe pedir la longitud de la cadena (de 2
a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la
cadena de números. En cada intento, el programa informará de cuántos números
han sido acertados
EJE: 

Dime la longitud de la cadena: 4
Intenta adivinar la cadena: 1234
Con 1234 has adivinado 1 valores. Intenta adivinar
la cadena: 1243
Con 1243 has adivinado 0 valores. Intenta adivinar
la cadena: 1432
Con 1432 has adivinado 2 valores. Intenta adivinar
la cadena: 2431
Con 2431 has adivinado 4 valores.
Felicidades

'''
import random

#largo_cadena = int(input("Dime la extension de la cadena..."))

# def num_aleat():
#     numero_aleatorio = ""
#     for i in range(largo_cadena):
#         x = random.randint(0, 9)
#         x = str(x)
#         numero_aleatorio += x
#     return numero_aleatorio
# print(num_aleat())

# def num_aleat():
#     numero_aleatorio = ""
#     for i in range(largo_cadena):
#         x = random.randint(0, 9)
#         x = str(x)
#         numero_aleatorio += x
#     print(numero_aleatorio)    
#     number_guess = str(int(input("Intenta adivinar la cadena, ingresa de a un numero a la vez...")))
#     current_number = ""
#     if numero_aleatorio.find(number_guess[0]):
#         current_number.join(number_guess)
#         print(f'Adivinaste!! {number_guess}, esta en el numero, continua...')
#     else:
#         print("NO adivinaste")
# print(num_aleat())


### otra solucion de numeros de 1 digito

num = random.randint(1, 10)
guess = ""

while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")