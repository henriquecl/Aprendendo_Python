# Questão 16 - Faça um progrmama que leia 5 numeros reais, e depois um código inteiro.
# Se o código for 0: Para
# Se o código for 1: Mostre o vetor na ordem direta
# Se o código for 2: Mostre o vetor na ordem inversa
# Caso o código for diferente de 1 e 2 escreva uma mensagem informando q oc ódigo é invalido

lista = []
numero = 0


for i in range(5):
    print(f'Digite {5 - i} numer(os)')
    numero = float(input())
    lista.append(numero)
i = int(input('Digite a operação que deseja\n'))

if i != 1 or i != 2 or i !=0:
    print('Código inválido')

if i == 1:
    print(f'Os valores inseridos foi: {lista}')

if i == 2:
    lista.reverse()
    print(f'Os valores interidos foi {lista}')

if i == 0:
    print('O programa foi finalizado')