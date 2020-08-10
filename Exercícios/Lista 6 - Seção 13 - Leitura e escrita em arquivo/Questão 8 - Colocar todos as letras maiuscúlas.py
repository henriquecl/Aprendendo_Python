"""
Questão 8 - Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo, mas com todas as
letras maiúsculas convertidas para maiúsculas.
"""

arquivo = input('Digite qual arquivo deseja abrir: ')
with open(arquivo + '.txt', 'r', encoding='UTF-8') as arq:
    texto = arq.read()


with open('questao8.txt', 'w', encoding='UTF-8') as arq2:
    arq2.write(texto.upper())




