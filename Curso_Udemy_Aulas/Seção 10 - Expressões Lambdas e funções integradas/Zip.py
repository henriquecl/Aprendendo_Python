"""
Zip

Bem painha.

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares
"""

# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, ]

zip1 = zip(lista1, lista2, 'abc')
print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, set ou Dicionário

print(list(zip1))
print(tuple(zip1))
print(set(zip1))


