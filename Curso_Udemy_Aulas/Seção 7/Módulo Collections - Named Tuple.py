"""
Módulo Collection - Named Tuple (Tupla Nomeada)

#Recaptulando Tuplas

Revisão Tuple
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple (Tupla Nomeada) -> São tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.


"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named tuple - Mais nítido

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])
# Forma 2 - Declaração Named Tuple
#                     nome da tupla,  parametros
cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 3 - Declaração Named tuple

cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Usando

ray = cachorro(idade=2, raça='Chow-Chow', nome='Ray')
print(ray)
# É como se fosse criar uma variável sua, sendo tudo de tupla válido

# Acessando os dados forma 1 -
print(ray[1])

# Acessando os dados forma 1 -

print(ray.raça)
print(ray.idade)
print(ray.nome)
