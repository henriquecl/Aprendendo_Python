"""
Questão 2 - Faça um programa que receba do usuário um arquivo de texto e mostre na tela quantas linhas possui
"""
with open('questao2.txt', 'r', encoding='UTF-8') as arquivo:
    num_linhas = len(arquivo.readlines())
    print(f'O arquivo possui {num_linhas} linhas')


