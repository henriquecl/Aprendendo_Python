"""
Questão 26 - Faça uma função que receba um  número inteiro positivo n e calcule o somatório de 1 até n
"""


def somatorio(num):
    soma = 0
    i = 0
    while i <= num:
        soma = soma + i
        i = i + 1
    return soma


print(somatorio(99))