"""
Questão 43 - Faça uma função que receba um vetor de inteiros e o preencha com números aleatórios sem repetição
"""
import random


def preencher_vetor_random(num):
    i = 0
    while i <= 100:
        num.append(random.random())
        i = i + 1
    num.sort()
    return num


lista = [1, 2, 3, 4, 5]
print(preencher_vetor_random(lista))
