"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função built-in open()

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que nesse caso é o caminho
do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

OBS: Por padrão, a função open() abre o arquivo para leitura. Esse arquivo deve existir, ou então teremos o error:
FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
                                    read()
A função read() lê todo o conteúdo de um arquivo.
"""
# Exemplo
arquivo = open('texto.txt', encoding='UTF-8')
#                                   UTF-8 para ter acento, cp1252 não pega acento
# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()
ret = arquivo.read()
print(type(ret))
print(ret)

"""
OBS: Ao tentar ler pela segunda vez não funciona, assim como mapas, filter, etc...
O Python utiliza um recurso para trabalhar com arquivos chamada cursor. Esse cursor funciona como o cursor quando esta-
mos escrevendo. Só consegue ler do curso para frente.
"""