def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
#           return total, Se nós tivessemos colocando o return aqui, o return iria finalizar a função no 1º loop for.
    return total


teste = 'Testou'
