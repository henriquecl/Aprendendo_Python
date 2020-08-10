# Questão 8 - Crie um programa q lê 6 valores inteiros e mostre na tela os vlaores lidos na ordem inversa

lista = []
numero = 0
for i in range(6):
    print(f'Digite {6-i} valor(es)')
    numero = int(input())
    lista.append(numero)
print(lista)
lista.reverse()
print(lista)
