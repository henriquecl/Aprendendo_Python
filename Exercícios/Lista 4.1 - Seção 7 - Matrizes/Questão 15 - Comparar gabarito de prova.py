"""
Questão 15 - Leia uma matriz 5x10 que se refere a 10 questões de múltipla escolha, referente a 5 alunos. Leia também um
vetor de 10 posições contendo o gabarito de respostas que podem ser a, b, c, ou d. Seu programa deverá comparar as repos
tas de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo a pontuação de cada aluno.
"""

prova_alunos = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                ['b', 'c', 'd', 'a', 'c', 'b', 'a', 'a', 'a', 'a'],
                ['a', 'a', 'd', 'a', 'd', 'd', 'a', 'b', 'c', 'a'],
                ['a', 'b', 'a', 'a', 'c', 'a', 'd', 'b', 'a', 'd'],
                ['a', 'c', 'c', 'a', 'a', 'b', 'c', 'a', 'd', 'a']]
gabarito = ['a', 'b', 'c', 'd', 'c', 'd', 'b', 'a', 'a', 'b']
nota = 0

for i in range(5):
    nota = 0
    for j in range(10):
        if prova_alunos[i][j] == gabarito[j]:
            nota = nota + 1

    print(f'O aluno {i} tirou nota: {nota}')








