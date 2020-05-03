# Exercício 2 - Leia um número fornecido pelo usúario. Se for positivo
# calcular a raiz quadrada. Se for negativo diz q nao pode

num = float(input('Digite um valor\n'))

if num < 0:
    print("Não existe raiz quadrada do valor nos reais")
else:
    print(f"O valor da raiz é igual a {num**(1/2)}")