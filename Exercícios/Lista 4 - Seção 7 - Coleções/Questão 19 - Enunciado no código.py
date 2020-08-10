# Questão 19 - Faça um vetor de tamanho 50 ser preenchido com (i+5*i)%(i+1), sendo i a posição. Imprima o vetor

lista = []
numero = 0

for i in range(50):
    numero = (i+(5*i)) % (i+1)
    lista.append(numero)
print(lista)
