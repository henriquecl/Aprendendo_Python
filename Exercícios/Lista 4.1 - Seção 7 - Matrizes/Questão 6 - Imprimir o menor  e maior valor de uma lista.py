"""
Questão 6 - Leia duas matrizes 4x4 e escreva uma terceira com os maiores valores de cada posição das matrizes lidas
"""
matrix1 = [[1, 2, 3, 8], [789, 19, 19, 19], [1891, 1, 987, 1], [1, 1, 53, 65]]
matrix2 = [[9, 8, 7, 0], [789, 19, 19, 19], [1891, 1, 1, 1], [1891, 5, 9, 8]]
matrix3 = [[], [], [], []]

for i in range(4):
    for j in range(4):
        if matrix1[i][j] >= matrix2[i][j]:
            numero = matrix1[i][j]
            matrix3[i].append(numero)
        else:
            numero = matrix2[i][j]
            matrix3[i].append(numero)

for i2 in range(len(matrix3)):
    print(f'{matrix3[i2]}')

