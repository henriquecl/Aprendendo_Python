"""
Questão 22 - Faça um programa que leia duas matrizes. A e B 3x3 calcule C = A*B
"""
a = [[], [], []]
b = [[], [], []]
c = [[], [], []]

for i in range(3):
    for j in range(3):
        numero = float(input(f'Digite o valor equivalente a posição [{i}][{j}]da primeira matriz '))
        a[i].append(numero)
for i1 in range(3):
    for j1 in range(3):
        numero = float(input(f'Digite o valor equivalente a posição [{i1}][{j1}]da segunda matriz '))
        b[i1].append(numero)

for i2 in range(3):
    for j2 in range(3):
        numero = a[i2][j2] * b[i2][j2]
        c[i2].append(numero)

for i3 in range(3):
    print(c[i3])
