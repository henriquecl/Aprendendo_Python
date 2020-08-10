"""
Questão 9 - Receber altura e raio de um cilindro circular e retorne o volume
"""
import math


def volume_cilindro(altura, raio):
    volume = math.pi * (raio ** 2) * altura
    return volume


print(volume_cilindro(3, 1))
print(volume_cilindro(4, 5))



