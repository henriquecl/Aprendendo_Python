"""
Objetos/Instância -> São instâncias de classe. Ou seja, as caracteristicas
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def liga_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Objetos / Instâncias
lamp1 = Lampada('branca', '110', '60')
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')
lamp1.liga_desliga()
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 20000)
user1 = Usuario('Henrique', 'Campos', 'kjdhasda@hotmailcom', 'senha')

