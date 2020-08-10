"""
Questão 25 - Faça um programa para determinar a próxima jogada em um jogo da velha. Assumir que o tabuleiro é 3x3. A mat
rix pode conter -1 0 1, representando respectavemente uma casa contendo uma peça minha (-1), uma casa vvazia do tabuleir
o (0), e uma do meu oponente (1)

"""


# Condição de vitória na Vertical
def condicao_vitoria_vertical(matriz):
    if (matriz[0][0] == -1 and matriz[1][0] == -1 and matriz[2][0]) == -1:
        print('O jogador 1 ganhou')
        return True
    if matriz[0][1] == -1 and matriz[1][1] == -1 and matriz[2][1] == -1:
        print('O jogador 1 ganhou')
        return True
    if (matriz[0][2] == -1 and matriz[1][2] == -1 and matriz[2][2]) == -1:
        print('O jogador 1 ganhou')
        return True

    if (matriz[0][0] == 1 and matriz[1][0] == 1 and matriz[2][0]) == 1:
        print('O jogador 2 ganhou')
        return True
    if matriz[0][1] == 1 and matriz[1][1] == 1 and matriz[2][1] == 1:
        print('O jogador 2 ganhou')
        return True
    if (matriz[0][2] == 1 and matriz[1][2] == 1 and matriz[2][2]) == 1:
        print('O jogador 2 ganhou')
        return True


# Condições de vitória na Horizontal( Todas as linhas)
def condicao_de_vitoria_horizontal(tabuleiro):
    for i5 in range(3):
        if tabuleiro[i5] == [-1, - 1, -1]:
            print('O jogador 1 ganhou')
            return True

    for i2 in range(3):
        if tabuleiro[i2] == [1, 1, 1]:
            print('O jogador 2 ganhou')
            return True


# Condições de vitória na diagonal
def condicao_vitoria_diagonal(tabuleiro):
    if tabuleiro[0][0] == -1 and tabuleiro[1][1] == -1 and tabuleiro[2][2] == -1:
        print('O jogador 1 ganhou')
        return True
    if tabuleiro[0][0] == 1 and tabuleiro[1][1] == 1 and tabuleiro[2][2] == 1:
        print('O jogador 2 ganhou')
        return True
    if tabuleiro[0][2] == -1 and tabuleiro[1][1] == -1 and tabuleiro[2][0] == -1:
        print('O jogador 1 ganhou')
        return True

    if tabuleiro[0][2] == 1 and tabuleiro[1][1] == 1 and tabuleiro[2][0] == 1:
        print('O jogador 2 ganhou')
        return True


# Imprimindo o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for h1 in range(3):
        print(jogo_velha[h1])


def conferindo_se_ja_jogou(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        return True


jogo_velha = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tabuleiro_trocado = [[], [], []]
memoria_diagonal1 = 0
memoria_diagonal2 = 0

i = 0
while i != 10:
    if i == 0:
        print('O jogo se inicia pelo jogador 1, cujo cada lugar assinalado é convertido por 1, e logo após é a jogada'
              'do jogador 2, cujo local assilado é convertido por -1')
        imprimir_tabuleiro(jogo_velha)
        i = i + 1
    matriz_convertida = [[], [], []]
    jogada_linha = int(input('Digite em qual linha deseja jogar: '))
    jogada_coluna = int(input('Digite em qual coluna deseja jogar: '))
    jogo_velha[jogada_linha][jogada_coluna] = -1
    imprimir_tabuleiro(jogo_velha)
    if condicao_vitoria_vertical(jogo_velha):
        break
    if condicao_de_vitoria_horizontal(jogo_velha):
        break
    if condicao_vitoria_diagonal(jogo_velha):
        break
    jogada_linha = int(input('Digite em qual linha deseja jogar: '))
    jogada_coluna = int(input('Digite em qual coluna deseja jogar: '))
    jogo_velha[jogada_linha][jogada_coluna] = 1
    imprimir_tabuleiro(jogo_velha)
    if condicao_vitoria_vertical(jogo_velha):
        break
    if condicao_de_vitoria_horizontal(jogo_velha):
        break
    if condicao_vitoria_diagonal(jogo_velha):
        break
    i = i + 1
    if i == 10:
        'Deu velha'
