"""
Questão 2 - Declare uma matriz 5x5. Preencha com 1 a diagonal princiapl e com 0 os demais elementos. Escreva no final
a matriz obtida
"""
matrix = [list(range(0, 5)), list(range(5, 10)), list(range(10, 15)), list(range(15, 20)), list(range(20,25))]

for i in range(5):
    for j in range(5):
        if i == j:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0


for i in range(len(matrix)):
    if i == 0:
        print('A matriz digitada foi:')
    print(matrix[i])

