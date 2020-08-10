"""
Questão 16 - Faça um programa que recebe um vetor de 10 numeros, converta cada um pra binário e grave a sequencia conver
tida em um arquivo texto. Cada um numa linha.
"""
lista_entrada = [9, 19, 209, 39, 483, 2, 39, 238, 38, 40]

with open('questao16.txt', 'a', encoding='UTF-8') as arquivo:
    for i in range(len(lista_entrada)):
        numero = bin(lista_entrada[i])
        arquivo.write(numero + '\n')


