"""
Questão 14 - Faça uma fução que receba a distância em Km e a quantidade de litros de gsolina consumidos pelo carro em um
percurso. Calcule o Km/l e escreva uma msg com a tabela abaixo
"""


def autonomia_veiculo(km_percorridos, litros):
    autonomia = km_percorridos / litros
    if autonomia <= 8:
        return 'Venda o carro'
    elif 8 < autonomia <= 12:
        return 'Econômico'
    return 'Super econômico'


print(autonomia_veiculo(70, 10))
print(autonomia_veiculo(100, 10))
print(autonomia_veiculo(150, 10))
