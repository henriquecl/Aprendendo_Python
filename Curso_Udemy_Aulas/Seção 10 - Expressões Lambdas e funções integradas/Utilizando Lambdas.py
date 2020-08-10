"""
Utilizando Lambdas

Conhecidas por expressões Lambdas, ou simplesmente Lambdas, são função sem nomes, ou seja, funções anônimas.

# Relembrando função em Python
def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

# Exemplo de expressão Lambda
lambda x: 3 * x + 1
# E como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))


# Podemos ter expressão lambdas com múltiplas entrada
# Title deixar a primeira letra em caixa alta
# Strip tira os espaços do inicio e do fim de uma string, não do meio
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' angelina ', 'JOLIE'))
print(nome_completo(' henrique ', 'CaMpoS              '))

# Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas também.
amar = lambda: 'Como não amar python?'
uma = lambda x: 3*x + 1
duas = lambda x, y: (x*y) **0.5
tres = lambda x, y, z: 3/(1/x+1/y +1/z)
# n = lambda x1, x2, ..., xn <expressão>
print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

# Outro exemplo (Exemplo correto de utilizar o Lambda
autores = ['Isaac Asimov', 'Ray Bradbury', 'Monteiro Lobato', 'Ruth Rocha', 'Dimas o Primeiro', 'Arthur C. Clarke']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
"""
# Função quadratica
# f(x) = a * x ** 2 + b * x + c

# Definindo a função


def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a*x**2 + b*x + c"""
    return lambda x: a*x **2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

# Aplicações de Lambdas
