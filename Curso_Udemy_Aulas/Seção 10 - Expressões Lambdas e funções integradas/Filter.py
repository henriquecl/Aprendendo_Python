"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção

# Biblioteca para trabalhar com dados estatisticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)

# OBS1: Assim como a função map(), a filter recebe dois parâmetros, sendo uma função e um iterável.
# OBS2: Que nem nos mapas, só podemos utilizar os valores de retorno do filter uma vez.
# OBS3: Se tentamos imprimir sem utiliza-lo irá retornar um filter object do tipo 'filter'
#                          TRUE OR FALSE
res = filter(lambda valor: valor > media, dados)
print(type(res))
print(res)
print(list(res))
print(list(res))


paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
# O none no filter vai fazer que os dados vazios sejam eliminados
res = filter(None, paises)  # Melhor maneira filtrar de uma lista os elementos vazio
# res = filter(lambda pais: pais != '', paises)
print(list(res))


# A diferença entre map e filter é:

map()-> Recebe dois parametros, uma função e um iterável  e retorna um objeto mapeando a função para cada elemento
do iterável. Nos mapas, geralmente as funções retornam valores diferente de booleanos.
filter() -> Recebe dois parametros, uma função e um iterável e retorna um objeto filtrando apenas os elementos acordo
com a função. Nos filtros, geralmente, as funções retornam valores booleanos para adicionar ou não em sua saida.


# Exemplos mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizza"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
print(usuarios)
# Filtrar os usuários que estão inativos no Twitter
# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2
inativos = list((filter(lambda usuario: not usuario['tweets'], usuarios)))
print(inativos)
"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo sua instrutora é: + nome da instrutora, desde que cada nome tenha menos de 5 letras

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
