"""
# Questão 1 - Faça um programa que determine e o mostre os cincos primeiros
# múltiplos de 3, considerando numeros maiores que 0
i = 0
for num in range(1, 2000):
    if num % 3 == 0:
        i = i + 1
        print(f'O multiplo de numero {i} de 3 é {num}')
    if i == 5:
        break


# Questão 2 - Escreva um programa que escreva na tela de 1-100 de 1 em 1, em for e em while
# Note que, o range no for já faz o incremento para entrar no for 3 vezes

i = 0
for i in range(0, 3):
    for num in range(1, 101):
        print(num)

i = 0
ii = 0
while ii <= 100:
    print(ii)
    ii = ii + 1

# Questão 3 - Faça uma algoritmo usando while que conta de 10 a 0 e mostrando a msg
# FIM após a contagem

i = 10
while i >= 0:
    print(i)
    i = i - 1
print('FIM')


# Questão 4 - Escreva um programa que declare um inteiro, e incremente-o de
# 1000 em 1000 e imprimindo seu valor na tela até que seja 100.000

for i in range(0, 100_000, 1000):
    print(i)

# Questão 5 - Faça um programa que peça para o usuário digitar 10 valores e some-os
soma = 0
for i in range(0, 10):
    numero = float(input(f'Digite {10 - i} numero(s) para a soma ser realizada\n'))
    soma = soma + numero

print(f'A soma dos valores inseridos foi {soma}')

# Questão 6 - Faça  um programa que leia 10 inteiros e imprima sua média
soma = 0
numero = 0
i = 0
while i != 10:
    numero = int(input(f'Digite {10 - i} numeros para ser calculada a média\n'))
    i = i+1
    soma = soma + numero
print(f'A média calculada é: {soma/10}')


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


# Questão 10 - Faça um programa que calcule e mostre a soma dos 50 1ºs numeros pares
b= 0
for i in range(0, 101, 2):
    b = b + i
print(f'{b}')


# Questão 11 - Faça um programa que leia um número inteiro pos e imprima todos os
# naturais de 0 até N em ordem crescente

numero = int(input('Digite um número\n'))

for numero in range(0, numero+1):
    print(f'{numero}')

# Questão 12 - Faça um programa que leia um número inteiro pos e imprima todos os
# naturais de 0 até N em ordem  decrescente

numero = int(input('Digite um número\n'))

for numero in range(numero, -1, -1):
    print(f'{numero}')

# Questão 13 - Faça um programa que leia um número inteiro pos  par e imprima todos os
# pares de 0 até N em ordem  crescente

numero = int(input('Digite um número par\n'))
if numero % 2 == 0:
    for numero in range(0, numero+1, 2):
        print(f'{numero}')

# Questão 14 - Faça um programa que leia um número inteiro pos  par e imprima todos os
# pares de 0 até N em ordem  decrescente

numero = int(input('Digite um número par\n'))
if numero % 2 == 0:
    for numero in range(numero, 0, -2):
        print(f'{numero}')

# Questão 15 - só imprmir impar crescente
# Questão 16 - só imprmir impar decrescente


# Questão 17 - Faça um programa que leia um numero int positivo B e calcule a soma dos
# N primeiros numero naturais

numero = int(input('Digite um número\n'))
soma = 0

for numero in range(0, numero+1):
    soma = soma + numero

print(f'{soma}')

# Questão 18 - Escreve um algoritmo que leia certa quantidade de números e imprima o maior
# deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve
# ser fornecido pelo usuário

qtd_de_num = int(input('Digite quantos números você deseja fornecer\n'))
maior_numero = 0
num_de_vezes = 0

while qtd_de_num != 0:
    qtd_de_num = qtd_de_num - 1
    numero = int(input('Digite um número\n'))
    if maior_numero <= numero:
        maior_numero = numero

    if maior_numero == numero:
        num_de_vezes = num_de_vezes + 1


print(f'O maior numero foi o {maior_numero}, e foi digitado {num_de_vezes} vez(es)')




# Questão 19 - Leia número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos
# que compõem o número

numero = int(input('Digite um número entre 100 e 999\n'))
unidade = 0
dezena = 0
centena = 0


while numero > 999 or numero < 100:
    numero = int(input('Digite um número entre 100 e 999\n'))

centena = (numero // 100)
dezena = ((numero//10) % 10)
unidade = (numero % 10)

print(f'A centena foi:{centena} \nA dezena foi:{dezena} \nA unidade foi:{unidade}')


# Questão 20 - Ler uma sequencia de numeros inteiros e determinar se são pares ou não.
# Deverá informar o nº de dados lidos e nº de valores pares. O processo termina quando
# for digitado o número 1000

numero = 0
i = 0
j = 0
while numero != 1000:
    numero = int(input('Digite os valores, e digite 1000 quando quiser parar\n'))
    if numero != 1000:
        i = i + 1
        if numero % 2 == 0:
            j = j + 1
print(f'Foram lidos {i} números, sendo entre eles {j} numeros pares')


# Questão 21 - Faça  um programa que receba 2 números.
# Calcule e mostre: a soma dos números pares desse intervalo de numeros
# incluindo os núemros
# a multiplicação dos números impares desse intervale, incluindo os digitados

num1 = int(input('Digite um número\n'))
num2 = int(input('Digite um número\n'))
b = 0
c = 1
# Se o numero for par e num 1 maior que num 2

if num1 % 2 == 0 and num1 > num2:
    for soma in range(num2, num1+1, 2):
        b = b + soma
        c = c * soma

    print(f'A soma dos números pares desse intervalo é:{b} e o produto dos imp'
          f'ares é {c}')
# Se o numero for par e num 2 maior que num 1

if num1 % 2 == 0 and num2 > num1:
    for soma in range(num1, num2+1, 2):
        b = b + soma
    print(f'A soma dos números pares desse intervalo é:{b}')
# Se o numero for impar e num 1 maior que num 2

if num1 % 2 != 0 and num1 > num2:
    for soma in range(num2+1, num1+1, 2):
        b = b + soma
    print(f'A soma dos números pares desse intervalo é:{b}')
# Se o numero for impar e num 2 maior que num 1

if num1 % 2 != 0 and num2 > num1:
    for soma in range(num1+1, num2+1, 2):
        b = b + soma

    print(f'A soma dos números pares desse intervalo é:{b}')


# Questão 22 - Escreva um programa completo que permita qqr aluno introduzir
# uma sequencia de notas (entre 10 e 20) e que mostre na tela o resultado da media
# aritmética. O nº de notas não será efetuado, e termina qnd for introduzido um
# valor que nao esteja entre 10 e 20

nota = int(input('Digite a nota para que seja calculada a média\n'))
i = 0
soma_das_notas = 0
primeira = nota
while 10 < nota < 20:
    nota = int(input('Digite a nota para que seja calculada a média\n'))
    i = i + 2
    soma_das_notas = soma_das_notas + nota + primeira
    if 10 < nota < 20:
        média = soma_das_notas/i
        print(f'Sua média é {média}')



# Questão 23 - Leia um numero positivo e imprima seus divisores

numero = int(input('Digite um número inteiro positivo\n'))
i = numero
divisor = 0

while numero < 0:
    numero = int(input('Digite um número inteiro positivo\n'))
while i != 0:
    divisor = divisor + 1
    i = i - 1
    if numero % divisor == 0:
        print(f'O numero é divisível por {divisor} ')


# Questão 24 - a soma dos divisores de um número com exceção do número

numero = int(input('Digite um número inteiro positivo\n'))
numero_inicial = numero
i = numero
divisor = 0
soma_dos_divisores = 0

while numero < 0:
    numero = int(input('Digite um número inteiro positivo\n'))
    numero_inicial = numero
while i != 0:
    divisor = divisor + 1
    i = i - 1
    if numero % divisor == 0:
        soma_dos_divisores = soma_dos_divisores + divisor
        print(f'O numero é divisível por {divisor} ')
print(f'A soma dos divisores é: {soma_dos_divisores - numero_inicial}')

"""

# Questão 25 até questão o final é só a lógica que muda, a programação não soma.


