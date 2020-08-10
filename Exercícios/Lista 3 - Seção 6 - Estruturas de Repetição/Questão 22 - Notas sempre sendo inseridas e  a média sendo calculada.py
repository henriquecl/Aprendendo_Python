# Questão 22 - Escreva um programa completo que permita qqr aluno introduzir
# uma sequencia de notas (entre 10 e 20) e que mostre na tela o resultado da media
# aritmética. O nº de notas não será efetuado, e termina qnd for introduzido um
# valor que nao esteja entre 10 e 20

nota = int(input('Digite a nota para que seja calculada a média\n'))
i = 0
soma_das_notas = 0
primeira = nota
while 10 < nota < 20:
    nota = int(input('Digite a nota para que seja calculada a média\n'))
    i = i + 2
    soma_das_notas = soma_das_notas + nota + primeira
    if 10 < nota < 20:
        média = soma_das_notas/i
        print(f'Sua média é {média}')
