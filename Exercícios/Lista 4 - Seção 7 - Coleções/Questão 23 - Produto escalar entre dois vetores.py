# Questão 23 - Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles.
# imprimir os dois conjuntos e o produto escalar

A = []
B = []
numero = 0
produto_escalar= 0

for i1 in range(5):
    print(f'Digite {5-i1} numer(os)')
    numero = float(input())
    A.append(numero)

for i2 in range(5):
    print(f'Digite {5-i2} numer(os)')
    numero = float(input())
    B.append(numero)

for i3 in range(5):
    produto_escalar = produto_escalar + (A[i3]*B[i3])
print(f'Os vetores digitados foram:{A} e {B}')
print(f'O resultado do produto escalar foi:{produto_escalar}')
