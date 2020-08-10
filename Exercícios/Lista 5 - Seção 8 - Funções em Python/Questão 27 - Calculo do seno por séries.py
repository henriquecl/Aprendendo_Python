"""
Questão 27 - Calculado do seno pela série de taylor (dada na questão)

"""
import math
fatorial1 = 1


def fatorial(num):
    global fatorial1
    i = num
    while i > 0:
        fatorial1 = fatorial1 * i
        i = i - 1
    return fatorial1


def seno_do_angulo(valor):
    valorad = valor * (math.pi / 180)
    seno = valorad - (valorad**3)/fatorial(3) + (valorad**5)/fatorial(5) - (valorad**7)/fatorial(7)+(valorad**9)/fatorial(9)

    return seno


print(seno_do_angulo(90))
