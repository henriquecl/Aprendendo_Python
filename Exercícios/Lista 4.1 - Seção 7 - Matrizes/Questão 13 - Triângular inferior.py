"""
Questão 13 - Gere uma matriz 4x4 com valores no intervalo [1,20]. Faça um programa que a transforme numa matriz triangu
lar inferior, ou seja, atribuindo 0 a todos os elementos acima da diagonal principal
"""

matrix = [list(range(1, 5)), list(range(6, 10)), list(range(10, 14)), list(range(15, 19))]

for i in range(4):
    for j in range(4):
        if i < j:
            matrix[i][j] = 0

for i in range(4):
    print(matrix[i])



