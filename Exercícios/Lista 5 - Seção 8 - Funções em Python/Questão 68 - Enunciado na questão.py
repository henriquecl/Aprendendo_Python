"""
Questão 68 - Faça uma função que receba duas strings. E retorne a intercalação letra a letra da primeira com a segunda
string. A string intercalada deve ser retornada na primeira string.
"""


def codigo(str1, str2):
    string_aux = ''
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        string_aux = string_aux + str1[i] + str2[i]
        i = i + 1
        j = j + 1
    str1 = string_aux
    return str1


print(codigo('vamos escreverlkjljlkj por código? que tal', 'desenvolvendo um novo código para o anv dela'))