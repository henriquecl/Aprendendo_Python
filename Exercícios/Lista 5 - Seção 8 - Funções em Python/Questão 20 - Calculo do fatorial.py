"""
Faça um algoritmo que receba um número inteiro positivo e calcule o fatorial de n.
"""
fatorial = 1


def fatorial_de_um_numero(num):
    global fatorial
    i = num
    while i > 0:
        fatorial = fatorial * i
        i = i - 1
    return fatorial


print(fatorial_de_um_numero(10))
