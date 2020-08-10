"""
Questão 3 - Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais
"""
numero_de_vogais = 0
with open('questao2.txt', 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read()

for vogal in texto:
    if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
        numero_de_vogais = numero_de_vogais + 1
    if vogal == 'A' or vogal == 'E' or vogal == 'I' or vogal == 'O' or vogal == 'U':
        numero_de_vogais = numero_de_vogais + 1
print(numero_de_vogais)