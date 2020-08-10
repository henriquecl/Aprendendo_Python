# Questão 14 - Faça um programa que leia 10 valores e verifique se existem valores iguais e os escreva na tela

lista = []
numero = 0

for i in range(10):
    print(f'Digite {10-i} valor(es)')
    numero = float(input())
    lista.append(numero)

for j in range(10):
    if lista.count(lista[j]) > 1:
        print(f'O valor {lista[j]} se repetiu {lista.count(lista[j])} vezes ')
