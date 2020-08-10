# Questão 4 - Faça um programa que leia uma lista[8], e em seguida leia dois valores X,Y que sejam correspondente a duas
# posições da lista. Ao final, o programa deve escrever a smoma dos valores encontrados nas posições X e Y
lista = []
numero = 0

for i in range(8):
    print(f'Digite {8- i} valores')
    numero = int(input())
    lista.append(numero)
X = int(input('Digite um valor entre 0 e 7 \n'))
Y = int(input('Digite outro valor entre 0 e 7 \n'))
print(lista)
lista[X] = (X+Y)
lista[Y] = (X+Y)
print(lista)