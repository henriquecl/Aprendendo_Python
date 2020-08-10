"""
Questão 21 -  Faça um programa que leia duas matrizes 2x2 com valores reais. Ofereça ao usuário um menu com opções:
a) somas as duas matrizes
b) subtrair as duas matrizes
c) adicionar umas cte as duas matrizes
d) imprimir as matrizes
"""
matrix1 = [[], []]
matrix2 = [[], []]
matrix_auxiliar = [[], []]
saida = 0

for i in range(2):
    for j in range(2):
        numero = float(input(f'Digite o valor [{i}][{j}] da primeira matriz: '))
        matrix1[i].append(numero)

for i1 in range(2):
    for j1 in range(2):
        numero = float(input(f'Digite o valor [{i1}][{j1}] da segunda matriz: '))
        matrix2[i1].append(numero)

while saida != 'sair':
    saida = int(input('Digite 0 para somar as matrizes, 1 para subtrair,'
                      ' 2 para add uma cte, 3 para imprimir, sair para parar:'))

    if saida == 0:
        for i2 in range(2):
            for j2 in range(2):
                numero = matrix1[i2][j2] + matrix2[i2][j2]
                matrix_auxiliar[i2].append(numero)

    if saida == 1:
        for i3 in range(2):
            for j3 in range(2):
                numero = matrix1[i3][j3] - matrix2[i3][j3]
                matrix_auxiliar[i3].append(numero)
    if saida == 2:
        cte = float(input('Digite o valor da constante'))
        for i4 in range(2):
            for j4 in range(2):
                numero = matrix_auxiliar[i4][j4] + cte
                matrix_auxiliar[i4].append(numero)

    if saida == 3:
        for i5 in range(2):
            print(matrix_auxiliar[i5])

    if saida == 'sair':
        break
