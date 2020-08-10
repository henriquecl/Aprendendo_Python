# Questão 30 - Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção entre os 2
# Ou seja, contem apenas os numeros que estão em ambos os vetores.
# PAROU AQUI A PARTE DE LISTA. TEM Q VER AS OUTRAS AULAS.
lista1 = []
lista2 = []
lista_de_intersecao = []

for i in range(10):

    numero = int(input('Digite um número\n'))
    lista1.append(numero)


for i2 in range(10):
    numero = int(input('Digite um número\n'))
    lista2.append(numero)

lista_de_intersecao = (set(lista1).intersection(set(lista2)))

print(lista1)
print(lista2)
print(lista_de_intersecao)

