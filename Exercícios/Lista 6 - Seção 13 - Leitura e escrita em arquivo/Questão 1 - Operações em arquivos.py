"""
Escreva um programa que:
a) crie/abra um arquivo de nome "arq.txt"
b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com 0
c) Feche o arquivo (com o with não precisa fechar)
Agora, abra e laia o arquivo, caractere por caractere, e escreva na tela todos os caracteres armazenados
"""

with open('arq.txt', 'w', encoding='UTF-8') as arquivo:
    while True:
        caractere = input('Digite o que deseja inserir no arquivo, para parar digite 0:')
        if caractere == '0':
            break
        arquivo.write(caractere + '\n')

with open('arq.txt', 'r', encoding='UTF-8') as arquivo:
    print(arquivo.read())

