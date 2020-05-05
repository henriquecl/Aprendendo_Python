"""
Questão 19 - Faça uma função que retorne o maior fator primo de um número - TILTEI

"""


def maior_fator_primo(numero):
    maior_fator = 0
    num = numero
    while num / 2 == int(num / 2):
        num = numero / 2
        maior_fator = 2
    while num / 3 == int(num / 3):
        num = numero / 3
        maior_fator = 3
    return num


print(maior_fator_primo(6))










