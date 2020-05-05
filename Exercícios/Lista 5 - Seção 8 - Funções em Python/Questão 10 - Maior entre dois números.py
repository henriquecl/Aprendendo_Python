"""
Questão 10 - Receba dois números e retorne qual o maior dos dois
"""


def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    return 'Iguais'


print(maior_numero(1, 1))
print(maior_numero(1, 2))
print(maior_numero(2, 1))
