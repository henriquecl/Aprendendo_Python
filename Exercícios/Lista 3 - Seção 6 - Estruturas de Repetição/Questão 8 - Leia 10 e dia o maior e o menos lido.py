# Questão 8 - Faça um programa cujo leia 10 e escreva o menor e o maior lido.

numero = 0
i = 0
menor_valor = 0
maior_valor = 0

while i != 10:
    numero = int(input(f'Digite {10 - i} numeros para eu falor qual o maior e qual o menor\n'))
    i = i + 1

    if numero > maior_valor:
        maior_valor = numero

    if numero < menor_valor:
        menor_valor = numero
print(f'O menor valor foi {menor_valor} e o maior valor foi {maior_valor}')

