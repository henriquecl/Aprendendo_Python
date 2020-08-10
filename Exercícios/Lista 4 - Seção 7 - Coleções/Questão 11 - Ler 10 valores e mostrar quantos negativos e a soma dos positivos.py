# Questão 11 - Faça um programa que lista 10 valores reais, calcule e mostre a quantidade de negativos e a
# soma dos números positivos dessa lista

lista = []
numero = 0
qtd_num_negativos = 0
soma_num_positivos = 0
for i in range(10):
    print(f'Digite {10-i} valores:')
    numero = float(input())
    lista.append(numero)

for j in range(len(lista)):
    if lista[j] < 0:
        qtd_num_negativos = qtd_num_negativos + 1

for j2 in range(len(lista)):
    if lista[j2] >= 0:
        soma_num_positivos = soma_num_positivos + lista[j2]
print(f'Dos valores inseridos {qtd_num_negativos} são negativos,e a soma dos positivos foi:{soma_num_positivos}')