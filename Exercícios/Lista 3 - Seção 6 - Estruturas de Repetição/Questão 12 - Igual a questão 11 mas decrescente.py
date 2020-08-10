# Questão 12 - Faça um programa que leia um número inteiro pos e imprima todos os
# naturais de 0 até N em ordem  decrescente

numero = int(input('Digite um número\n'))

for numero in range(numero, -1, -1):
    print(f'{numero}')
