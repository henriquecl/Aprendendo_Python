"""
Questão 4 - Leia uma matriz 4x4, imprima a matriz e retorne a localização do maior valor
"""

from random import randint

matrix = [[1, 2, 3, 4, 5], [789, 19, 19, 19, 19], [1891, 1, 1, 1, 1], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
linha = 0
coluna = 0
maximo = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] > maximo:
            maximo = matrix[i][j]
            linha = i
            coluna = j

for i in range(len(matrix)):
    if i == 0:
        print('A matriz digitada foi:')
    print(matrix[i])
print(f'A posição do maior valor está na linha: {linha+1} e na coluna: {coluna+1} e ele é {maximo}')




