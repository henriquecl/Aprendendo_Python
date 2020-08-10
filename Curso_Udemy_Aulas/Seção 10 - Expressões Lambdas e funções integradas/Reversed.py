"""
Reversed

OBS: Não confunda com a função reverse() que estudamos na listas, que só funciona com LISTAS.

A função reverseD funciona com qualquer iterável, sua função é inverter o iterável

A função retorna um iterável chamado List Reverse Iterator
"""

# Exemplos
tupla = (1, 2, 3, 4, 5)
print(list(reversed(tupla)))
print(tuple(reversed(tupla)))
print(set(reversed(tupla)))  # Lembrando que o set não existe ordem, logo pode retornar qualquer coisa


# Podemos iterar sobre o reversed

for letra in reversed('Geek Univeristy'):
    print(letra, end='')






