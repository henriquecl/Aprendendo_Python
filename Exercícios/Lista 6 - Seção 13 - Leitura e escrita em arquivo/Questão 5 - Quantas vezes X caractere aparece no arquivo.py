"""
Questão 5 - Faça um programa que recebe um arquivo texto e um caractere. Mostra na tela quantas vezes aquele caractere
ocorre dentro do arquivo
"""
with open('questao2.txt', 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read()

numero_de_ocorrencias = 0
caractere_desejado = input('Qual caractere deseja q eu mostre quantas vezes ele se repete: ')

for letra in texto:
    if letra == caractere_desejado:
        numero_de_ocorrencias = numero_de_ocorrencias + 1

print(f'O caractere {caractere_desejado} se repetiu {numero_de_ocorrencias}')
