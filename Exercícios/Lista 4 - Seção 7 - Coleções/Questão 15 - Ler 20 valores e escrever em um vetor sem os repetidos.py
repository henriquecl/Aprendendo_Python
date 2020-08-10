# Questão 15 - Leia 20 valores. Escreva os elementos do vetor eliminando elementos repetidos

lista = []
numero = 0

for i in range(20):
    print(f'Digite {20-i} numer(os)')
    numero = float(input())
    lista.append(numero)
print(lista)
for j in range(20):
    if lista.count(lista[j]) > 1:
        lista[j] = 0
print(lista)
