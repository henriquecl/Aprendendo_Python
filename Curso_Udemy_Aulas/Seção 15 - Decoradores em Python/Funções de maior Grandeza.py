"""
Funções de maior grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como resul
tado, ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar variáveis do tipo de
funções nos nossos programas.
OBS: Na seção de funções, nós utilizamos isso.
Em python, as funções são Cidadões de Primeira Classe, First Class Citizen

# Exemplo - Definindo as funções

def somar(a, b):
    return a+b

def diminuir(a, b):
    return a-b
def multiplicar(a, b):
    return a*b
def dividir(a, b):
    return a/b
def calcular(num1, num2, funcao):
    return funcao(num1, num2)
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, dividir))
print(calcular(4, 3, multiplicar))

# Nested Functions - Funções aninhadas
Em Python, podemos ter também funções dentro de funções, que são conhecidas como Nested Functions, ou também Inner Fun-
ctions.

# Exemplo
from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai', 'Sumas daqui', 'Gosto muito de você'))
    return humor() + ' ' + pessoa


print(cumprimento('João'))
print(cumprimento('PA'))

# Retornando funções de outras funções
from random import choice
def faz_me_rir():
    def rir():
        return choice(('KKKKKKKKKK', 'HAHAHAHAHA', 'kkk'))
    return rir
rindo = faz_me_rir()
print(rindo())
"""

# Inner Functions (Funções internas/Nested Functions) podem acessar o escopo de funções mais externas

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('KKKKKKKKKK', 'HAHAHAHAHA', 'kkk'))
        return f'{risada} {pessoa}'
    return dando_risada()


print(faz_me_rir_novamente('henrique'))