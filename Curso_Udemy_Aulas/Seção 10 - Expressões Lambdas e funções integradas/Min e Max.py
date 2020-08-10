"""
Min e Max

max(*args) -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.
# Ex 1 - Max

lista = [1, 8, 4, 99, 999, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 999, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 999, 34, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 999, 'e': 34, 'f': 129}
print(max(dicionario.values()))


# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('dale: '))
val2 = int(input('dale: '))

print(max(val1, val2)) # Recebe *args

MIN
min() -> O contrário do max, funciona exatamente igual só q com o menor valor, claro.


# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))  # Letra mais ao final do alfabeto
print(min(nomes))  # Letra mais ao inicio do alfabeto

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
"""
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Fade to Black", "tocou": 2},
    {"titulo": "Jah jah know", "tocou": 4},
    {"titulo": "Ladrão", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica["tocou"]))
print(min(musicas, key=lambda musica: musica["tocou"]))

# DESAFIO! Imprima somente o título da múscia mais e menos tocada
print(max(musicas, key=lambda musica: musica["tocou"])['titulo'])
print(min(musicas, key=lambda musica: musica["tocou"])['titulo'])

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max, min e lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])
