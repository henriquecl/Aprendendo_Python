# Questão 38 - Peça ao usuário 10 numeros e ordene por ordem crescente. Ordene assim que digitar. Mostre na tela
lista = []
for i in range(10):
    numero = float(input(f'Digite {10 - i } numeros.\n'))
    lista.append(numero)
    lista.sort()
    print(lista)
