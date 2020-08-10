"""
Modos de abertura de arquivos

r -> read-only
w -> write-only - Sobrescreve caso exista.
x -> write-only - Abre para escrita somente se o arquivo não existir, caso o arquivo exista gera o erro:
FileExistsError: [Errno 17] File exists: 'university.txt'
Exemplo 'x':
try:
    with open('university.txt', 'x', encoding='UTF-8') as arquivo:
        arquivo.write('Teste de conteúdo 2\n')
except FileExistsError:
    print('Arquivo já existe')

a -> write-only - Adicionando o conteúdo SEMPRE para o FINAL do arquivo (mesmo alterando a posição do cursor)
caso ele exista, de não existir será criado
Exemplo 'a':
with open('outro.txt', 'a', encoding='UTF-8') as arquivo:
    arquivo.seek(0)
    arquivo.write('No topoo!\n')
    arquivo.write('Nova linha\n')
    arquivo.write('Mais uma linha')

+ -> Abre para o modo de atualização: Leitura e Escrita com controle do cursor

https://docs.python.org/3/library/functions.html#open


# Exemplo r+
with open('outro.txt', 'r+', encoding='UTF-8') as arquivo:
    # arquivo.seek(0)
    arquivo.write('Adicionada\n')
    arquivo.seek(11)
    arquivo.write('Nova linha\n')
    arquivo.seek(32)
    arquivo.write('Mais uma linha\n')
    print(arquivo.read())
"""
