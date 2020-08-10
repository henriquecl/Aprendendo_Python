# Questão 29 - Faça um programa que receba 6 números inteiros e mostre:
# Os númeors pares digitados.
# A soma dos números pares
# Os números impares
# A quantidade de números impares

lista = []
numeros_pares = []
numeros_impares = []

for i in range(6):  # Recebendo os dados
    numero = int(input('Digite um número\n'))
    lista.append(numero)

for i2 in range(6):  # Números pares
    if lista[i2] % 2 == 0:
        numeros_pares.append(lista[i2])

for i3 in range(6): # Números impares
    if lista[i3] % 2 != 0:
        numeros_impares.append(lista[i3])

print(f'Os números pares digitados foram: {numeros_pares}, e a soma deles foi {sum(numeros_pares)}')
print(f'Os números impares digitados foram: {numeros_impares}, e a quantidade deles foi {len(numeros_pares)}')
