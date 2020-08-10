"""
Questão 1 -Leia uma Matriz 4x4, conte e escreva quantos valores maiores que 10 ela possui
"""
matriz = [[], [], [], []]
matriz_auxuliar = []
numeromaior = 0

for i in range(4):
    for j in range(4):
        numero = float(input(f'Digite o valor [{i}][{j}] da matriz:'))
        if numero > 10:
            numeromaior = numeromaior + 1
        matriz[i].append(numero)

for i in range(len(matriz)):
    if i == 0:
        print('A matriz digitada foi:')
    print(matriz[i])
print(f'E ela possui {numeromaior} numer(os) maior(es) que 10')


