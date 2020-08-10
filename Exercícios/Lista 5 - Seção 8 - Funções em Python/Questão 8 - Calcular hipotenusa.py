"""
Questão 8 - Calcular hipotenusa
"""
import math


def hipotenusa(cateto1, cateto2):

    hip = math.sqrt(cateto1**2 + cateto2**2)
    return hip


print(hipotenusa(1, 1))
print(hipotenusa(3, 4))
print(hipotenusa(9, 9))

