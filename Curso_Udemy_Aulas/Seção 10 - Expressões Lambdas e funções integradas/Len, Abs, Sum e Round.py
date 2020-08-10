"""
Len, Abs, Sum e Round

Len -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

Só pra revisar - Len
print(len('Geek University'))
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print((len(range(0, 10))))
# Por debaixo dos panos, quanto utilizamos a função len() o Python faz o seguinte:
# Dunder len
print('Geek University'. __len__())

Abs -> Retorna o valor absoluto de um número real. De forma básica, seria o módulo de um número.
# Exemplos abs
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

Sum -> Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna o valor da soma total dos elementos
incluindo o valor inicial.
Obs: O valor inicial default é 0
-------- Exemplos sum ------------
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

Round -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão nao for estabelecida
retorna o inteiro mais próximo da entrada.
-------- Exemplos Round ------------
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(11.5))
print(round(1.21212121, 2))
print(round(1.2199999, 2))
"""

