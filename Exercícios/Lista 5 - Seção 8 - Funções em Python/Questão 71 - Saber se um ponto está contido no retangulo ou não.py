"""
Questão 71 - Para representar um ponto em uma grade 2D, implemente uma função que indique se um ponto p está localizado
dentro ou fora de um retângulo. O retângulo é definido por seus vértices inferior esquerdo, v1 e superior direito, v2. A
função deve retornar 1 caso o ponto esteja localizado dentro do triângulo e 0 caso contrario.
"""
i = 0

def esta_dentro(v1, v2, coord_x1, coord_y1, coord_x2, coord_y2):

    if v1 > coord_x1:
        if v1 > coord_x2:
            return print('Está fora')

    if v2 > coord_y1:
        if v2 > coord_y2:
            return print('Está fora')

    if v1 < coord_x1:
        if v1 < coord_x2:
            return print('Está fora')

    if v2 < coord_y1:
        if v2 < coord_y2:
            return print('Está fora')

    return print('Está dentro')


while i != 10:
    x = int(input('Digite a coordenada x: '))
    y = int(input('Digite a coordenada y: '))
    esta_dentro(x, y, 1, 1, 4, 2)





