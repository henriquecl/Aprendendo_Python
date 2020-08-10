"""
Questão 18  - Faça um programa que leia um arquivo contendo o nome e o preço de diversos produtos (separados por linha)
e calcule o preço total da compra
"""

with open('produtos.txt', 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read()
texto_separado = texto.split()
texto_separado.sort()
print(texto_separado)

lista_de_precos = []
try:
    for i in range(len(texto_separado)):
        numero = float(texto_separado[i])
        lista_de_precos.append(numero)
except ValueError:
    None

print(f'O preço total das compras foi: {sum(lista_de_precos)}')
