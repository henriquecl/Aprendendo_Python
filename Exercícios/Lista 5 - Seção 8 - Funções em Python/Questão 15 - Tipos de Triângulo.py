"""
Questão 15 - Crie um programa que receba 3 valores (obrigatoriamente maiores que zero), representando 3 lados de um
triangulo

a) Determinar se esses lados formam um triangulo:
    O comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados
b) Mostrar o tipo de triangulo:
    Equilátero - 3 lados iguais
    Isósceles - 2 lados iguais
    Escaleno - 3 lados diferentes
"""


def triangulo(lado1, lado2, lado3):
    if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
        return 'Não é triângulo'
    if lado1 == lado2 == lado3:
        return 'Triângulo Equilátero'
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return 'Triângulo isósceles'
    return 'Triângulo escaleno'


for i in range(99):
    primeiro_lado = int(input('Digite o primeiro lado:'))
    segundo_lado = int(input('Digite o primeiro lado:'))
    terceiro_lado = int(input('Digite o primeiro lado:'))
    print(triangulo(primeiro_lado, segundo_lado, terceiro_lado))

