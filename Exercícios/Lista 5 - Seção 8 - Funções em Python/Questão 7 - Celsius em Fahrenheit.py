"""
Questão 7 - Faça uma função que receba uma temperatura em C e retorne em F
"""


def c_em_f(temperatura):
    f = (temperatura * (9/5))+32
    return f


print(c_em_f(30))
