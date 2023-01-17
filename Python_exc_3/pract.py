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


'''
def sumattion(number):
    summation = 0
    limit = number +1
    for i in range(1,limit):
        summation = summation + i
    print(summation) 

sumattion(4)


