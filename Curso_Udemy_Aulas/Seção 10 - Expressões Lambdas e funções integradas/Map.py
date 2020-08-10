"""
Map

Com map, fazemos mapeamento de valores para função.

import math


def area(raio):
    alcula a área de um circulo com raio 'r'
    return math.pi * (raio**2)


raios = [2, 5, 7.1, 0.3, 10, 44]
# Forma comum de calcular todos os raios da lista
areas = []
for r in raios:
    areas.append((area(r)))
print(areas)

#  Forma 2 - Utilizando maps
# Map é uma função que recebe 2 parametros, o primeiro a função, o segundo um iteravel. Retorna um Map Object.
# e o tipo é 'map'
# Passa cada dado do iterável para a função.
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Forma 3 - Maps e Lambdas

areas2 = map(lambda raio: math.pi * (raio**2), raios)
print(list(areas2))


# OBS: A partir do primeiro momento que utilizamos o 'resultado' do map, ele zera


Para fixar - Map
Temos dados iteráveis:
dados: a1, a2, ..., an

Temos uma função:
Função: f(x)

Utilizamos a função map (f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função
O Map Object: f(a1), f(a2), f(...), f(an)
"""

# Mais exemplo:

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tókio', 27), ('Nova York',28)]
print(cidades)

# f = (9/5 * c) + 32
# Lambda

c_para_f = lambda dado: (dado[0], ((9/5 * dado[1]) + 32))
print(list(map(c_para_f, cidades)))

