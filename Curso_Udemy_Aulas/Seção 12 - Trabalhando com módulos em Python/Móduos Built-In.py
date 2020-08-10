"""
Trabalhando com módulos Built-In (Módulos integrados, que já vem instalados no Python)
-------------------------
|Python|Módulos built-in|
------------------------
    Utilizando alias (apelidos) para módulos ou funções
import random as rdm
print(rdm.random())
    Podemos importar todas as funções de um módulo utilizando  o *
from random import *
    Diferente de fazer import random, a maneira de utilizar não precisa do random.rondom(), só random()
print(random())
    Utilizando alias pra Funções
from random import random as rdm, randint as rdi
print(rdm())
print(rdi(3, 49))

# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import (random as rdm,
                    randint,
                    shuffle as shuff,
                    choice)
print(rdm())
print(randint(0, 10))
print(shuff([1, 2, 3, 4, 5]))
print(choice([1, 2, 3, 4, 5]))
https://docs.python.org/3/py-modindex.html
"""