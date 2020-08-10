"""
Questão 44 - Faça uma função que receba como parâmetro um vetor X de 30 elemetentos inteiros e retorne, tambêm por para-
metro dois vatores A e B. O vetor A deve conter os elementos pares de X e o vetor B os elementos impares.
"""


def separar_pares_impares(x, a=[], b=[]):
    for numero in x:
        if numero % 2 == 0:
            a.append(numero)
        else:
            b.append(numero)

    return a, b


lista = list(range(11))
print(separar_pares_impares(lista))

