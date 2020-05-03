"""
Loop for

Loop -> Estrutura de repetição
    for -> uma dessas estruturas

Exemplos de iteráveis:
    - String
        nome = 'Geek Univerity'
    - Lista
        lista = [1, 3, 5, 7, 9]
    - Range
        numeros = range(1, 10)


nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo for 1 (iterando string)

for letra in nome:
    print(letra)

# Exemplo de for 2   (itegrando em uma lista)

for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)
# range(valor_inicial, valor_final - 1)
for numero in range(1, 10):
    print(numero)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for letra in enumerate(nome):
    print(letra)


qtd = int(input('Quantas vezes esse loop deve rodar?\n'))
soma = 0
for n in range(1, qtd+1):
    numero = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + numero
print(f'A soma é {soma}')


nome = 'Geek University'
for letra in nome:
    print(letra, end='')

# Original: U+1F60D
# Modificado : U0001F60D

for x in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
"""