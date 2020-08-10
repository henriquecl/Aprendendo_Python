"""
StringIO -> Utilizado para ler e criar arquivos em memória.

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - Permissão de leitura
    - Permissão de escrita


"""
# Primeiro fazemos o import
from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida, ou mesmo vazio para inserir-mos o texto depois.
arquivo = StringIO(mensagem)        # Equivalente é arquivo = open('arquivo.txt', 'w')

# Agora, tendo o arquivo, podems utilizar tudo que ja sabemos sobre eles.
print(arquivo.read())
# Escrevendo outro texto
arquivo.write('Outro texto\n')
# Podemos inclusive movimentar o cursor
arquivo.seek(0)
print(arquivo.read())