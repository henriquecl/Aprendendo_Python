# Questão 2 - Crie um programa que leia 6 valores inteiros , e em seguida, mostre na tela os valores lidos

i = 0
lista = []
while i != 6:
    print('Digite um valor inteiro')
    numero = input()
    lista.append(numero)
    i = i + 1
print(f'{lista}')
