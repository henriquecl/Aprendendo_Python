"""
Questão 40 - Faça uma função que receba um vetor de inteiros e retorne quantos valores pares ele tem
"""


def valor_par(numeros):
    lista_auxiliar = []
    for num in numeros:
        if num % 2 == 0:
            lista_auxiliar.append(num)
    return f'A list possui {lista_auxiliar} numeros pares e com a quantidade:{len(lista_auxiliar)}'


numeross = [3, 4, 5, 6, 7, 8, 9]

print(valor_par(numeross))

