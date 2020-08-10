"""
Questão 5 - Faça uma função e um programa de teste para o cálculo do volume de uma esfera. Sendo o raio passado por pa-
râmetro.

V = 4/3 * pi * R³
"""
import math


def volume_esfera(diametro):
    volume = (4/3) * math.pi * (diametro/2)
    return volume


print(volume_esfera(1))
print(volume_esfera(3))
print(volume_esfera(4))
