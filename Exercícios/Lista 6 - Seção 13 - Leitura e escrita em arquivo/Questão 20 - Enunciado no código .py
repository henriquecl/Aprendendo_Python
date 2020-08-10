"""
Questão 20 - Crie um programa que receba como entrada o número de alunos. Receba em uma lista o nome dos alunos e o seg
undo  contém suas notas finais. Crie um arquivo que armazene a cada linha o nome do aluno e sua nota final. O nome tem
que ter no máximo 40 caracteres. Se não tiver 40, preencher com espaço em branco
"""
alunos = []
notas = []
texto = ''
while True:
    nome = input('Digite o nome do aluno, para parar digite "sair"\n')
    if nome == 'sair':
        break
    nota = input(f'Digite a nota da(o) aluno: ')
    alunos.append(nome)
    notas.append(nota)


for i2 in range(len(alunos)):
    if len(alunos[i2]) < 40:
        alunos[i2] = alunos[i2] + ' '*(40 - len(alunos[i2]))

for i3 in range(len(alunos)):
    texto = texto + alunos[i3] + 'Nota:' + notas[i3] + '\n'

with open('questao20.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write(texto)

