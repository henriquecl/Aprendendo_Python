"""
List comprehension

Nós podemos adicionar estruturas condicionais lógicvoas as nossas List Comprehension
"""

# Ex 1

numeros = list(range(1, 7))

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Qualquer número par módulo de 2 é 0, e 0 em python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número impar módulo de 2 é 1, e 1 em python é true
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# Ex 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
