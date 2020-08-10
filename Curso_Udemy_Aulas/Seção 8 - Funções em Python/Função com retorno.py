"""
Funções com retorno

OBS: Em Python quando uma função não retorna nenhum valor, o retorno é None
OBS: Função Python que retornam valores, devem retornar estes valores com a palavra reservada 'return'
OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução
da função para outras funções ou mesmo para o print.

# Exemplo 1 - Sem Retorno


def quadrado_de_7():
    print(7*7)

ret = quadrado_de_7()
print(ret)

# Exemplo 2- Vamos refatorar essa função pra ele retornar valor(refatorar = reescrever)


def quadrado_de_7_2():
    return 7*7


quadrado_de_7_2()
ret = quadrado_de_7_2()
print(ret)
# ou
print(quadrado_de_7_2())


# Refatorando a primeira função (aula definindo funções)

def diz_oi():
    return 'Oi '

alguem = 'Pedro!'
print(diz_oi() + alguem)

Observações sobre a palavra reservada return:

1.1 - Ela finaliza a função, ou seja, ela sai da execução da função;
1.2 - Podemos ter em uma função diferentes returns;
1.3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo multiplos valores;

# Exemplo 1.1 - Ela finaliza a função, ou seja, ela sai da execução da função;


def diz_oi():
    print('Estou sendo executado antes do retorno')
    return 'Oi!'
    print('Estou sendo executado após o retorno')
print(diz_oi())

# Exemplo 1.2 - Podemos ter em uma função diferentes returns;


def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
print(nova_funcao())

# Exemplo 1.3 -Podemos em uma função retornar qualquer tipo de dado e até mesmo multiplos valores;
def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

# ou
print(outra_funcao())


# Vamos criar uma função para jogar a moeda.

from random import random


def jogar_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(jogar_moeda())
"""

# Erros comuns na utilização do retorno, mas que na verdade nem é erro, mas sim codificação desnecessária


def eh_impar():
    numero = 81
    if numero % 2 != 0:
        return True
#    else:  nesse caso o else é desnecessário.
    return False


print(eh_impar())



