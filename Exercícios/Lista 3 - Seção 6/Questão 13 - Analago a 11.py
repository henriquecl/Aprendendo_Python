# Questão 13 - Faça um programa que leia um número inteiro positivo  par e imprima todos os
# pares de 0 até N em ordem  crescente

numero = int(input('Digite um número par\n'))
if numero % 2 == 0:
    for numero in range(0, numero+1, 2):
        print(f'{numero}')
