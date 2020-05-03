"""
Definindo Funções:

- Funções são uma pequena parte de nosso código que realizam uma tarefa específica;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela é bom fazer uma verificação para que a função
seja simplificada.

Já utilizamos várias funções desde que iniciamos esse curso:
- print(); len(); max(); min(); sort(); count()

"""

# Exemplo de utilização de funções:

# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()



# curso = 'Programação em Python: Essencial'


# cores.append('roxo')

#  curso.append('Mais dados....')  #AtributeError
#  print(curso)

# cores.clear()
# print(cores)

# print(help(print))
# DRY - Don't Repeat Yourself

# Mas então, como definir funções?

"""
Em Python, a forma geral de definir uma função é:

def nome_da_função(parametros_de_entrada):
    bloco_da_funcao
    
Onde: 

nome_da_função -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separador por virgula, podendo ser opcionais ou não
bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função utilizamos a palavra reservada 'def' informando ao Python que estamos definindo
uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é utilizado em Python para definir
blocos
    
    
"""

# Definindo a primeira função

# Definição


def diz_oi():
    print('Oi!')


diz_oi()


"""
OBS:
1- Veja que,dentro da nossas funções podemos executar outras funções;
2- Veja que nossa função só executa uma tarefa, ou seja, a única coisa q ela faz é dizer oi
3- Veja que essa função não recebe nenhum parâmetro de entrada;
4- Veja que essa função não retorna nada;
"""

# Chamada de execução
# ATENÇÃO: NUNCA ESQUEÇA DE UTILIZAR O PARENTESES AO EXECUTAR UMA FUNÇÃO.
# Ex: diz_oi - errado. diz_oi() - certo

# Exemplo 2


def cantar_parabens():
    print('Parabens pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva ao aniversariante')


# for i in range(4):
#   cantar_parabens()

# Em Python podemos inclusive criar variáveis do tipo de uma função e executar essa função através da variável.
# Serve pra nada '-'


canta = cantar_parabens

canta()

