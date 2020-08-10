
# Questão 32 - Leia dois vetores inteiro x e y, cada um com 5 elementos (assuma que o usuário não informe repetidos)
# Calcule e mostre os vetores resultantes em cada passo abaixo:
# a) soma entre x e y;
# b) produto entre x e y;
# c) diferença entre x e y;
# d) interseção entre x e y;
# e) união entre x e y.


x = []
y = []
uniao = []
intersecao = []
elementos_que_nao_existem = []
# Coletando os dados
for i in range(5):
    numero = int(input(f'Digite {5-i} valor(es)\n'))
    x.append(numero)

for i2 in range(5):
    numero = int(input(f'Digite {5-i2} valor(es)\n'))
    y.append(numero)

# soma, diferença e produto

for i3 in range(5):
    soma = x[i3] + y[i3]
    diferenca = x[i3] - y[i3]
    produto = x[i3] + y[i3]
    print(f'A soma dos valores na posição {i3} foi {soma}, a diferença entre eles {diferenca}'
          f' e o produto entre eles é {produto}')

# intereseção e união

intersecao = (set(x).intersection(set(y)))
uniao = (set(x).union(set(y)))
elementos_que_nao_existem = set(x).difference(set(y))
print(f'Os elementos que tem em X que não tem em Y são {elementos_que_nao_existem}')
print(f'A interseção dos dois conjuntos é:{intersecao}')
print(f'A união dos dois conjuntos é:{uniao}')

