"""
Questão 12 - Imprima a transposta de uma matriz 3x3
"""

matrix = [[1, 2, 3], [789, 19, 19], [1891, 1, 1]]
matrix_transposta = [[], [], []]

for j in range(3):
    for i in range(3):
        numero = matrix[j][i]
        matrix_transposta[i].append(numero)

for i in range(3):
    print(matrix_transposta[i])
