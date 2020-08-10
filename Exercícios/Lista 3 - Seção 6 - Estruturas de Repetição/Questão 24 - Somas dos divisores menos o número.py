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
