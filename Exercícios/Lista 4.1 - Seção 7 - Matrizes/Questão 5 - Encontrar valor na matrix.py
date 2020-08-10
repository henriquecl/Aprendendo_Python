"""
Questão 5 - Leia uma matrix 5x5. Leia também o valorr X. O programa deverá fazer uma bsuca desse valor na matriz, e ao
final escrever a localização ou uma mensagem de não encontrado
"""

matrix = [[1, 2, 3, 4, 5], [789, 19, 19, 19, 19], [1891, 1, 1, 1, 1], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
linha = 0
coluna = 0
x = float(input('Digite um valor'))
aux = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == x:
            maximo = matrix[i][j]
            linha = i
            coluna = j
            aux = 1

if aux:
    print(f'O valor procurado {x} foi encontrado e está na linha: {linha}, e na coluna: {coluna} ')
else:
    print('Valor não encontrado')


for i in range(len(matrix)):
    if i == 0:
        print('A matriz digitada foi:')
    print(matrix[i])
