"""
Tuplas (tuple)

Tuplas são bastante parecidas com as listas.

Existem basicamente duas diferenças:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são IMUTÁVEIS: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla, gera uma
nova tupla.

# Cuidado 1 : As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Cuidado 2 : Tuplas com 1 elemento NÃO É TUPLA.

tupla3 = (4)
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))

# Podemos concluir então que tuplas são definidas pela virgulas, e não pelo uso do parenteses.
(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)


# Desempacotamento de tupla - Tem q ter o msm número de variaveis para elementos na lista e vice-versa
tupla = ('Geek Univeristy', 'Programação em python: Essencial')
escola, curso = tupla
print(escola, curso)

# Método para adição e remoção de elementos nas tuplas não existe, dado o fato das tuplas serem imutaveis

# Soma*, Valor maximo*, Valor mínimo* e tamanho: Válidos iguais ao das listas

# *Se forem inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas: Não alteram as tuplas, logo é possivel realiza-las

tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = (4, 5, 6)
print(tupla2)
print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

tupla1 = tupla1 + tupla2  # TUplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento está na tupla
tupla = (1, 2, 3)
print(33 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('z'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))


# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos mudar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[2])

# Iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Exemplo 2
# Verificando em qual indice o elemeneto está na tupla
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')


                (item  , a partir de)
print(meses.index('Junho', 4))  # Obs: Caso o elemento não exista será gerado um ValueError

# Slicing
# Exemplo 3

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')

print(meses[5::2])


# Por quê utilizar tuplas?

- Tuplas são mais rápidas do que listas
- Deixa seu código mais seguro, isso por que trabalhar com elementos imutáveis traz segurança para o código

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)
nova = tupla  # Na tupla não temos o problema de Shallow Copy
print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra
print(nova)
"""


