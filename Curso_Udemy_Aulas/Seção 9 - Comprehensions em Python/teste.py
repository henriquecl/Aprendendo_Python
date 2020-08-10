lista = [[], [], []]

for i in range(3):
    for j in range(3):
        numero = input('digte um numero:')
        lista[i].append(numero)

print(f'{lista[0]}\n{lista[1]}\n{lista[2]}')