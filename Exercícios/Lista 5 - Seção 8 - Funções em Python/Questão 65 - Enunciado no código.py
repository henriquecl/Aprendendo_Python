"""
Questão 65 - Implemente uma função a qual recebe duas strings. E um valor inteiro N. A função não concatena mais que N
caracteres da string apontada por str2 à str1.
"""


def concatenar_controlado(str1, str2, num):
    i = 0
    palavra = ''
    while i < num and i < len(str2):
        palavra = palavra + str2[i]
        i = i + 1
    return str1 + palavra


print(concatenar_controlado('Eu gosto de banana', ' e de lapis', 129))



