"""
Questão 18  - Faça um programa que permita ao usuário entrar ocm uma matrix 3x3 com números inteiros. Em seguida, impri
ma, e gere uma lista cujo cada elemento é a soma das colunas
"""
matrix = [[], [], []]
lista = []

for i in range(3):
    for j in range(3):
        numero = int(input('Digite um número:'))
        matrix[i].append(numero)

for i in range(3):
    print(matrix[i])

for j1 in range(3):
    soma = 0
    for i1 in range(3):
        soma = soma + matrix[i1][j1]
    lista.append(soma)
print(lista)