# Questão 5 - Leia uma lista de 10 valores. Conte e escreva quantos valores pares ele possui
lista = []
numero = 0
contagem = 0
for i in range(10):
    print(f'Digite {10- i } valor(es)')
    numero = int(input())
    lista.append(numero)

for j in range(len(lista)):
    if lista[j] % 2 == 0:
        contagem = contagem + 1
print(f'A lista tem {contagem} numer(os) par(es)')