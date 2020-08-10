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
