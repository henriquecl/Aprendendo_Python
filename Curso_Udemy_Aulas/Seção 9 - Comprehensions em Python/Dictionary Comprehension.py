"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

tupla = (1, 2, 3, 4)

set = {1, 2, 3, 4}

dicionário = {'a':1, 'b':2, 'c':3, 'd':4}

Sintaxe:
{chave:valor for valor in iterável}
[valor for valor in iterável]

# Exemplo - 1
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

# Exemplo 2 -
numero = [1, 2, 3, 4, 5, 1, 2]

quadrados = {valor: valor ** 2 for valor in numero}
print(quadrados)

# Exemplo 3 -

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
"""

# Exemplo 4 - Com lógica condicional

numero = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numero}
print(res)


