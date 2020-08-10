"""
Questão 11 - Peça para o usuário informar o nome de um arquivo e uma palavra, retorne quantas vezes a palavra aparece
no arquivo
"""
arquivo = input('Digite qual arquivo deseja abrir: ')
palavra = input('Digite por qual palavra-chave deseja buscar:')
contador = 0
with open(arquivo+'.txt', 'r', encoding='UTF-8') as arq:
    texto = arq.read()

separando_o_texto = texto.split()

for i in range(len(separando_o_texto)):
    if separando_o_texto[i] == palavra:
        contador = contador + 1
print(f'A palavra {palavra} é repetida {contador} vezes no texto')





