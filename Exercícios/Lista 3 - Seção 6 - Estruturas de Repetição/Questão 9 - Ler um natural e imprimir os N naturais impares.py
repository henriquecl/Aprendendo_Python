# Questão 9 - Ler um número inteiro natural, dps imprima os N primeiros números naturais
# impares

numero = int(input('Digite um número\n'))
contagem = numero
if numero % 2 == 0:
    for contagem in range(numero, numero * 3, 2):
        print(f'{contagem+1}')

if numero % 2 != 0:
    for contagem in range(numero, numero*3, 2):
        print(f'{contagem+2}')
