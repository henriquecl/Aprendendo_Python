"""
Questão 11 - Elabore uma função que receba três notas de um aluno como parametro e uma letra. Se a letra for A,
a função deverá calcular a média aritimética das notas. Se for P, deverá calcular a média ponderada com pesos 5, 3 e 2
"""


def media_aluno(tipo_de_media, nota1, nota2, nota3):
    media = 0
    if tipo_de_media == 'A':
        media = (nota1 + nota2 + nota3) / 3
    if tipo_de_media == 'P':
        media = (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
    return media


print(media_aluno('A', 3, 6, 9))
print(media_aluno('P', 3, 6, 9))

