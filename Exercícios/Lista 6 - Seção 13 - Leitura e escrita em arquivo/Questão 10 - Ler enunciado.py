"""
Questão 10 - Faça um programa que receba o nome de um arquivo de entrada e outro de sáida. O arquivo de entrada contem
em cada linha o nome de uma cidade (Ocupando 40 caracteres) e seu número de habitante. O programa deverá ler o arquivo
de entrada e gerar um arquivo de saída onde aparece o nome da cidade mais populosa seguida pelo seu número de habitantes
"""
arquivo_entrada = input('Digite o nome do arquivo de entrada: ')
arquivo_saida = input('Digite o nome do arquivo de saida desejado: ')
lista_de_cidades = []
lista_de_habitantes = []
with open(arquivo_entrada+'.txt', 'r', encoding='UTF-8') as arquivo:
    cidades = arquivo.read()

cidades_organizadas = cidades.split()
for i in range(len(cidades_organizadas)):
    if i % 2 != 0:
        aux = int(cidades_organizadas[i])
        lista_de_habitantes.append(aux)
    else:
        lista_de_cidades.append(cidades_organizadas[i])

indice_mais_habitado = lista_de_habitantes.index(max(lista_de_habitantes))
numero_de_habitantes = lista_de_habitantes[indice_mais_habitado]
cidade_mais_habitada = lista_de_cidades[indice_mais_habitado]

with open(arquivo_saida+'.txt', 'w', encoding='UTF-8') as arquivo2:
    arquivo2.write(f'A cidade mais habitada é {cidade_mais_habitada} e possui {numero_de_habitantes} habitantes')





