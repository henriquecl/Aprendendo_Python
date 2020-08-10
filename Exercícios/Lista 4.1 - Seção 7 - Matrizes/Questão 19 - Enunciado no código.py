"""
Questão 19 - Faça um programa que leia uma matrix 5x4 onde: (5 alunos 4 infos)
1º Coluna: Número de matricula
2ª Coluna: Média das provas
3ª Coluna: Média dos trabalhos
4ª Coluna: Nota final
a) Leia as 3 primeiras infos de cada aluno
b) Calcule a nota final como sendo a soma da média das provas e da média dos trabalhos
c) imprima a matrícula do aluno que obteve a maior nota final.
d) média aritimética das notas finais
"""

# Recebendo dados:
alunos = [[], [], [], [], []]
maior_nota = 0
matricular_maior_nota = 0
soma_das_notas_finais = 0

for i in range(5):
    for j in range(4):
        if j == 0:
            matricula = int(input('Digite sua matrícula: '))
            alunos[i].append(matricula)
        if j == 1:
            media_prova = int(input('Digite a média da sua prova: '))
            alunos[i].append(media_prova)
        if j == 2:
            media_trabalhos = int(input('Digite a média dos seus trabalhos: '))
            alunos[i].append(media_trabalhos)

# Calculando nota final
for i1 in range(5):
    nota_final = (alunos[i1][1] + alunos[i1][2]) / 2
    alunos[i1].append(nota_final)

#  Imprima a matricula do aluno que obteve a maior nota final
for i2 in range(5):
    if alunos[i2][3] > maior_nota:
        maior_nota = alunos[i2][3]
        matricular_maior_nota = i2
print(f'O aluno com a maior nota final foi o de matrícula: {alunos[matricular_maior_nota][0]}')

# Média das notas finais
for i3 in range(5):
    soma_das_notas_finais = soma_das_notas_finais + alunos[i3][3]
print(f'A média das notas finais foi: {soma_das_notas_finais / len(alunos)}')

for i4 in range(5):
    print(alunos[i4])
