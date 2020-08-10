"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada. Temos que importar e utilizar esta função
a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso, 99% das vezes um loop for é
mais legivel.

Para entender o reduce()

Imagine que você tem uma coleção de dados:
dados = [a1, a2, a3, ..., an]
E você tem uma função que recebe dois parametros:

def funcao(x,y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável
reduce(função, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 =  f(a1, a2)  # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo 2: res2 =  f(res1, a3) # Aplica a função passando o resultado do passo 1 mais o 3º elemento e guarda o result
    Passo 3: res3 =  f(res2, a4) # Aplica a função passando o resultado do passo 3 mais o 4º elemento e guarda o result
    Isso é repetido até o final.

Ou seja, em cada passo ela aplica a fnução passando como primeiro elemento o resultado da aplicação anterior. No final,
reduce() irá retornar o valor final.

Alternativamente poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4),...), an)
"""
from functools import reduce

# Na prática - Usando a função reduce para multiplicar todos os números de uma lista

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce nós precisamos de uma função que receba dois parametros

res = reduce(lambda x, y: x * y, dados)
print(res)

# Utilizando um lood normal
res2 = 1

for n in dados:
    res2 = res2 * n

print(res2)
