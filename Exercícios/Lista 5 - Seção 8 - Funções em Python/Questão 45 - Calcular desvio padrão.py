"""
Questão 45 - Faça uma função que calcule o desvio padrão de um vetor v contendo n números


fórmula: DP=sqt(1/n-1)* somatório n   (  v[i] - m)^2
                                i = 1
"""
import math


def devio_padrao(v):
    primeiro_termo = 1/(len(v)-1)
    media_do_vetor = sum(v)/len(v)
    somatorio = 0
    i = 0
    while i < len(v):
        segundo_termo = (v[i] - media_do_vetor)**2
        somatorio = somatorio + segundo_termo
        i = i + 1
    desvio_padrão = (primeiro_termo*somatorio) **(1/2)

    return media_do_vetor, primeiro_termo, somatorio, desvio_padrão


lista = [1.55, 1.70, 1.80]
print(devio_padrao(lista))

