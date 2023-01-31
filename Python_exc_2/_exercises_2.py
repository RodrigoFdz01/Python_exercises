
######  Ejercicio  #####
'''
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() 
del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números.
 Supongamos que tenemos mas de 3 números o no sabemos cuantos números son.
  Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
'''

def max_in_list(list):
    list = (1,2,322,4,35,46)
    return max(list)

print(max_in_list(list))
## 2da opcion
def max_in_list(lista):
    inicio = 0
    for i in lista:
      if i > inicio:
        inicio = i
    return inicio
print(max_in_list([1,2,322,4,35,46]))


######  Ejercicio 2 #####
'''
Escribir una función mas_larga() que tome una lista de palabras
y devuelva la mas larga.
'''

def mas_larga(lista):
  mas_larga2=""
  for i in lista:
    if len(i) > len(mas_larga2):
      mas_larga2 = i
  return mas_larga2 

print(mas_larga(["hola","si", "casiessdfg","function"])) 

######  Ejercicio 3 #####
'''
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
 y devuelva las palabras que tengan mas de n caracteres.
'''

def filtrar_palabras(lista, number):
  for i in lista:
    if len(i) > number:
      print(i)
print(filtrar_palabras(["hola","si", "palabras","function"],5))

######  Ejercicio 4  ######
'''
Escribir un programa que le diga al usuario que ingrese una cadena. 
El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
'''

from itertools import count

def c_mayusculas():
  word = input("ingresa una palabra...")
  con = 0
  for i in word:
    if i == i.upper():
      con += 1
  print(con)

print(c_mayusculas())       

###  Ejercicio 5  ???????
'''
Construir un pequeño programa que convierta números binarios en enteros.
'''
def aDecimal(numeroBin):
    numeroBin = str(numeroBin)
    decimal = 0
    exp = len (numeroBin) -1
    for i in numeroBin:
        decimal += (int(i) * 2**(exp))
        exp = exp - 1
    return decimal

print(aDecimal(101)) 

######  Ejercicio 6 #####
'''
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
'''
def program():
  year = input("ingresa año en curso...")
  for i in range(3):
    name = input("Ingresa el nombre...")
    birth_year = input("year of birth..")
    print(f'{name}, cumple {int(year)-int(birth_year)} años, en el {year}')

print(program())

     ######  Ejercicio 7 #####
'''
Definir una tupla con 8 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
'''     

def ages_over_20(lista):
  counter = 0
  for i in lista:
    if i > 20:
      counter += 1
  print('Hay '+ str(counter) + ' personas sobre 20') 

print(ages_over_20((21,11,45,23,17,17,22,19)))

      ######  Ejercicio 8 #####
'''
Definir una lista con un conjunto de nombres, imprimir la cantidad q comienzan 
con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
      '''

def main():
    x = input ("Cuantos nombres quieres ingresar?: ")
    option = str(input("ingresa la primera letra a buscar en la lista..."))
    counter = 0
    lista = []
    for i in range(int(x)):
        a = input("Ingresa el nombre: ")
        lista.append (a)
    for i in lista:
      if i[0] == option.lower() or i[0] == option.upper():
        counter +=1
    print(counter)

print(main())    


    #### Ejercicio 9  #####
'''
Crear una función contar_vocales(), que reciba una palabra y
 cuente cuantas letras "a" tiene,
 cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
'''

def contar_vocales():
  word = input("ingresa una palabra: ")
  word = word.lower()
  vocals = "aeiou"
  contador = 0
  for i in vocals:
    for j in word:
      if i == j:
        contador += 1
  print(contador)
print(contar_vocales())


 ##### Ejercicio 10 ####
'''
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
'''

def es_bisiesto():
    print ("Comprueba años bisiestos:   ")
    a = input ("Escriba un año y le dire si es bisiesto: ")
    a = int(a)
    if a % 4 == 0 and (a % 100 != 0):
        print ("El año " + str(a) + " es un año bisiesto porque es multiplo de 4")
    elif a % 400 == 0:
        print ("El año " +str(a)+" es un año bisiesto porque es multiplo de 400")
    else:
        print ("El año " +str(a)+ " no es bisiesto")

print(es_bisiesto())
