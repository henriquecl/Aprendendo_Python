"""
Questão 7 - Gerar e imprimir uma matriz de tamanho 10x10, onde seus elementos são da forma:
A[i][j] = 2i+7j -2 se i<j
A[i][j] = 3i² -1 se i = j
A[i][j] = 4i³ - 5j² se i>j
"""

matrix = [[], [], [], [], [], [], [], [], [], []]

for i in range(10):
    for j in range(10):
        if i > j:
            numero = 4*(i**3) - 5*(j**2)
            matrix[i].append(numero)
        elif i == j:
            numero = (3*(i**2)) - 1
            matrix[i].append(numero)
        else:
            numero = (4*(i ** 3)) - 5 * (j ** 2)
            matrix[i].append(numero)

for i in range(10):
    print(matrix[i])