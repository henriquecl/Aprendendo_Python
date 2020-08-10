"""
Mapas -> Conhecidos em Python como dicionários{}

# Iterar sobre dicionários

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'En {chave} recebi {receita[chave]} reais')

# Acessando as chaves do dicionário
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores do dicionário
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita.values())

for chave in receita.keys():
    print(receita[chave])

# Desempacotamento de dicionarios

print(receita.items())
for chave, valor in receita.items():
    print(f'A chave é {chave} e valor é {valor}')

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Soma*, Valor máximo*, Valor mínimo*, Tamanho
# *Se tiverem apenas int ou float

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""


