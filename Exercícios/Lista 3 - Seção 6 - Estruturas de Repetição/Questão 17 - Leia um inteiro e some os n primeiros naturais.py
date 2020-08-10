# Questão 17 - Faça um programa que leia um numero int positivo B e calcule a soma dos
# N primeiros numero naturais

numero = int(input('Digite um número\n'))
soma = 0

for numero in range(0, numero+1):
    soma = soma + numero

print(f'{soma}')