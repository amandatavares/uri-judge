#Pegando os números do teclado
entrada = input().split()
#Transformando eles em inteiro
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

#Colocando todos em uma lista
lista = [a,b,c]

#Ordenando a lista
lista.sort()

#Mostrando os numeros ordenados
print(lista[0])
print(lista[1])
print(lista[2])
print("")

#Mostrando os números como foram digitados
print(a)
print(b)
print(c)
