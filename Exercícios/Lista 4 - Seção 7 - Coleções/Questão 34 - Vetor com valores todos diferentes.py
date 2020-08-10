# Questão 34 - Faça um prog para ler 10 num diferentes a serem armazenados em um vetor. Os dados devem ser amazenados
# no vetor na ordem que forem sendo lidos, sendo que caso o usuário digite um número que ja foi digitado anteriormente
# o programa deverá pedir para ele digitar outro numero. Exibir na tela o vetor final digitado

conjunto = set()

while len(conjunto) != 10:
    numero = int(input(f'Digite {10 - len(conjunto)} valores diferentes:\n'))
    conjunto.add(numero)
print(conjunto)
