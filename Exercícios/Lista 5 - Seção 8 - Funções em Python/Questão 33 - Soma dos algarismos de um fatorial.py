"""
Questão 33 - Faça uma função que receba um número N e retorne a soma dos algarismos de N! Ex: Se N=4, N!=24 logo a soma
de seus algarismos é 2+4 = 6
"""
fatorial = 1


def fatorial_de_um_numero(num):
    global fatorial
    i = num
    while i > 0:
        fatorial = fatorial * i
        i = i - 1
    return fatorial


def soma_dos_algarismos(numero):
    num2 = str(numero)
    return sum(int(i) for i in num2)


print(soma_dos_algarismos(fatorial_de_um_numero(5)))





