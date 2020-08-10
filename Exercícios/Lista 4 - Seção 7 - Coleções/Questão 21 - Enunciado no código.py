# Questão 21 - Faça um programa que receba dois vetores, A e B, com 10 numeros cada, Crie um novo vetor C. C = A - B
# Mostre na tela os dados do vetor C

A = []
B = []
C = []
numero = 0

for i1 in range(10):
    print(f'Digite {10-i1} numer(os)')
    numero = float(input())
    A.append(numero)

for i2 in range(10):
    print(f'Digite {10-i2} numer(os)')
    numero = float(input())
    B.append(numero)

for i3 in range(10):
    C.append(A[i3]-B[i3])
print(A)
print(B)
print(C)
