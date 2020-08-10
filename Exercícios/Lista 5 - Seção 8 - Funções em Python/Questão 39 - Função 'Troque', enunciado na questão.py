"""
Questão 39 -  Faça uma função 'Troque', que recebe duas variáveis reais A e B e troca o valor delas.
"""


def troque(a, b):
    lista_a = [a]
    lista_b = [b]
    b = lista_a.copy()
    a = lista_b.copy()
    return a, b


print(troque(3, 5))

