# Questão 5 - Faça um programa que peça para o usuário digitar 10 valores e some-os
soma = 0
for i in range(0, 10):
    numero = float(input(f'Digite {10 - i} numero(s) para a soma ser realizada\n'))
    soma = soma + numero

print(f'A soma dos valores inseridos foi {soma}')