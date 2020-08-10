"""
Questão 28 - Faça uma função que receba como parâmetro o valor de um ângulo em GRAUS e calcule o valor do cosseno desse
angulo usando sua respectiva série de Taylor
"""
import math

fatorial1 = 1


def fat(num):
    global fatorial1
    i = num
    while i > 0:
        fatorial1 = fatorial1 * i
        i = i - 1
    return fatorial1


def cosseno(angulo_em_grau):
    angulod = angulo_em_grau * (math.pi / 180)
    cos = 1 - (angulod ** 2)/fat(2) + (angulod ** 4)/fat(4) - (angulod**6)/fat(6) + (angulod**8)/fat(8)
    return cos


print(cosseno(0))
