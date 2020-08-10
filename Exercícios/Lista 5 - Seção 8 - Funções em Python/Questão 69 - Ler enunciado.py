"""
Questão 69 - Faça um programa que faça o seguinte:
a) leia duas frações p e q
b) simplificar as frações
c) soma, subtração, produto e quociente entre as frações lidas
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


def soma_de_fracoes(numerador1, denominador1, numerador2, denominador2):
    denominador_comum = denominador1*denominador2
    numerador_resultante = (denominador_comum/denominador1)*numerador1 + (denominador_comum/denominador2)*numerador2
    return {numerador_resultante},{denominador_comum}


def diferenca_de_fracoes(numerador1, denominador1, numerador2, denominador2):
    denominador_comum = denominador1 * denominador2
    numerador_resultante = (denominador_comum / denominador1)*numerador1 - (denominador_comum / denominador2)*numerador2
    return f'{numerador_resultante}/{denominador_comum}'


def produto_de_fracoes(numerador1, denominador1, numerador2, denominador2):
    numerador_resultante = numerador1 * numerador2
    denominador_comum = denominador1 * denominador2
    return f'{numerador_resultante}/{denominador_comum}'


def quociente_de_fracoes(numerador1, denominador1, numerador2, denominador2):
    numerador_resultante = numerador1 * denominador2
    denominador_comum = denominador1 * numerador2
    return f'{numerador_resultante}/{denominador_comum}'


print(soma_de_fracoes(1, 2, 1, 2))
print(diferenca_de_fracoes(1, 2, 1, 2))
print(produto_de_fracoes(1, 2, 1, 2))
print(quociente_de_fracoes(1, 2, 1, 2))
