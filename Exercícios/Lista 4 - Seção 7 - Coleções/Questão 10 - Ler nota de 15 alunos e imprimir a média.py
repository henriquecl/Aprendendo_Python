# Questão 10 - Faça um progrmaa para ler a nota da prova de 15 alunos, calcule e imprima a média geral

notas = []
nota_individual = 0

for i in range(15):
    print(f'Digite as {15-i} notas')
    nota_individual = float(input())
    notas.append(nota_individual)
media_geral = (sum(notas))/(len(notas))
print(f'A média geral foi {media_geral}')
