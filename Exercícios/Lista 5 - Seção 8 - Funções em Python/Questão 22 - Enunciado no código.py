"""
Questão 22 - Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linha com pontos de exclama
ção conforme o exemplo da questão
"""


def loucura(num):

    j = 0
    texto = ''
    while j != num:
        j = j + 1
        texto = texto + ('j'*j) + '\n'
    return texto


print(loucura(9))



