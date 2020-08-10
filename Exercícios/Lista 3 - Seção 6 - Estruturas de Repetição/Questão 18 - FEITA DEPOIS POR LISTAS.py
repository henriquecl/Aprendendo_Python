# Questão 18 - Escreve um algoritmo que leia certa quantidade de números e imprima o maior
# deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve
# ser fornecido pelo usuário

qtd_de_num = int(input('Digite quantos números você deseja fornecer\n'))
maior_numero = 0
num_de_vezes = 0

while qtd_de_num != 0:
    qtd_de_num = qtd_de_num - 1
    numero = int(input('Digite um número\n'))
    if maior_numero <= numero:
        maior_numero = numero

    if maior_numero == numero:
        num_de_vezes = num_de_vezes + 1


print(f'O maior numero foi o {maior_numero}, e foi digitado {num_de_vezes} vez(es)')
