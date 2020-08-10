"""
Atributos -> Representam as caracteristicas do objeto. Ou seja, conseguimos representar computacionalmente os estados de
um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - de Instância
    - de Classe
    - Dinâmicos

Atributos de instância: São atributos declarados dentro do método construtor.
Obs: Método construtor é um método especial utilizado para a construção do objeto.

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público. Ou seja, pode ser acessado em to
do o projeto. Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser
acessado/utilizado somente dentro da própria classe onde está declarado, utiliza-se __ duplo underscore no inicio de seu
nome. Isso é conhecido também como Name Mangling


O que significa atributos de instância?

Quer dizer que, ao criarmos instâncias/obejetos de uma classe, todas as instâncias terão estes atributos.

user1 = Acesso('dlasjkdsa@hotmail.com', '02938')
user2 = Acesso('dadsa@gmail.com', '127321')

user1.mostra_email()
user2.mostra_email()
"""

# Classe com Atributo de Instância Publico
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo





class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senho = senha


# Classe com Atributo de Instância Privado
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_email(self):
        print(self.email)

# Lembre-se que isso é apenas convenção, a linguagem não irá impedir de que façamos acesso dos atributos fora da classe.


user = Acesso('user@gmail.com', '12382')
print(user.email)
# print(user.__senha)     # AttributeError
print(user._Acesso__senha)  # Temos acesso, mas não deveriamos faze-lo (Name Mangling)
print(dir(user))

"""
Atributos de classe -> São atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente
já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe, ou seja, ao invés de cada
instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos de classe, tod
as as instâncias terão o mesmo valor para esse atributo.
"""


class Produto:
    # Atributo de classe
    imposto = 1.05 #  0.05% de imposto
    contador = 0
    # Atributos de instância
    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto('Play4', 'video game', 2300)
p2 = Produto('Xbox S', 'video game', 4500)

print(p1.valor)  # Acesso possivel, mas incorreto de um atributo de classe.
print(p2.valor)  # Acesso possivel, mas incorreto de um atributo de classe.


# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe.
print(Produto.imposto)  # Acesso correto de um atributo de classe
print(p1.id)
print(p2.id)

"""
Atributos dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução.
Obs: O atributo dinâmico será exclusivo da instância que o criou.
"""

p1 = Produto('Play4', 'video game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

p2.peso = '5kg'  # Note que na classe produto não existe o produto peso.

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor:{p2.valor}, Peso:{p2.peso}')
# Exibindo todos os Atributos dinâmicos de uma Classe
print(p1.__dict__)
print(p2.__dict__)

# Deletando Atributos

del p2.peso
print(p2.__dict__)
