"""
Questão 23 -  Faça um programa que leia uma matriz A de tamanho 3x3 e calcule B = A²
"""
a = [[], [], []]
b = [[], [], []]

for i in range(3):
    for j in range(3):
        numero = float(input(f'Digite o valor equivalente a posição [{i}][{j}]da primeira matriz '))
        a[i].append(numero)

for i1 in range(3):
    for j1 in range(3):
        numero = a[i1][j1] ** 2
        b[i1].append(numero)

for i2 in range(3):
    print(b[i2])
