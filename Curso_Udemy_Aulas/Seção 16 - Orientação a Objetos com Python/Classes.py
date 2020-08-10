"""
Classes -> Em POO, nada mais são do que modelos dos objetos do mundo real sendo representado computacionalmente, podendo
ser interpretado como um novo tipo de dado.

Imagine que você queira fazer um sistema pra automatizar o controle das lampadas da sua casa.

Classes podem conter:
    Atributos -> Representam as caracteristicas do objeto, ou seja, pelos atributos conseguimos representar computacio-
nalmente os estados de um objeto. No caso da lâmpada, possivelmente iriamos querer saber se a lampada é 110 ou 220V, se
é branca, amarela, vermelha ou outra cor, qual a luminosidade dela, etc...

    Métodos (funções) -> Representam os compuortamentos do objeto, ou seja, as ações que esse objeto pode realizar no
seu sistema. No caso da lampada, por exemplo, é o de ligar e desligar a mesma.

Em python, para definir uma classe, utilizamos a palavra reservada ''class''.
Obs: Utilizamos a palavra ''pass'' em Python quando temos um bloco de código que ainda não está implementado.
Obs: Quando nomeamos nossas classes em Python, utilizamos por convenção o nome com inicial em Maiuscúlo. Se o nome for
composto, utiliza-se as iniciais de ambas as palavras em maiúsculo todas juntas.

Dicas Geek: Em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares para nomes de classes,
atributos, métodos, arquivos, diretórios e etc...

Obs: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos
que serão mapeados para classes de entidades.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


lamp = Lampada()
print(type(lamp))
