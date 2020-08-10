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
