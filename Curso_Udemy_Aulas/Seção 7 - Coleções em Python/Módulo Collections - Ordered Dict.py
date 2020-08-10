"""
Módulo Collections - Ordered Dict
# Ou seja, utilizando o Ordered Dict o dicionário garante a ordem dos elementos, além da maior perfomace.


# Em um dicionário a ordem de inserção dos elementos não é garantida

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave} e valor= {valor}')


# Fazendo import

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(chave, valor)
"""
from collections import OrderedDict
# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # Nesse caso, a ordem dos elementos não importa
# True

dict3 = OrderedDict({'a': 1, 'b': 2})
dict4 = OrderedDict({'b': 2, 'a': 1})

print(dict3 == dict4)  # Agr, a ordem dos elementos importa.
# False
