"""
Questão 9 - Leia uma matriz de 3x3. Calcule a soma dos elementos que estão abaixo da diagonal principal
"""

matrix = [[1, 2, 3], [789, 19, 19], [1891, 1, 1]]
num = 0
for i in range(3):
    for j in range(3):
        if j < i:
            num = matrix[i][j] + num

print(num)
