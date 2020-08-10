"""
Módulo Collections - Default Dict

# Recaptulando dicionários
dicionario = {'curso': 'Programação em Pyhon: Essencial'}

print(dicionario)
print(dicionario['curso'])
#  print(dicionario['outro'])  # KeyError


Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar um lambda. Esse
valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que não existe, essa chave
será criada e o valor default será atribuído.

# OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.
"""

# Fazendo o import
from collections import defaultdict

dicionario = defaultdict(lambda: 'a chave nao existe')


dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

print(dicionario['outro'])  # Se fosse um dicionário comum iria dar Key error

print(dicionario)


