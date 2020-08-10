"""
Questão 3 - Faça um programa que preenche uma matriz 4x4 com o produto do valor da linha e da coluna de cada elemento.
Em seguida, imprima a matriz
"""

matrix = [[], [], [], []]

for i in range(4):
    for j in range(4):
        numero = i * j
        matrix[i].append(numero)

for i in range(len(matrix)):
    if i == 0:
        print('A matriz digitada foi:')
    print(matrix[i])
