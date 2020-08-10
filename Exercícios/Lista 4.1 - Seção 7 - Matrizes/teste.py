
matriz = [[-1, 0, 0], [-1, 0, 0], [-1, 0, 0]]


def condicao_vitoria_vertical(matriz):
    if (matriz[0][0] and matriz[1][0] and matriz[2][0]) == -1:
        print('O jogador 1 ganhou')
    if matriz[0][1] and matriz[1][1] and matriz[2][1] == -1:
        print('O jogador 1 ganhou')
    if (matriz[0][2] and matriz[1][2] and matriz[2][2]) == -1:
        print('O jogador 1 ganhou')

    if (matriz[0][0] and matriz[1][0] and matriz[2][0]) == 1:
        print('O jogador 2 ganhou')
    if matriz[0][1] and matriz[1][1] and matriz[2][1] == 1:
        print('O jogador 2 ganhou')
    if (matriz[0][2] and matriz[1][2] and matriz[2][2]) == 1:
        print('O jogador 2 ganhou')




condicao_vitoria_vertical(matriz)