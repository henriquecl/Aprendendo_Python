"""
Questão 20 - Faça um programa que leia uma matriz 3x6 com valores reais.
a) imprima a soma de todos os valores das colunas impares
b) imprima a média aritmética dos elementos da segunda e quarta coluna
c) substituis os valores da sexta coluna pela soma dos valores das colunas 1 e 2
d) imprima a matriz modificada
"""
matrix = [[], [], []]
lista_auxiliar = []

# Entrada de dados
for i in range(3):
    for j in range(6):
        numero = float(input(f'Digite o número para a posiação [{i}][{j}]'))
        matrix[i].append(numero)

# Somas de todos os valores das colunas impares
for i2 in range(3):
    for j2 in range(1, 6, 2):
        num = matrix[i2][j2]
        lista_auxiliar.append(num)
print(sum(lista_auxiliar))

# Imprima a média aritmética dos elementos da segunda e quarta coluna

for i3 in range(3):
    print(f'A média entre o elemento da 2ª e da 4ª coluna é:{(matrix[i3][1] + matrix[i3][3])/2}')

# Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2
for i3 in range(3):
    matrix[i3][5] = matrix[i3][0] + matrix[i3][1]


