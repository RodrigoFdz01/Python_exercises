# number = 1
# contador = 0
# while contador < 10:
#     contador += 1
#     print(contador)
#     if contador == 5:
#         break
'''
current_numbers = []
lista = "123"
total_len = len(lista)
count = 0
while len(lista) > len(current_numbers):

    user_number = input("ingresa un numero: ") # es un str

    if lista.find(user_number) != -1:
        current_numbers.append(user_number)
        print("si")
        print(current_numbers)
    else:
        print("no esta !!!")

count += 1
print("igualaste la extension")


###   Debes crear una funcion llamada `sumattion` que reciba un numero como parametro y
que devuelva la sumatoria de todos sus numeros anteriores, incluso ese mismo.
Ejemplo:
- sumattion(3) debe retornar 6 porque hace (1+2+3)
- sumattion(8) debe retornar 36  



def sumattion(number):
    summation = 0
    limit = number +1
    for i in range(1,limit):
        summation = summation + i
    print(summation) 

sumattion(4)
'''


'''
Crea una aplicacion qu obtenga los elementos impares de inalista pasada por parametro con filter
y realice una suma de esos datos obtenidos mediante reduce

'''

lista_de_numeros= [1,2,3,4,5,6]

# filter

impares = list(filter(lambda el : el % 2 != 0 , lista_de_numeros))
print(impares)


from functools import reduce
suma = reduce(lambda a, b : a + b, impares)
print(suma)