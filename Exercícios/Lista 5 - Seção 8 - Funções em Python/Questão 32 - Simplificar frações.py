"""
Questão 32 - Faça uma função chamada 'simplifica' que recebe como parâmetro o numerador e o denominador de uma fração.
Esta função deve simplificar a fração recebida dividindo o numerador e o denominador pelo maior fator possivel.
------UTILIZAR CONJUNTOS
"""


def simplifica(numerador, denominador):
    i = 1
    j = 1
    divisores_numerador = set()
    divisores_denominador = set()
    divisores_comuns = set()
    while i <= numerador:  # Descobrindo os divisores do numerador
        if numerador / i == int(numerador/i):
            divisores_numerador.add(i)
        i = i + 1
    while j <= denominador:  # Descobrindo os divisores do numerador
        if denominador / j == int(denominador/j):
            divisores_denominador.add(j)
        j = j + 1
    maximo_divisor_comum = max(divisores_denominador.intersection(divisores_numerador))
    return f"A fração simplificada foi: {numerador/maximo_divisor_comum}/{denominador/maximo_divisor_comum}"


print(simplifica(4788, 12357))







