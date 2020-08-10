"""
Questão 9 - Faça um programa que receba dois arquivos do usuário, e crie um terceiro com o conteúdo dos dois primeiros
juntos, o conteúdo do primeiro seguido do segundo
"""

with open('questao2.txt', 'r', encoding='UTF-8') as arquivo1:
    texto1 = arquivo1.read()

with open('questao8.txt', 'r', encoding='UTF-8') as arquivo2:
    texto2 = arquivo2.read()

with open('questao9.txt', 'a', encoding='UTF-8') as arquivo3:
    arquivo3.write(texto1 + '\n')
    arquivo3.write(texto2)

