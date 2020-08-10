# Exercício 4 - Faça um programa que leia um numero e caso seja positivo, mostre o numero ao quadrado e a raiz dele

num = float(input('Digite um valor\n'))

if num >= 0:
    print(f"O valor desse valor ao quadrado é: {num**2} \n e a raiz dele é {num**(1/2)}")
