"""
Questão 17 - Faça uma função que receba dois números inteiros positivos por parametro e retorna a soma dos N números
inteiros existentes entre eles
"""


def soma_dos_inteiros(num1, num2):
    soma = 0
    i = num1 + 1
    while i != num2:
        soma = soma + i
        i = i + 1
    return soma


print(soma_dos_inteiros(3, 999999))

