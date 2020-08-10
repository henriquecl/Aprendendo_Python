"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizar-mos;
Pacote -> É um diretório contendo uma coleção de Módulos

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py, já nas
versões 3.X do Python não é mais necessário, mas normalmente é utilizado para manter compatibilidade


from geek import (geek1,
                  geek2)
from geek.university import (geek3,
                             geek4)

print(geek1.pi)
print(geek1.funcao1(4, 6))

print(geek2.curso)
print(geek2.funcao2())

print(geek3.funcao3())
print(geek4.funcao4())
"""

from geek.university.geek3 import funcao3
print(funcao3())
