# Questão 31 - Faça um prg q leia 2 vetores de 10 elementos. Crie um vetor que seja a união de ambos sem repetição

lista1 = []
lista2 = []
lista_de_uniao = []

for i in range(10):
    numero = int(input(f'Digite {10-i} valores\n'))
    lista1.append(numero)

for i2 in range(10):
    numero = int(input(f'Digite {10-i2} valores\n'))
    lista2.append(numero)

lista_de_uniao = set(lista1).union(set(lista2))

print(lista1)
print(lista2)
print(lista_de_uniao)

