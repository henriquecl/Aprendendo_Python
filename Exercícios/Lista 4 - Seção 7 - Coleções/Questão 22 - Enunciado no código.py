# Questão 22 - Faça um programa que elia dois vetores de 10 posições e calcule outro vetor contendo, nas posições pares
# os valores do primeiro vetor, e nas impares os valores do segundo

A = []
B = []
C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numero = 0

for i1 in range(10):
    print(f'Digite {10-i1} numer(os)')
    numero = float(input())
    A.append(numero)

for i2 in range(10):
    print(f'Digite {10-i2} numer(os)')
    numero = float(input())
    B.append(numero)

for i3 in range(0, 10, 2):
    C.pop(i3)
    C.insert(i3, A[i3])

for i4 in range(1, 10, 2):
    C.pop(i4)
    C.insert(i4, B[i4])

print(A)
print(B)
print(C)

