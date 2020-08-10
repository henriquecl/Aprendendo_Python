"""
Questão 13 - Faça um programa que permita que o usuário entre com diversos nomes e telefone para cadastro, e crie um,
arquivo com essas informações, uma por linha. O usuário finaliza a entrada com '0' para o telefone.
"""
with open('agenda.txt', 'a', encoding='UTF-8') as arquivo:
    while True:
        nome = input('Digite o nome do novo contado a ser adicionado: ')
        if nome == '0':
            break
        telefone = input('Digite o número desse contato: ')

        if telefone == '0':
            break
        contato = nome+': ' + telefone
        arquivo.write(contato + '\n')







