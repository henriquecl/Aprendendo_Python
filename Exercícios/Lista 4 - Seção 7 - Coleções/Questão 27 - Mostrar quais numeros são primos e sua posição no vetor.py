# Questão 27 - Leia 10 num e armazene num vetor. Em seguia escreva os elementos que são primos e suas respectivas
# posições no vetor

lista = []
divisores = []
for j in range(10):
    print(f'Digite {10 - j} numeros para que eu diga quais são primos:')
    numeros1 = int(input())
    lista.append(numeros1)

for i in range(10):
    for j1 in range(1, lista[i]+1):
        teste = lista[i] / j1
        if int(teste) == teste:
            divisores.append(teste)
    if len(divisores) == 2:
        print(f'O número {lista[i]} é primo e sua posição é {i}')
        divisores.clear()
    elif len(divisores) > 2:
        divisores.clear()