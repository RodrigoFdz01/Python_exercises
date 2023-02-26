# number = 1
# contador = 0
# while contador < 10:
#     contador += 1
#     print(contador)
#     if contador == 5:
#         break



# ingresar numeros hasta completar todos los match del array lista
# current_numbers = []
# lista = "123"
# total_len = len(lista)
# count = 0
# while len(lista) > len(current_numbers):

#     user_number = input("ingresa un numero: ") # es un str

#     if lista.find(user_number) != -1:
#         current_numbers.append(user_number)
#         print("si, correcto!!!")
#         print(current_numbers)
#     else:
#         print("no esta !!!")

# count += 1
# print("igualaste la extension")

'''

Debes crear una funcion llamada `sumattion` que reciba un numero como parametro y
que devuelva la sumatoria de todos sus numeros anteriores, incluso ese mismo.
Ejemplo:
- sumattion(3) debe retornar 6 porque hace (1+2+3)
- sumattion(8) debe retornar 36  

'''
# def sumattion():
#    number = int(input("ingresa un numero > a 0: "))
#    summation = 0
#    limit = number + 1
#    for i in range(1,limit):
    #    summation = summation + i
#    print(summation) 

# sumattion()



'''
Crea una aplicacion q obtenga los elementos impares de una lista pasada por parametro con filter
y realice una suma de esos datos obtenidos mediante reduce
'''

#### filter

#lista_de_numeros= [1,2,3,4,5,6]
#impares = list(filter(lambda el : el % 2 != 0 , lista_de_numeros))
#print(impares)
#
#
#from functools import reduce
#suma = reduce(lambda a, b : a + b, impares)
#print(suma)

'''
Implementar la clase Libro q tenga info de su autor, titulo del libro, 
genero  cantidad de paginas.
INcluir todos los comandos de consulta y modificacion de atributos(los get y set)
Implementar los metedos equals, copy y clone.
MOstrar ejemplos de uso de cada uno para verifcar el funcionamiento
'''

#class Libro:
#    def __init__(self,autor=None,titulo=None,genero=None,paginas=None):
#        self.autor = autor
#        self.titulo = titulo
#        self.genero = genero
#        self.paginas =  paginas
#
#    def get_autor(self):
#        return self.autor
#
#    def get_titulo(self):
#        return self.titulo
#
#    def get_genero(self):
#        return self.genero
#
#    def get_paginas(self):
#        return self.paginas
#
#    ####
#    def set_autor(self,autor):
#        self.autor = autor
#
#    def settitulo(self,titulo):
#        self.titulo =titulo
#
#    def set_genero(self,genero):
#        self.genero = genero
#
#    def set_paginas(self,paginas):
#        self.paginas = paginas
#
#
#    def clone(self):
#        return Libro(self.autor,self.titulo,self.genero,self.paginas)
#
#    
#    def copy(self):
#        return self
#
#    def equals(self, objeto):
#        return True if self is objeto else False
#
#
#libro1 = Libro("Juan", "El resplandor", "Terror","1501")
#print(libro1)
#
#libro_clone = libro1.clone()
##print(libro_clone)
#
#libro_copia = libro1.copy()
##print(libro_copia)
#
## metodo equals , chequea si un obj es el mismo
#print(libro1.equals(libro_clone))
#print(libro1.equals(libro_copia))



'''
Replace the first two occurrences of a white-space character with the digit 9:
'''
#????

'''
find a expression in a str
'''
# import re
# txt = "The rain in Spain"
# word = "rains"

# if re.search(word ,txt) is not None:
#     print("encontro")
# else:
#     print("NO LO ENCONTRO")


'''
loop in both list, find and append the match
'''

# a= [1,2,3]

# b = [4,5,6]
# new_arr = []

# def super_func(a,b):
#     for i in a:
#         for j in b:
#             if i == j:
#                 new_arr.append(i)
#     return new_arr
# print(super_func(a,b))


