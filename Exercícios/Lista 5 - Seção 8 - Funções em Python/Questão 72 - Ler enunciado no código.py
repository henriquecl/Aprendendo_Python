"""
Questão 72 - Para representar um vetor no R³, implemente uma função que calcule a soma de dois vetores.
"""


def soma_de_vetor(v1, v2):
    resultado = []
    if len(v1) != len(v2):
        return 'Não é possivel somar esses dois vetores'
    for i in range(len(v1)):
        resultado.append(v1[i] + v2[i])
    return resultado


print(soma_de_vetor([1, 1, 1], [1, 1, 1]))
