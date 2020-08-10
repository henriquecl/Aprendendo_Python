"""
Funções com parametro padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;
 Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')
print()


def exponencial(numero , potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva a potencia informada pelo usuário

# OBS: Se o usuário passar somente um parâmetro, esse será atribuido ao parametro, número, e será calculado o ² do nume
# ro, se o usuário passar 2 argumentos, o primeiro será atribuido ao numero, e o segundo a potência
print(exponencial())

# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM estar ao final da declaração.
# ERRO!


def teste(potencia, num=2):
    return num ** potencia


print(teste(6))

# Outros exemplos
def soma(num1, num2):
    return num1 + num2
print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())   # TyperError



# Exemplo mais complexto

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))



# Por quê utilizar parâmetros com valor default?
- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código


# Quais tipos de dados podemos utilizar como valores default para parâmetros?
- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc....


# Exemplos

def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões
# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = 'Python'    # Variável local
    return f'Oi {instrutor}'


print(diz_oi())

# OBS: Se tivermos uma variável local com o msm nome de uma global, a local terá preferencia

def diz_oi():
    prof = 'Geek'   # Variável local
    return f'Olá {prof}'


print(diz_oi())
print(prof)         # NameError

# Atenção com variáveis globais (se puder evitar, evite)
total = 0


def incrementa():
    total = total + 1   # UnboundLocalError (A variavel local está sendo utilizada sem ter sido iniciada
    return total
print(incrementa())

# Modo correto
total = 0
def incrementa():
    global total        # Avisando que queremos utilizar a variável global

    total = total + 1   # UnboundLocalError (A variavel local está sendo utilizada sem ter sido iniciada
    return total


print(incrementa())
print(incrementa())
"""

# Podemo ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador       # O não local é utilizado para inicializar uma variável de função externa
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())
print(fora())
print(fora())
# print(dentro())     # NameError
