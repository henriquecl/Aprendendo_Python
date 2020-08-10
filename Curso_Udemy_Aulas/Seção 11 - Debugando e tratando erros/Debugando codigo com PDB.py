"""
Debugando com PDB
PDB -> Python Debugger

------------------- Exemplo de prática ruim -------------------

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorrou o problema: {err}'
print(dividir(4, 7))
# OBS: A utilização do print() para debuggar código é  uma prática ruim.

# Existem formar mais profissionais de se fazer esse 'debug', utilizando o debugger.
# Em Python, podemos fazer isso em diferentes IDE's, como o Pycharm ou o PDB

# Exemplo com o Pycharm
def dividir(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorrou o problema: {err}'
print(dividir(4, 0))
"""

# Exemplo com o PDB - Python Debugger
# Para utilizar o PDB, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
# Comandos básicos do PDB
# l (listar onde estamos no código), n (proxima linha), p(imprime variável), c (continua a execução e finaliza o debbug)
# A partir do Python 3.7, não é mais necessario importar a bib, pois o debug foi incorporado como buil-in. basta escre
# ver breakpoint() e utilizar os comandos padrão  do PDB
import pdb
nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
