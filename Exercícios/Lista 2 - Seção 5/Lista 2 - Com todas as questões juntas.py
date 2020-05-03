"""
# Exercício 1 - Faça um programa que receba dois números e mostre qual o maior
# NOTE: Se não colocar o float(input..) ele não vai interpretar o numeral, e sim a string.
num1 = float(input('Digite um numero\n'))
num2 = float(input('Digite outro numero\n'))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num2 > num1:
    print(f'{num2} é maior que {num1}')
else:
    print('Os numeros são iguais')

# Exercício 2 - Leia um número fornecido pelo usúario. Se for positivo
# calcular a raiz quadrada. Se for negativo diz q nao pode

num = float(input('Digite um valor\n'))

if num < 0:
    print("Não existe raiz quadrada do valor nos reais")
else:
    print(f"O valor da raiz é igual a {num**(1/2)}")


Exercício 3 - Leia um numero real. Se for >0 imprima a raiz, se nao eleve ao quadrado

numero = float(input("Digite um valor\n"))

if numero >= 0:
    print(f"A raiz desse numero é {numero**(1/2)}")
else:
    print(f"O valor desse número ao quadrado é {numero**2}")


# Exercício 4 - Faça um programa que leia um numero e caso seja positivo, mostre o numero ao quadrado e a raiz dele

num = float(input('Digite um valor\n'))

if num >= 0:
    print(f"O valor desse valor ao quadrado é: {num**2} \n e a raiz dele é {num**(1/2)}")


# Exercício 5 - Faça um programa que receba um inteiro e diga se é par ou impar

num_inteiro = int(input('Digite um número inteiro \n'))

if num_inteiro % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")


# Exercício 6 - Escreva um programa que, dado dois números inteiros
# mostre o maior, assim como a diferença entre ambos

num1 = float(input('Digite um numero\n'))
num2 = float(input('Digite outro numero\n'))

if num1 > num2:
    print(f" O maior número é:{num1} \n A diferença entre eles é: {num1-num2}")
else:
    print(f" O maior número é:{num2} \n A diferença entre eles é: {num2-num1}")

#Exercício 7 - Já fiz no exercício 1 kkkkk


# Exercício 8 - Ler 2 notas, verifica se as notas são válidas e
# exibir na tela a média. A nota deve ser entre 0 e 10, onde caso
# nao seja válida o fato deve ser informado e prog termina

nota1 = float(input('Digite a nota do seu 1º EE\n'))
nota2 = float(input('Digite a nota do seu 2º EE\n'))

if 10 < nota1 or nota1 < 0:
    print("Você inseriu um valor incorreto")
elif 10 < nota2 or nota2 < 0:
    print("Você inseriu um valor incorreto")
else:
    print(f"A média das suas notas foi: {(nota1+nota2)/2}")


# Exercício 9 - Ler o salário e o valor da prestação de um emprestimo
# Se a prestação for maior que 20% do salário: emprestimo nao concedido
# Se nao, empréstimo

salario = float(input('Digite seu salário\n'))
parcela = float(input('Digite a parcela do emprestimo\n'))

if parcela > 0.2*salario:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")


# Exercício 10 - programa de calcular imc se for homem uma formula
# se for mule outra formula

altura = float(input('Digite sua altura em metros\n'))
sexo = input('Digite seu sexo\n')

if sexo == 'masculino':
    print(f"Seu imc é: {((72.7*altura)-58)}")
elif sexo == 'feminino':
    print(f"Seu imc é: {((62.1*altura)-44.7)}")
else:
    print('Houve algum erro de digitação')

# Exercício 11 - Dizer a soma dos algarismos de um número***
# Exercício 12/13 é agua


# Exercício 14 - Ponderar notas e dizer se passou ou nao
import sys
trab_lab = float(input('Digite a sua nota do trab de lab\n'))
if 10 < trab_lab or trab_lab < 0:
    print("Você inseriu a nota errada.")
    sys.exit()
av_semestral = float(input('Digite a sua nota da av semestral\n'))
if 10 < av_semestral or av_semestral < 0:
    print("Você inseriu a nota errada.")
    sys.exit()
ex_final = float(input('Digite a sua nota do ex final\n'))
if 10 < ex_final or ex_final < 0:
    print("Você inseriu a nota errada.")
    sys.exit()
media = ((trab_lab*2 + av_semestral*3 + ex_final*5)/10)

if 0 < media < 2.999:
    print(f"Você foi reprovado pois sua média foi: {media}")

elif 3 <= media < 4.999:
    print(f"Você está de recuperaçao pois sua média foi: {media}")
else:
    print(f"Você foi aprovado pois sua média foi: {media}")


# Questão 15,16 usando switch, ele não deu.
# Questão 17 agua

# Questão 18 - Calculadora

operacao = input("Digite qual operação você quer fazer entre "
                 "soma,diferença,divisão ou multiplicação\n")
num1 = float(input("Digite um número\n"))
num2 = float(input("Digite outro número\n"))

if operacao == 'soma':
    print(f"O resultado da soma é: {num1+num2}")
elif operacao == 'diferença':
    print(f"O resultado da diferença é: {num1-num2}")
elif operacao == 'divisão':
    print(f"O resultado da divisão é: {num1/num2}")
elif operacao == 'multiplicação':
    print(f"O resultado da multiplicação é: {num1*num2}")
else:
    print("Operação inválida.")


# Questão 19 - Verificar se um inteiro é divisivel por 3 ou por 5
# mas nao pelos dois simultaneamente

num1 = int(input('Digite um número\n'))

div_por3 = num1 % 3
div_por5 = num1 % 5

if div_por3 == 0 and div_por5 == 0:
    print('O valor é divísivel por 5 e 3 simultaneamente')
elif div_por3 == 0:
    print('O número é divisível por 3')
elif div_por5 ==0:
    print('O valor é divísivel por 5')
"""

# Só exemplo reptitivo que nao agrega muito