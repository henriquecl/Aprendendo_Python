"""
Seek e Cursors

seek() -> Utilizada para movimentar o curso pelo arquivo.
Essa função, é utilizada para movimentação do cursor pelo arquivo. Ela recebeu parâmetro que indica onde queremos colo-
car o cursor.
-----------------
# Movimentando o cursor pelo arquivo com a função seek() and destroyyyyy
arquivo = open('texto.txt', encoding='UTF-8')
print(arquivo.read())
arquivo.seek(22)
print(arquivo.read())
------------------------
# readline() -> Lê o arquivo linha a linha
arquivo = open('texto.txt', encoding='UTF-8')
ret = arquivo.readline()
print(type(ret))   # str
print(ret)
print(ret.split(' '))
-----------------------------
#  readlines() -> Transforma cada linha do texto que tem conteúdo numa posição de uma lista.
arquivo = open('texto.txt', encoding='UTF-8')-
linhas = arquivo.readlines()
print(len(linhas))
print(linhas)
------------------------------
OBS: Quando abrimos um arquivos com a função open() é criada uma conexão entre o arquivo no disco do computadoe e o
programa. Essas conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo, devemos fechar essa conexão.
Para isso, utilizamos a função close()

Passos para se trabalhar com um arquivo:
1 - Abrir o arquivos
2 - Fazer o que precisar
3 - Fechar o arquivo
arquivo.close() # Fecha o arquivo
print(arquivo.close) # Verifica se está aberto ou fechado

OBS: Se tentarmos manipular um arquivo após seu fechamento teremos: ValueError: I/O operation on closed file.

1 - Abrir o arquivos
arquivo = open('texto.txt', encoding='UTF-8')
2 - Fazer o que precisar
print(arquivo.read())
print(arquivo.closed)
3 -  Fechar o arquivo
arquivo.close()
print(arquivo.closed)
"""
arquivo = open('texto.txt', encoding='UTF-8')

print(arquivo.read(50))   # Limita quantos caracteres serão lidos
