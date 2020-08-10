"""
Programação orientada a objeto
Paradigma de programação (metodologia utilizada para pensar/desenvolver sistemas) que utilizada de mapeamento de objetos
do mundo real para modelos computacionais.
Classe tem atributos
Ex:
Classe -> Modelo do objeto do mundo real representado computacionalmente. Ex: Produto (Novo TIPO de dado)
Atributos -> Caracteristicas do objeto. Ex: Nome, preço, desconto
Métodos -> Comportamento do objeto. (Lembrar de funções)
    Construtor -> Método especial utilizado pra criar objetos
Objeto/instâncias: Elementos criados basiádos nas classes
"""

numero = 10
nome = 'Geek'
print(numero)
print(type(numero))
print(nome)
print(type(nome))


class Produto:
    pass


ps4 = Produto()
print(ps4)
print(type(ps4))
