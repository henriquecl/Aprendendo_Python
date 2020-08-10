"""
Questão 14 - Faça um programa para gerar automaticamente número entre 0 e 99 de uma cartela de bingo. Sabendo que cada
cartela deve conter 5 linhas de 5 numeros, gere estes dados de modo a não ter números repetidos dentro das cartelas.
"""
from random import randint
cartela = [[], [], [], [], []]
lista_auxiliar = []
lista_auxiliar_2 = []
#lista.append(randint(0, 99))

for i in range(5):
    for j in range(5):
        numero = randint(0, 99)
        lista_auxiliar.append(numero)
        if lista_auxiliar.count(numero) <= 1:
            cartela[i].append(numero)
        elif lista_auxiliar.count(numero) >= 1:
            numero = randint(0, 99)
            lista_auxiliar.append(numero)
            lista_auxiliar.count(numero) <= 1
            cartela[i].append(numero)
        elif lista_auxiliar.count(numero) >= 1:
            numero = randint(0, 99)
            lista_auxiliar.append(numero)
            lista_auxiliar.count(numero) <= 1
            cartela[i].append(numero)
        elif lista_auxiliar.count(numero) >= 1:
            numero = randint(0, 99)
            lista_auxiliar.append(numero)
            lista_auxiliar.count(numero) <= 1
            cartela[i].append(numero)
        elif lista_auxiliar.count(numero) >= 1:
            numero = randint(0, 99)
            lista_auxiliar.append(numero)
            lista_auxiliar.count(numero) <= 1
            cartela[i].append(numero)

for i in range(5):
    print(cartela[i])
lista_auxiliar.sort()
print(lista_auxiliar)

