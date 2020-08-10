# Exercício 6 - Escreva um programa que, dado dois números inteiros
# mostre o maior, assim como a diferença entre ambos

num1 = float(input('Digite um numero\n'))
num2 = float(input('Digite outro numero\n'))

if num1 > num2:
    print(f" O maior número é:{num1} \n A diferença entre eles é: {num1-num2}")
else:
    print(f" O maior número é:{num2} \n A diferença entre eles é: {num2-num1}")
