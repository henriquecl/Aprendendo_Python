"""
Escrevendo em arquivos

write() -> Utilizada para escrever em arquivos, recebe como parâmetro uma string

Por padrão, o open abre o arquivo em modo 'r', sendo APENAS de LEITURA. Da mesma forma, se abrirmos o arquivo para es-
crita podemos APENAS ESCREVER.
CUIDADO!! Ao utilizar o modo 'w'
1 - Ao abrir um arquivo para escrita, caso o mesmo não existe, ele é criado no sistema operacional.
2 - Se o arquivo existir, o antigo será apagado, e um novo criado.
# Exemplo de escrita - modo 'w' - write
teste = 'daleeee\n'
with open('novo.txt', 'w', encoding='UTF-8') as arquivo:
    print(arquivo.write(teste))
    print(arquivo.write('Podemos colocar quantas linhas quisemos.\n'))
    print(arquivo.write('Última linha.'))
    print(arquivo.write('3'))

# Forma tradicional de escrever em arquivo
arquivo = open('mais.txt', 'w', encoding='UTF-8')
arquivo.write('dale\n')
arquivo.write('dalee\n')
arquivo.write('daleee\n')
arquivo.write('daleeee\n')
arquivo.close()
"""
with open('frutas.txt', 'w', encoding='UTF-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite ''sair'': ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break



