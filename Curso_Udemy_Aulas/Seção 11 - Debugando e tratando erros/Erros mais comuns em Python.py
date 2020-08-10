"""
Erros mais comuns em Python

ATENÇÃO: É importante prestar atenção e aprender a ler as saidas de erros geradas pela execução do nosso código.

Os erros mais comuns:

SyntaxError -> Ocorre qnd o Python encontra um erro de sintaxe, ou seja, você escreveu algo que o Python não reconhece
como parte da linguagem.

# Exemplos de SyntaxError
a) def funcao:
        print('geek university')

b) None = 1

c) return

NameError -> Ocorre quando uma variável ou função não foi definida
# Exemplos NameError
a) print(geek)
b) while i != 0:  (sem definir o 'i')
    print('oi')
c) funcao()
d) a = 18       Como não entra no if a variável 'msg' não é criada
if a < 10:
    msg = 'É maior que 10'
print(msg)

TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.
# Exemplos TypeError
a) print(len(5))
b)print('Geek' + 4)

IndexError -> Ocorre quando tentamos acesar um elemento em uma lista ou outro tipo de dado indexado utilizando um indice
invalido
# Exemplos IndexError
a)lista = ['Geek']      Acessar elemento q não existe
print(lista[1])

ValueError -> Ocorre quando uma função/operação built-in recebe um argumento com tipo correto mas valor inapropriado
# Exemplos ValueError
a) print(int('Geek'))

KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.
# Exemplos KeyError
a) dic = {'geek': 'University'}
print(dic['outrachave'])

AttributeError -> Ocorre quando uma variável não tem um atributo/função
# Exemplos AttributeError
a)tupla = (9, 2, 19, 4)     Não existe o
print(tupla.sort())

IndentationError -> Ocorre quando não respeitamos a identação do Python (4 espaços)
# Exemplos IndentationError
a)def nova():
print('Geek')
b) for i in range(10):
print('oi')


OBS: Exception e Erros são sinonimos na programação.
OBS: Importante ler e prestar atenção na saída de error.
"""
