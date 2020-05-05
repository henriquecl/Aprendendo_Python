"""
Questão 2 - Faça uma função que receba a data atual (dia, mês e ano em inteiro). E exiba-a na tela no formato por
extenso. Exemplo: Data 01/01/2000, imprimir: 1 de janeiro de 2020

"""


def data_por_extenso(dia, mes, ano):

    if mes == 1:
        mes_auxiliar = 'Janeiro'
    elif mes == 2:
        mes_auxiliar = 'Fevereiro'
    elif mes == 3:
        mes_auxiliar = 'Março'
    elif mes == 4:
        mes_auxiliar = 'Abril'
    elif mes == 5:
        mes_auxiliar = 'Maio'
    elif mes == 6:
        mes_auxiliar = 'Junho'
    elif mes == 7:
        mes_auxiliar = 'Julho'
    elif mes == 8:
        mes_auxiliar = 'Agosto'
    elif mes == 9:
        mes_auxiliar = 'Setembro'
    elif mes == 10:
        mes_auxiliar = 'Outubro'
    elif mes == 11:
        mes_auxiliar = 'Novembro'
    elif mes == 12:
        mes_auxiliar = 'Dezembro'

    return f"{dia} de {mes_auxiliar} de {ano}"


dia = int(input('Digite que dia é hoje\n'))
mes = int(input('Digite que mes estamos\n'))
ano = int(input('Digite que ano estamos hoje\n'))

print(data_por_extenso(dia, mes, ano))


