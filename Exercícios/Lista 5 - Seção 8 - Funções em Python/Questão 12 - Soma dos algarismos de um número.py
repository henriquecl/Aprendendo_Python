"""
Questão 12 - Escreva um uma função que receba um número inteiro maior que zero e retorne a soma dos seus algarismos
"""


def soma_dos_algarismos(numero1):
    return sum(int(i) for i in numero1)


print(soma_dos_algarismos('398'))

