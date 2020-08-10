"""
Questão 6 - Faça uma função que recebe 3 números inteiros como parâmetro, representando horas, minutos e segundos
e os converta em segundos
"""


def transformar_em_segundos(horas, minutos, segundos):
    valor_em_segundos = horas*60*60 + minutos * 60 + segundos
    return valor_em_segundos


print(transformar_em_segundos(2, 2, 50))
