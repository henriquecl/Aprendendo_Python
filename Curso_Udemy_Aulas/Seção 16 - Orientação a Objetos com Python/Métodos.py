"""
Métodos (funções) -> Representam os comportamentos dos objeto. Ou seja, as ações que esse objeto pode realizar no seu
sistema.

Em Python, dividimos os métodos, assim como atributos em 2 grupos:
    - de Instância
    - de Classe

# Métodos de Instância

O método dunder init __init__ é um método especial chamado de construtor e sua função é construir um objeto a partir da
classe.
Obs: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline).

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder, não é aconselhado. Python possui vários
métodos com essa forma de nomenclatura e pode ser que mudemos o comportamento dessas funções mágicas internas da lingua-
gem, então, não utilize.

Métodos são escritos com letras minúsculas, se for composto separa por underline.

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere')
    exit(1)

print('Usuário criado com sucesso!')
senha = input('Informe a senha para acesso:')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')


Métodos de Classe:
"""
from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador+1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema.')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


