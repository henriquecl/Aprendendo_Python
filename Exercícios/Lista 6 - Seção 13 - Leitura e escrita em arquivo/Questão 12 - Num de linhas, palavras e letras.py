"""
Questão 12 - Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas e o número de palavras
desse arquivo. Escreva também quantas vezes cada letra ocorre no arquivo
"""

with open('questao2.txt', 'r', encoding='UTF-8') as arquivo:
    num_de_linhas = len(arquivo.readlines())
    arquivo.seek(0)
    texto = arquivo.read()

num_de_caracteres = len(list(texto))
num_de_palavras = len(texto.split())

print(f'O texto possui {num_de_caracteres} caracteres, {num_de_palavras} palavras e {num_de_linhas} linhas ')


