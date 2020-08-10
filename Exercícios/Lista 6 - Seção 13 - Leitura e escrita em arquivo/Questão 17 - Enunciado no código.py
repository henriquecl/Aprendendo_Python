"""
Questão 17 - Faça um programa que leia um arquivo que contenha as dimensões de uma matriz (linha x coluna), a quantida
de de posições que serão anuladas, e as posições a serem anuladas.
O programa lê esse arquivo, e em seguida, produz um novo arquivo com a matriz com as dimensões dadas no arquivo lido, e
todas as posições especificadas no arquivo ZERADAS e o restante recebendo valor 1.
3 3 2 / 3 tamanho de linhas, 3 tamanho de colunas, 2 posições a serem anuladas
1 0 / posição a ser anulada
1 2 / posição a ser anulada
"""


def lista_em_int(lista, lista_inteiro):
    """
    :param lista: Tem uma lista como entrada
    :param lista_inteiro: A lista de sáida
    :return: Converte os itens que estão contidos na lista de 'str' para 'int' se forem APENAS números.
    """
    for i in range(len(lista)):
        lista_inteiro.append(int(lista[i]))
    return lista_inteiro


def matriz_tamanho_usuário(matriz, tamanho):
    """
    :param matriz : A matriz cuja você deseja criar
    :param tamanho: Tamanho da matriz desejada pelo usuário
    :return: Uma matriz do tamanho que o usuário desejar
    """
    for i in range(tamanho):
        matriz.append([])


def preenche_matriz(matriz):
    """
    Essa função preenche todos os itens de uma matriz por 1
    :param matriz: Matriz que deseja ser preenchida
    :return: None
    """
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i].append(1)


matriz_nova = []
with open('matrix.txt', 'r', encoding='UTF-8') as arquivo:
    linha0 = arquivo.readline()
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()

# Convertendo todas as linhas em lista, e depois em lista de inteiros
tamanho_matrix = linha0.split()
anula_1 = linha1.split()
anula_2 = linha2.split()
tamanho_matrix_inteiro = []
anula_1_inteiro = []
anula_2_inteiro = []
lista_em_int(tamanho_matrix, tamanho_matrix_inteiro)
lista_em_int(anula_1, anula_1_inteiro)
lista_em_int(anula_2, anula_2_inteiro)

# Criando uma matrix do tamanho digitado pelo usuário
matriz_tamanho_usuário(matriz_nova, tamanho_matrix_inteiro[0])

# Preenchendo a matriz com numeros 1
preenche_matriz(matriz_nova)

# Substituindo pelos valores desejados
matriz_nova[anula_1_inteiro[0]][anula_1_inteiro[1]] = 0
matriz_nova[anula_2_inteiro[0]][anula_2_inteiro[1]] = 0


a = str(matriz_nova)

# Criando um novo arquivo com a matriz_nova

with open('questao17.txt', 'w', encoding='UTF-8') as arquivo2:
    arquivo2.write(a)






