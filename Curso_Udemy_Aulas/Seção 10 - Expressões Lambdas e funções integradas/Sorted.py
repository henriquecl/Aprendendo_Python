"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que estudamos em listas. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

O sorted SEMPRE retorna uma lista com os elementos do iterável ordenados.

# Exemplo  1.

numeros = (6, 1, 8, 2)
print(numeros)
print(sorted(numeros))
print(numeros)

OBS: O sorted não modifica o objeto! Ele cria uma nova LISTA com os valores ordenados, sendo os dados padrão
não alterado.

numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))
# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor


# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizza"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor":"amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], 'cor': 'preto', "musica": "rock"}
]

print(usuarios)

# Ordenando pelo username - Ordem alfabética.
print(sorted(usuarios,  key=lambda usuario: usuario["username"]))
# Ordenando pelo número de tweets - Ordem crescente
print(sorted(usuarios,  key=lambda usuario: len(usuario["tweets"])))


# Último exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Fade to Black", "tocou": 2},
    {"titulo": "Jah jah know", "tocou": 4},
    {"titulo": "Ladrão", "tocou": 32}
]
# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
"""
