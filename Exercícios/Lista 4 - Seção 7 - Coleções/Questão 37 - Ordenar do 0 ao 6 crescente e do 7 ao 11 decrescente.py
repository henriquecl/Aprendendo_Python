# Questão 37 - Considerar um vetor de 11 elementos, imprimir o vetor de 0a6 em ordem crescente e de 711 decrescente
lista = []
lista_final = []
lista_crescente = []
lista_decrescente = []

for i in range(11):
    numero = int(input(f'Digite {11 - i} valores\n'))
    lista.append(numero)

lista.sort()

lista_crescente = list(lista.copy()[0:6])
lista_decrescente = list(lista.copy()[11:6:-1])
lista_final = lista_crescente.copy() + lista_decrescente.copy()
print(lista_final)