# Questão 11 - Faça um programa que leia um número inteiro pos e imprima todos os
# naturais de 0 até N em ordem crescente

numero = int(input('Digite um número\n'))

for numero in range(0, numero+1):
    print(f'{numero}')
