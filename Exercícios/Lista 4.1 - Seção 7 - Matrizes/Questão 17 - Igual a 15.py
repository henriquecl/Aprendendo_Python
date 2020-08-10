# Questão 17  - Leia 10 valores e atribua o valor 0 para todos os elementos que forem negativos

lista = []
numero = 0

for i in range(20):
    print(f'Digite {20-i} numer(os)')
    numero = float(input())
    lista.append(numero)
print(lista)
for j in range(20):
    if lista[j] < 0:
        lista[j] = 0
print(lista)
