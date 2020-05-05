"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que comece
com asterisco


Exemplo:
*xis
Mas por convenção, utilizamos *args para defini-lo.

O parâmetro *args utilizado em uma função, coloca os valores extras informados como uma entrada em uma tupla. Então, des
-de já, lembre-se que tuplas são imutáveis. Ou seja, podemos interpreta-lo como valores de entrada infinitos, não sendo
necessário amarrar quantas entrada nos teremos na função. Ao utilizar o *args podemos ter quantas entradas forem nece-
ssarias na função sem necessáriamente declara-las


# Ex 1
Se a cada vez fosse adicionado um novo numero na soma, iriamos ter que aumentar a função cada vez mais, ou seja, péssimo
def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))

# Entendendo o args

def soma_todos_numeros(nome, email, *args):
    return sum(args)


print(soma_todos_numeros('Henrique', 'Campos'))
print(soma_todos_numeros('Henrique', 'Campos', 1))
print(soma_todos_numeros('Henrique', 'Campos', 2, 3))
print(soma_todos_numeros('Henrique', 'Campos', 2, 3, 4))
print(soma_todos_numeros('Henrique', 'Campos', 3, 4, 5, 6))

# Exemplo de utilização do *args
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-Vindo Geek'
    return 'Eu não sei quem você é...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

"""


def soma_todos_numeros(*args):
    print(args)
    return sum(args)


# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador
print(soma_todos_numeros(*numeros))
# O asterisco serve para que informemos ao python que estamos passando como argumento uma coleção de dados. Dessa forma,
# ele saberá que precisará antes desempacotar os dados contidos. Só não funciona com dicionário



