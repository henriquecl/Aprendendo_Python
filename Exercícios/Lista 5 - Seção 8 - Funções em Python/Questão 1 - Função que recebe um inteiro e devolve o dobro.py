#  Questão 1 - Crie uma função que recebe como parâmetro um número inteiro e devolve o dobro
def dobro(numero):
    return numero*2


num = int(input('Digite um número\n'))

while num != 0:
    num = int(input('Digite um número\n'))
    print(dobro(num))




