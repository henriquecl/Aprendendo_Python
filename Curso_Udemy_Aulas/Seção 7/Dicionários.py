"""
Dicionários (dict)

OBS: Em algumas linguagens de programação os dicionários Python são conhecidos por mapa.

Dicionários são coleções do tipo chave/valor.
OBS: Nas listas e tuplas a chave fica omitida. Só vemos os valores.

Dicionários são representados por chaves {}.
OBS: Tanto a chave quanto o valor podem ser de qualquer tipo, podendo ser até misturados
dict = {'chave': 'valor', 'chave2': 'valor2'}

# Criação de dicionários
# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])
# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - RECOMENDADO

print(paises.get('br'))
print(paises.get('ru'))
# Nesse caso, ao tentarmos acessar uma chave que não existe, retornará None.
# O tipo None sempre é especificado com letra maiúscula
# Bom para iniciar variáveis que não saberemos que tipo ele será
# O tipo None sempre retornará False

Ex1:
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

russia = paises.get('ru')

if russia:
    print(f'Encontrei o país {russia}')
else:
    print('Não encontrei o país')

Ex2:
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
                   (chave, valor padrão caso não encontre)
russia = paises.get('py', 'Não encontrado')

print(f'Encontrei o país {russia}')


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# Podemos verificar se determinada chave se encontra no dicionário: (chave in dicionário)
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive:lista, tupla, dicionário como chaves.
# Tuplas por exemplo são bastante interessantes de serem utilizadas como chaves de dicionários, pois as mesma não mudam

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (35.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 - Mais comum
receita['abr'] = 350
print(receita)

# Forma 2 - Menos comum

novo_dado = {'mai': 500}
receita.update(novo_dado)  # receita.update({'mai':500})
print(receita)

# Atualizando dados em um dicio´nário

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai': 600})
print(receita)

# CONCLUSÕES
# 1 - A forma de adicionar novos elementos ou atualiza-los em um dicionário é a mesma.
# 2 - Em dicionários, NÃO podemos ter chaves repetidas. Se passar a mesma chave o valor do elemento sera sobrescrito

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
# Forma 1 - Mais comum
ret = receita.pop('mar')
print(ret)
print(receita)
# OBS: Nesse caso é obrigatório informar a chave, e caso não encontre o elemento um KeyError é retornado.
# Obs2: Ao removermos um objeto o valor deste objeto é sempre retornado

# Forma 2 - Menos comum
del receita['fev']

print(receita)
# Nesse caso não retorna o valor que foi removido se ele existir
# Se a chave não existir será gerado um KeyError

"""

# Imagine que você tem um comercio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.
"""
Carrinho de compras:
    Produto1:
        -nome;
        -qtd;
        -preço;
    Produto2:
        -nome;
        -qtd;
        -preço;
        
# Forma 1, utilizando listas - Poderíamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playstation4', 1, 2300.00]
produto2 = ['God of war 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto.

# Forma 2- Poderiamos utilizar uma tupla para isso? Sim.

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of war 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto novamente.

# Forma 3 - Poderiamos utilizar um dicionário para isso? Sim
carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300}
produto2 = {'nome': 'God of war 4', 'quantidade': 1, 'preço': 150}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Dessa forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza
# sobre cada informação

# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

print(d)


# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

Limpar o dicionário/qualquer coisa que tenha
d.clear()
print(d)

opiando um dicionário para outro

Forma 1 - Deep Copy

novo = d.copy()
print(novo)

novo['d'] = 4
print(d)
print(novo)

Forma 2 - Shallow Copy

novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)


"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
# OBS:                  [cada coisa daqui vira uma chave]   , virou um valor para a chave
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável e uma chave, e irá atribuir a essa chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)
# Note que não existe a repetição de chave.

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
