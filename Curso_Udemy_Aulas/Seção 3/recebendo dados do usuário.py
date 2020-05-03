# Entrada de dados
# TODO dado recebido via input é string
# Em python, string é tudo que estiver entre '' ," ", ''' '''', """ """
# ex: 'angelina', "angelina, '''angelina''', """angelina"""

# Recebendo de maneira antiga
# print("Qual seu nome? ")
# nome = input()

nome = input('Qual seu nome?')

# Exemplo de print da versão antiga do python
# print('Seja bem-vindo(a) %s' % nome)

# Ex print mais moderno
# print('Seja bem-vindo(a){0}'.format(nome))


# Ex de print atual
print(f'Seja bem vindo(a) {nome}')

# Recebendo de maneira antiga
# print("Qual sua idade?")
# idade = input()

idade = int(input('Qual sua idade?'))

# Processamento

# Exemplo de print da versão antiga do python
print(f'O {nome} tem {idade} anos e nasceu em {2020-idade}')

