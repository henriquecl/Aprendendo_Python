"""
Questão 7 - Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto contendo o texto do arqui
vo de entrada, mas com as vogais substituidas por ''*''
"""

with open('questao2.txt', 'r', encoding='UTF-8') as arquivo1:
    texto = arquivo1.read()

texto_em_lista = (list(texto))
for i in range(len(texto_em_lista)):
    if texto_em_lista[i] == 'a' or texto_em_lista[i] == 'e' or texto_em_lista[i] == 'i'\
            or texto_em_lista[i] == 'o' or texto_em_lista[i] == 'u':
        texto_em_lista[i] = '*'
lista_em_texto = ''.join(texto_em_lista)

with open('questao7.txt', 'w', encoding='UTF-8') as arquivo2:
    arquivo2.write(lista_em_texto)






