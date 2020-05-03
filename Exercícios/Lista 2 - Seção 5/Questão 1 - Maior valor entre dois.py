# Exercício 1 - Faça um programa que receba dois números e mostre qual o maior
# NOTE: Se não colocar o float(input..) ele não vai interpretar o numeral, e sim a string.
num1 = float(input('Digite um numero\n'))
num2 = float(input('Digite outro numero\n'))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num2 > num1:
    print(f'{num2} é maior que {num1}')
else:
    print('Os numeros são iguais')