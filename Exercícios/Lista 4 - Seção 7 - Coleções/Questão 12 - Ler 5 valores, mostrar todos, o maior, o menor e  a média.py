# Questão 12 - Faça um programa para ler 5 valores, mostrar todos os valores lidos, junto com o maior valor,
# o menor e a média dos valores
numero = 0
lista = []
for i in range(5):
    print(f'Digite {5-i} valor(es)')
    numero = float(input())
    lista.append(numero)

print(f'Os valores inseridos foram {lista} maior valor inserido foi {max(lista)}, o menor {min(lista)}')
print(f'Já a media dos valores inseridos foi {sum(lista)/len(lista)}')