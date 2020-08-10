"""
Questão 34 - Faça uma função não-recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo dess
número. O fatorial duplo é definido como o produto de todos os números impares naturais de 1 até algum impar N.
"""


def fatorial_duplo(numero):
    i = 1
    produto_dos_numeros = 1
    divisores_impares_numero =[]
    while i <= numero:  # Descobrindo os divisores do numerador
        if numero / i == int(numero/i):
            if i % 2 != 0:
                divisores_impares_numero.append(i)
        i = i + 1
    for j in range(len(divisores_impares_numero)):
        produto_dos_numeros = produto_dos_numeros*divisores_impares_numero[j]
    return divisores_impares_numero, produto_dos_numeros


print(fatorial_duplo(99))

