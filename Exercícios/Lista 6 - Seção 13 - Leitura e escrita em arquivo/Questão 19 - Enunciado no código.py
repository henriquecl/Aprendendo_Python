"""
Questão 19 - Faça um programa que receba do usuário um arquivo que contenha o nome e a nota de diversos alunos
Da seguinte forma(NOME: JOÃO NOTA:8), um aluno por linha. Mostre na tela o nome e a nota do aluno que possui a maior
nota.
"""

with open('alunos.txt', 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read()
    arquivo.seek(0)
    num_linhas = len(arquivo.readlines())
lista_de_notas = []
texto_em_lista = texto.split()

for i in range(1, num_linhas + 1):
    lista_de_notas.append(float(texto_em_lista[(5*i) - 1]))

nota_max = str(max(lista_de_notas))
posicao_maior_nota = (texto_em_lista.index(nota_max))
aluno_com_maior_nota = texto_em_lista[posicao_maior_nota - 3]

print(f'O aluno com a maior nota foi {aluno_com_maior_nota} e tirou nota: {nota_max}')