# Questão 1 - Faça um programa que determine e o mostre os cincos primeiros
# múltiplos de 3, considerando numeros maiores que 0
i = 0
for num in range(1, 2000):
    if num % 3 == 0:
        i = i + 1
        print(f'O multiplo de numero {i} de 3 é {num}')
    if i == 5:
        break