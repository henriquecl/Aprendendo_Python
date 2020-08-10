"""
Levantando os próprios erros com Raise

raise -> Lança exceções

OBS: O raise não é uma função, é uma palavra reservada assim como def, lambda...

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de error.

A forma geral de  utilização é:
raise TipoDoError('Mensagem de Error')

# Exemplo 1 -

def colore(texto, cor):
    if type(texto) != str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) != str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Banana', 2)

Exemplo 2 -
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) != str:
        raise TypeError('Texto precisa ser uma string')

    if type(cor) != str:
        raise TypeError('Cor precisa ser uma string')

    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Banana', 'rosa')

OBS: O raise assim como o return finaliza  a funçao, nada após o raise é executado.
"""
# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) != str:
        raise TypeError('Texto precisa ser uma string')

    if type(cor) != str:
        raise TypeError('Cor precisa ser uma string')

    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Banana', 'rosa')
