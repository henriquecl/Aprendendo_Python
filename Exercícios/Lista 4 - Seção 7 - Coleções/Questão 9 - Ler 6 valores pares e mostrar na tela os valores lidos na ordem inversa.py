# Questão 9 - Crie um programa q lê 6 valores pares e mostre na tela os valores lidos na ordem inversa
lista = []
numero = 0

for i in range(6):
    print(f'Digite {6-i} valor(es) pares')
    numero = int(input())
    while numero % 2 != 0:
        print('Digite um valor par')
        numero = int(input())
    lista.append(numero)
lista.reverse()
print(lista)