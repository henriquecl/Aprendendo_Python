"""
Questão 21 - Escreva uma função para determinar a quantidade de números primos abaixo de N
"""


def maior_primo(numero):
    divisores = []
    divisores_dos_multiplos = []
    i = 1
    j = 0
    j2 = 1
    while i <= numero:
        if numero / i == int(numero/i):  # Quer dizer que o número é multiplo
            divisores.append(i)
        i = i + 1
    while j <= len(divisores):
        while j2 <= divisores[j]:
            if divisores[j] / j2 == int(divisores[j]/j2):
                divisores_dos_multiplos.append(divisores[j])
                j = j + 1
                j2 = j2 + 1
    return divisores_dos_multiplos


print(maior_primo(33))
