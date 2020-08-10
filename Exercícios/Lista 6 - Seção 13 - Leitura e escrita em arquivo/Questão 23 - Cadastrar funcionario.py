"""
Questão 23 -  Faça um programa que leia a profissão e o tempo de serviço em anos de cada um dos 5 funcionários de uma
empresa e armazene-os no arquivo ''emp.txt''. Cada linha do arquivo corresponde a um funcionário
"""
with open('questao23.txt', 'a', encoding='UTF-8') as arquivo:
    for i in range(5):
        profissao = input('Digite a profissão que você exerce na empresa: ')
        anos = input('Digite o tempo de serviço na empresa:')
        texto = 'A profissão é:' + profissao + '. E trabalha na empresa há: ' + anos +'\n'
        arquivo.write(texto)



