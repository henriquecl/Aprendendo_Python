"""
Listas aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java/Php) possuem uma estrutura de dados chamada de arrays
    - Unidimensionais (Arrays/vetores);
    - Multidimensionais (Matrizes);


Em Python nós temos as listas.

numeros = [1, 2, 3, 4, 5]  aqui são listas, nas outras são arrays


# Exemplo

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Lista de listas, ou seja, uma matriz
#          LINHA0      LINHA1     LINHA2

print(listas)
print(type(listas))

# Como fazemos para acessar os dados?
#          [linha] [coluna]
print(listas[0][1])  # 2
print(listas[2][1])  # 8

# Iterando com loops em uma lista aninhada
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

"""

# Outros exemplos:

# Gerando uma matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1,4)])
