"""
Generators:

Em aulas anteriores nós estudamos:
- List Comprehension
- Dict //
- Set //

Não vimos:
- Tuple Comprehension... pq elas se chamam Generators

nomes = ['carlos', 'camila', 'carla, 'cassiano', 'cristiane', 'vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

# Poderiamos ter feito utilizando Generators
nomes = ['carlos', 'camila', 'carla', 'cassiano', 'cristiane', 'vanessa']
print(any(nome[0] == 'c' for nome in nomes))

# List Comprehension
res = [nome[0] == 'c' for nome in nomes]
print(type(res))

# Generator - Para melhor desempenho utilizar generator
res = (nome[0] == 'c' for nome in nomes)
print(type(res))

# Qual é a utilizade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof
# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string mais espaço ocupa
print(getsizeof('Geek'))
print(getsizeof('Geek Univeristy'))
print(getsizeof(9))
print(getsizeof(99))
print(getsizeof(999989789779))
print(getsizeof(True))
print(getsizeof(False))

from sys import getsizeof

# Gerando uma lista de números com List/set/dict Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
print(list_comp)

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})
print(set_comp)

# Gerando uma lista de números com Dict Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
print(dict_comp)
# Gerando uma lista de números com Generator
gen = getsizeof((x * 10 for x in range(1000)))
print(gen)
"""

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 100 for x in range(10000))
print(gen)
print(type(gen))

for num in gen:
    print(num)