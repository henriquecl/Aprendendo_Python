"""
Conjuntos

- Conjuntos em qlqr linguagem de progração estamos fazendo referencia à Teoria dos Conjuntos da matemática

- Aqui no Python os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índices, ou seja, conjuntos não são indexados;

 Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os Sets são referenciados em Python com chaves {}

Diferença entre conjuntos (Sets) e mapas (dicionários).
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor.

# Definindo um conjuntos

# Forma 1 - Mais comum

s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print(s)
print(type(s))

# Forma 2

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos
print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erros e não
# fará parte do conjunto

# Verificando se o elemento esta contido no conjunto
if 13 in s:
    print('Tem o 13')
else:
    print('Não tem o 13')



# Importante lembrar que, além de não termos valores duplicados, não temos ordem, ou seja, não irá imprimir na ordem que
# foram inseridos


lista = [99, 2, 34, 23, 12, 1, 44, 5, 44]
print(lista, len(lista))


tupla = (99, 2, 34, 23, 12, 1, 44, 5, 44)
print(tupla, len(tupla))


dicionario = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 44], 'dict')
print(dicionario, len(dicionario))

s = {99, 2, 34, 23, 12, 1, 44, 5, 44}
print(s, len(s))

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente

for valor in s:
    print(valor)

# Usos interessantes com Sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu, e os visitantes informaram manual-
# mente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição

cidades = ['Recife', 'Recife', 'Recife', 'Recife', 'São Paulo', 'Cuiabá', 'Belo Horizonte', 'São Paulo', 'Manaus']
print(cidades)
cidades_unicas = set(cidades)
print(f'Fomos visitados por {len(cidades)} pessoas de {len(cidades_unicas)} lugares diferentes')

# Adicionando elementos em um conjunto

s = {1, 2, 3}
print(s)
s.add(4)
s.add(4)  # Duplicidade não gera erro, simplesmente é ignoradoe não é adicionado.
print(s)

# Remover elementos em um conjunto
# Não retorna nenhum valor removido em nenhuma das duas formas
s = {1, 2, 3}
print(s)
# Forma 1 - Caso o valor não seja encontrado será gerado o error KeyError.
s.remove(3)  # NÃO é indice! Informamos o valor
print(s)

# Forma 2 - Caso o valor não seja encontrado nada acontece.
s.discard(2)
print(s)

# Copiando um conjunto para outro... SHALLOW COPY E DEEP COPY (PADRÃO)

# Podemos remover todos os itens de um conjunto
s = {1, 2, 3}
s.clear()

# Métodos Matemático de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e outro estudantes do curso de Java

est_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
est_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando Union , lembrando q a ordem da união não importa

estudantes = est_java.union(est_python)
print(estudantes)

# Forma 2 - Utilizando o caractere pipe |

estudantes1 = est_python | est_java
print(estudantes1)

# Gerar um conjunto de estudante que estão em ambos os cursos (interseção)

# Forma 1 - Utilizando intersection

ambos = est_python.intersection(est_java)
print(ambos)

# Forma 2 - Utilizando o &

ambos1 = est_java & est_python
print(ambos1)

# Gerar um conjunto de estudantes que não estão no outro

so_python = est_python.difference(est_java)
print(so_python)
so_java = est_java.difference(est_python)
print(so_java)

# Soma*, Valor Máximo*, Valor mínimo*, Tamanho.
# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))


"""



