# Questão 1 - Faça um programa que possua um vetor denominado A, que armazene 6 numeros inteiros
# a) atribuir os valores abaixo para ele
A = [1, 0, 5, -2, -5, 7]
print(A)
# letra b) somas a posições ditas

soma = A[0] + A[1] + A[5]
print(soma)

# letra c) modificar o valor de uma posição

A.pop(3)
A.insert(3, 100)
print(A)

# letra d)  mostrar na tela o valor de cada posição separado
i = 0
while i != len(A):
    i = i + 1
    print(A[i])
