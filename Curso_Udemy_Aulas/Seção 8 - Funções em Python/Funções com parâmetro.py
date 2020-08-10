"""
Funções com parâmetro (De entrada)

- Funções que recebem dados para serem processados dentro da mesma.

Se a gnt pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gnt pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função


def quadrado(numero):
    return numero ** 2


num = int(input())
# se executar print(quadrado())  # TypeError
while num != 0:
    print(quadrado(num))
    num = int(input())

# Refatorando outra função

def cantar_parabens(aniversariante):
    print('Parabens pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}')


cantar_parabens('Henrique')

# OBS: Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada em uma função quantos parametros
# forem necessários, separando-os por vírgula. ONDE A ORDEM IMPORTA!


def soma(a, b):
    return a+b


def mutiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(mutiplica(4, 5))
print(mutiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Geek '))

# OBS: Se a gnt informar um número errado de parâmetro ou argumentos, teremos TypeError

# Nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Henrique', 'Campos'))

# A diferença entre Parâmetros e Argumentos.
# Parâmetros são as variáveis declaradas na definição de uma função.
# Argumentos são os dados passados durante a execução de uma função.

# A ordem dos parâmetros IMPORTA.
# Argumentos nomeados (Keyword Arguments), como se fossem dicionários
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qqr ordem
nome = 'Henrique'
sobrenome = 'Campos'

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome='Campos'))
print(nome_completo(sobrenome='Campos', nome='Henrique'))

"""

# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
#           return total, Se nós tivessemos colocando o return aqui, o return iria finalizar a função no 1º loop for.
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
