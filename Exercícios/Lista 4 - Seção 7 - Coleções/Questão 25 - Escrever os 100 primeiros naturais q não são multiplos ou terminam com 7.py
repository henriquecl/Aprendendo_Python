# Questão 25 - Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que não são múltiplos
# ou que terminam com 7

lista = []

for i1 in range(100):
    if i1 % 7 != 0 and i1 % 10 != 7:
        lista.append(i1)

print(lista)
