"""
Listas (list) - Uma das coisas mais importantes que tem

Listas em Python funcionam como vetores/matrizes (arrays), com a
diferença de serem DINÂMICO e também de podermos colocar QUALQUER
tipo de dado

Linguagens  C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5
    este array será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e só ir adicionando elementos
enquanto houve memória disponivel, pode ir colocando elementos.
- Qualquer tipo de dado: As listas não possuem tipo de dado fixo; Ou seja, podemos colocar qlqr
tipo de dado;

As listas em Python são representados por colchetes: []

# Podemos facilmente checar se determinado valor está na lista

if 'g' in lista5:
    print('O caractere está na lista')
else:
    print('O caractere não está na lista')

# Podemos facilmente ordenar uma lista -sort

lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

# Podemos facilmente contar o número de ocorrência de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))
"""
# Adicionar elementos em listas
"""
Para adicionar elementos em listas, utilizamos a função append
Para adicionar varios elementos únicos, utilizamos extend
OBS: Com append, nós só conseguimos add um elemento por vez,
para contornar isso, passamos outra lista dentro do append
ficando assim, uma lista dentro de outra lista
SEMPRE VÃO PARA O FIM DA LISTA

print(lista1)
lista1.append(3)
print(lista1)
lista1.append([8, 3, 1])

if [8, 3, 1] in lista1:
    print('lalaa')
else:
    print('lalalaa')

print(lista1)
lista1.extend([3, 3, 3])
print(lista1)
print(lista1.count(3))

# Podemos inserir um novo elemento na lista informando a posição
# do indíce. Não substituindo, e sim, desloncado para a direita a lita

lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos juntar duas listas

lista1 = lista1 + lista2
OU
lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista
lista1.reverse()
print(lista1)

# Copiar uma lista
lista6 = lista2.copy()

# Numero de elementos da lista
print(len(lista1))

# Podemos remover facilmente o útilmo elemento de uma lista
obs: também retorna o elemento q ele removeu
lista5.pop()

# Podemos remover um elemento pelo indice
# Obs: Os elementos a direita desse indice serão deslocado para
# a esquerda
# Obs: Se tentar removar um elemento que não existir, irá dar IndexError
lista5.pop(2)

# Podemos remover todos os elementos
lista5.clear()

# Podemos facilmente repetir elementos em uma lista
nova = [1, 3, 5]
nova = nova * 3

# Podemos converter uma string para uma lista
--- Exemplo 1
curso = 'programação em python :  Essencial'
print(curso)
curso = curso.split()
print(curso)
Obs: Por padrão, o split separa o elementos pelo espaço entre elas
--- Exemplo 2
curso = 'Programação,em,python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Podemos converter uma lista em uma string
lista6 = ['Programação', 'em', 'Python',':','Essencial']
print(lista6)
curso = ' '.join(lista6)
# Ou seja, pega a lista 6, coloca 'espaço' entre cada elemento
# e transforma em string
print(curso)

# Iterando sobre listas

Exemplo 1 - Utilizando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

Exemplo 2 - Utilizando while
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para parar")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
print(numeros)
numeros1 = [num1, num2, num3, num4, num5]
print(numeros1)

# Fazemos acesso aos elementos de forma indexada
cores = ['azul', 'amarelo', 'vermelho']
print(cores[0])
print(cores[1])
print(cores[2])
# Fazer acesso aos elementos de forma indexada inversa
# Pense na lista como um circulo
print(cores[-1])  # O ultimo elemento

# Revisitando for e while
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
    
# Gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)

# Outros métodos não tão importantes mas também úteis

Encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros)

Em qual indice da lista está o valor 5
Obs: Se tiver mais de um valor, será retornado o primeiro que aparece
print(numeros.index(5))
Caso não tenha o elemento na lista, será apresentado ValueError
Podemos fazer busca dentro de um range, ou seja,
qual indice começar a buscar
#      (o que queremos, a partir do indice )
print(numeros.index(5, 1))

# Podemos fazer busca dentro de um range, inicio/fim

print(numeros.index(8, 3, 6))  # Busca pra mim o valor 8 entre 3 e 6

# Revisão slicing
lista[inicio:fim:passo]
range[inicio:fim:passo]

Trabalhando com slice de listas com o parâmetro 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:])

Trabalhando com slice de listas com o parâmetro 'fim'

print(lista[:2])  # começa em 0, e vai até o indice 2-1

# Invertendo valores em uma lista

nomes = ['Geek', 'University']
print(nomes)
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))  # soma
print(max(lista))  # máximo
print(min(lista))  # minimo
print(len(lista))  # tamanho da lista

# Questão 18  fazendo por lista
tamanho_lista = int(input('Quantos números deseja avaliar?\n'))
numeros = []

while tamanho_lista != 0:
    print(f'Digite {tamanho_lista} numero(s)')
    numero = input(numeros.append(numero))
    numeros.append(numero)
    tamanho_lista = tamanho_lista - 1

print(f'O maior número foi {max(numeros)} e ele se repetiu {numeros.count(max(numeros))}')

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6] 
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
Se desempacotar em tamanhos diferentes gera ValueError
lista = [1, 2, 3]
num1, num2, num3, = lista

print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)
Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()  # cópia
print(nova)

nova.append(4)
print(lista)
print(nova)

Veja que ao utilizarmos .copy() copiamos da lista para uma nova lista, mas elas
ficaram totalmente independentes, ou seja, modificando uma lista, nao
nao afeta a outra. Isso é chamado de Deep Copy (Cópia Profunda)

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', '.', '.', '.']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

cores = ['azul', 'amarelo', 'vermelho']


# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista  # cópia
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados  da lista
# para a nova lista, mas ao realizar a modificação em uma das listas
# essa modificação se refletiu em ambas a listas, sendo chamado de
# Shallow Copy (Cópia Rasa)
"""
