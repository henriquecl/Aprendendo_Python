"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são que outros arquivos Python.

Módulo Random -> É um módulo buil-in. Possui várias funções para geração de números pseudo-aleatórios


# OBS: Existem duas formas de se utilizar um módulo ou função deste.
Forma 1  - Importando todo o módulo (Não recomendado). Ao realizar o import de todo o módulo todas as funções,atributos,
classes e propriedades que estiverem dentro do módulo, ficarão disponíveis (em memória). Caso você saiba quais funções
você precisa utilizar, então esta não seria a forma ideal de utilização.

import random
print(random.random())

random() -> Gera um número real pseudo aleatório entre 0 e 1.
Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função, separados
por ponto

Forma 2 - Importando uma função específica do módulo (Forma recomendada)
Estamos falando: Do módulo random importe a função random.

from random import random as num_aleatorio
for i in range(100):
    print(num_aleatorio())

uniform () -> Gerar um número real pseudo-aleatório entre os valores estabelecidos
from random import uniform

for i in range(10):
    print(uniform(5, 10))  # O set não é incluido


randint() -> Gera um número inteiro pseudo-aletório entre os valores estabelecidos
from random import randint
for i in range(6):
    print(randint(1, 61), end=', ')

choise() -> Mostra um valor aleatório entre um iterável.
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))
print(choice('Geek University'))

shuffle() -> Tem a função de embaralhar dados
from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas.pop(0))
print(cartas)
"""

