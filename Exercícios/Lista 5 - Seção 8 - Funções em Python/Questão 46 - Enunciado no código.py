"""
Questão 46 - Crie um programa contendo aS seguinteS funções que recebem o mesmo vetor V.

Impressão do vetor
Impresso inversa
Média aritmética dos elementos do vetor
"""


def imprimir_vetor(v1):
    return print(v1)


def inverter_vetor(v2):
    v2.reverse()
    return print(v2)


def media_vetor(v3):
    return print(sum(v3)/len(v3))


v = [1, 2, 3, 4, 5]
imprimir_vetor(v)
inverter_vetor(v)
media_vetor(v)
