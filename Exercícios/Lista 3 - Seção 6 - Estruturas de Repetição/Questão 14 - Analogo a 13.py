# Questão 14 - Faça um programa que leia um número inteiro pos  par e imprima todos os
# pares de 0 até N em ordem  decrescente

numero = int(input('Digite um número par\n'))
if numero % 2 == 0:
    for numero in range(numero, 0, -2):
        print(f'{numero}')
