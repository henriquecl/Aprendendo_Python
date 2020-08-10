"""
Questão 3 - Faça uma função para verificar se o número é positivo ou negativo. Sendo que o valor de retorno será 1 se
positivo, -1 se negativo e 0 se for igual a 0

"""


def numero(num):
    if num == 0:
        return 0
    elif num > 0:
        return 1
    return -1


num_teste = float(input('Digite um número\n'))
print(numero(num_teste))






