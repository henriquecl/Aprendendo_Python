# Questão 6 - Faça um programa que receba do usúario uma lista de 10 valores, e em seguida imprimir o maior e menor
# elemento da lista
numero = 0
lista = []
for i in range(10):
    print(f'Digite {10 - i} valor(es)')
    numero = int(input())
    lista.append(numero)
lista.sort()
maior_valor = lista[9]
menor_valor = lista[0]
# podia ter feito
maior_valor2 = max(lista)
menor_valor2 = min(lista)
print(f'O maior valor foi {maior_valor}, e o menor valor foi {menor_valor}')