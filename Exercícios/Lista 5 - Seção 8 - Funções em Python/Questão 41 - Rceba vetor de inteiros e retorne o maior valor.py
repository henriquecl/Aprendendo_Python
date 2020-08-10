"""
Questão 41 - Faça uma função que receba um vetor de inteiros e retorne o maior valor deles
"""
i = []


def maior_numero(numero):
    lista_auxiliar = []
    for num in numero:
        lista_auxiliar.append(num)
    return max(lista_auxiliar)


j = int(input('Digite um número, se quiser parar digite um negativo:  '))
i.append(j)
while j > 0:
    j = int(input('Digite um número, se quiser parar digite um negativo:  '))
    i.append(j)

print(maior_numero(i))
