# Questão 7 - Faça um programa que leia 10 inteiros positivos, ignorando não positivos,
# e imprima sua média

soma = 0
numero = 0
i = 0
while i != 10:
    numero = int(input(f'Digite {10 - i} numeros para ser calculada a média\n'))
    i = i+1
    if numero >= 0:
        soma = soma + numero
print(f'A média calculada é: {soma/10}')
