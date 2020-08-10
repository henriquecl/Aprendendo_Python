
# Questão 33- Faça um programa que leia um vetor de 15 posições  e o compacte, ou seja, elimine posições com valor 0.
# para isso, todos os elementos a frente do zero devem ir para esquerda.

lista = []
lista_compactada = []
for i in range(15):
    numero = int(input(f'Digite {15-i} valores:\n'))
    lista.append(numero)

for i2 in range(len(lista)):
    if (lista[i2]) != 0:
        lista_compactada.append(lista[i2])
print(lista_compactada)
