"""
Documentando funções com Docstrings
OBS: Podemos ter acesso a documentação de uma função em Python utilizando a propriedade especial __doc__

Podemos ainda fazer acesso a documentação com a função help()

"""


def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'


print(diz_oi.__doc__)
help(diz_oi)


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' ** potencia informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial, por padrão 2
    :return: Retorna o exponencia de 'numero' por 'potencia'
    """
    return numero ** potencia


print(exponencial.__doc__)
