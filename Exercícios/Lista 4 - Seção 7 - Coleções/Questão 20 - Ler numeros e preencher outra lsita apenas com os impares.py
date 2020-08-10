# Questão 20 - Escreva um programa que leia numeros inteiros no intervalo de [0,50] e os armazene em umalista de 10 posi
# ções. Preencha uma segunda lista apenas com os números impares.

lista1 = []
lista2 = []
numero = 0

for i in range(10):
    numero = float(input('Digite um valor de 0 a 50\n '))
    while numero > 50 or numero < 0:
        numero = float(input('Digite um valor de 0 a 50 teste\n '))
    lista1.append(numero)
print(lista1)  # Só teste
for j in range(10):
    if lista1[j] % 2 != 0:
        lista2.append(lista1[j])
print(f'Os numeros impares foram:{lista2}')