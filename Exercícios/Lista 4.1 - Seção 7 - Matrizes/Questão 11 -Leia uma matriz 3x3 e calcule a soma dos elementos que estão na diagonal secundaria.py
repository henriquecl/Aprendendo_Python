"""
Questão 11 - Leia uma matriz 3x3 e calcule a soma dos elementos que estão na diagonal secundaria
"""


matrix = [[1, 2, 3], [789, 19, 19], [1891, 1, 1]]
num = 0
for i in range(3):
    for j in range(3):
        if i + j == 2:
            num = matrix[i][j] + num
print(num)

