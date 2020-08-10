# Questão 18 - Faça um prog q leia 10 numeros, leia o numero x. Conte os múltiplos de um número inteiro X e mostre-os
# na tela

lista = []
lista_dos_multiplos = []
numero = 0

for i in range(10):
    print(f'Digite {10-i} valor(es)')
    numero = float(input())
    lista.append(numero)
X = int(input('Digite um valor para que eu diga quem são seus multiplos\n'))

for j in range(10):
    if lista[j] % X == 0:
        lista_dos_multiplos.append(lista[j])
print(f'O número na lista que são multiplos de {X} são: {lista_dos_multiplos}')