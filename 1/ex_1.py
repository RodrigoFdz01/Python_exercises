'''
 
1- si es Palindromo...
'''

#def Palindromo(word):
#     word = word.lower()
#     return word == word[::-1]
#
#print(Palindromo("neuquen"))
#
#print(Palindromo("pampa"))


'''
2. Loop de pares
Debes crear una funcion llamada loopDePares que reciba como parametro un numero 
y haga un loop de 0 a 50 mostrando en la consola cada numero del loop.
En caso de que el numero de la iteracion, sumado con el numero pasado por parametro, sea par,
 mostra en la consola “El numero x es par”. 
'''

def Loop(number):
      start = 0
      end = 20
      while start <= end:
         suma = start + number
         result =  print(" El numero es par" if suma % 2 == 0 else start )
         start += 1
       
Loop(2)

'''
3- Sumatoria de todos sus numeros anteriores

 Debes crear una funcion llamada `sumattion` que reciba un numero como parametro y
que devuelva la sumatoria de todos sus numeros anteriores, incluso ese mismo.
Ejemplo:
- sumattion(3) debe retornar 6 porque hace (1+2+3)
- sumattion(8) debe retornar 36   
'''

def sumattion(number):
    summation = 0
    limit = number +1
    for i in range(1,limit):
        summation = summation + i
    print(summation) 

sumattion(3)
'''
4.Imprimir Todos los numeros 
'''

def todos_losnumeros(number):
    count = 1
    while count <= number:
        print(count)
        count = count +1
todos_losnumeros(12)     

'''
5 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
 (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos
  es un muy buen ejercicio.
'''
def max(number,number2):
    result = number if number > number2 else number2
    print(result)

max(122,15)

'''
6- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva
 el mayor de ellos.
'''

def max(number,number2, number3):
    result = number if number > number2 else number2
    result2 = result if result > number3 else number3
    print(result2)

max(12,150, 100)

'''
7- Definir una función que calcule la longitud de una lista o una cadena dada.(Es cierto que
 python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy 
 buen ejercicio.
'''

def long_chain(list):
    cont = 0
    for i in list:
        cont += 1
    print(cont)

long_chain([1,2,3,4,5])

'''
8- Escribir una función que tome un carácter y devuelva True si es una vocal, 
de lo contrario devuelve False.
'''

def es_vocal(x):
    s = "aeiou"
    if s.find(x) == -1:
        print("No!")
    else:
        print("yes!")

es_vocal("a")

'''
9- Escribir una función sum() y una función multip() que sumen y multipliquen 
respectivamente todos los números de una lista.
 Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) 
 debería devolver 24.
'''

def suma(x):
    suma = 0
    for i in x:
        suma += i
    print (suma) 

suma([1,2,3,4])
#------------------
def mult(el):
    suma = 1
    for i in el:
        suma *= i
    print (suma) 

mult([1,2,3,2])

'''
10- Definir una función inversa() que calcule la inversión de una cadena.
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
'''

def inverse(param):
    reversed_word = param[::-1]
    print(reversed_word)
inverse("estoy probando")    

'''
11- Definir una función superposicion() que tome dos listas y devuelva True
 si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
 Escribir la función usando el bucle for anidado.
'''

def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False           
                
print(superposicion([1,20,30,4],[5,6,7,8,20]))

'''
12- Definir una función generar_n_caracteres() que tome un entero n y 
devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") 
debería devolver "xxxxx".
'''

def create_n_characs(number, str):
    print (number * str)
create_n_characs(3,"x")



