"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com
um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências
desse elemento.

# Utilizando o Counter
from collections import Counter

# Ex 1
# Podemos utilizar qualquer iterável, aqui utilizamos lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 1, 2, 3, 3, 4, 5, 6, 7, 6, 6, 6, 6]


res = Counter(lista)

# Ele é escrito na forma Elemento: Número de ocorrências
#                         CHAVE  : Qtd de Ocorrências
# Counter({3: 6, 6: 5, 1: 4, 2: 4, 4: 1, 5: 1, 7: 1})

print(type(res))
print(res)

# Ex 2

print(Counter('Geek University'))
"""

# Ex 3
from collections import Counter

texto = """ O incidente dos envelopes postais da Apollo 15 foi um escândalo da NASA em 1972 envolvendo os astronautas
 da Apollo 15, que levaram aproximadamente quatrocentos envelopes postais não autorizados para o espaço e até a 
 superfície da Lua a bordo do módulo lunar Falcon. Alguns desses foram vendidos pelo comerciante de selos alemão Hermann
  Sieger por preços altos, ficando conhecidos como "envelopes Sieger". Os astronautas David Scott, Alfred Worden e James
   Irwin concordaram em aceitar pagamentos para levarem os envelopes, porém devolveram o dinheiro e foram repreendidos
    pela NASA. A imprensa realizou uma grande cobertura do incidente e a tripulação foi convocada para depor diante de 
    um comitê do Senado. Os três nunca mais voltaram para o espaço e deixaram a NASA até 1977; os envelopes apreendidos
     foram devolvidos em 1983.
Os três astronautas mais seu conhecido Horst Eiermann concordaram em produzir os envelopes e levá-los para o espaço.
 Cada um dos membros da tripulação receberia por volta de sete mil dólares. Scott conseguiu fazer com que os envelopes
  fossem carimbados na manhã do lançamento da Apollo 15 em 21 de julho de 1971. Eles foram embalados e entregues a ele 
  enquanto se preparava. Os envelopes não foram incluídos na lista de itens pessoais que estariam carregando por causa
   de um erro.
   Todos ficaram desde 30 de julho até 2 de agosto a bordo do Falcon na superfície lunar. Elas foram carimbadas
    novamente em 7 de agosto, o dia da amerrissagem, a bordo do navio de resgate USS Okinawa. Cem foram enviadas para
     Eiermann, que as repassou para Sieger; as restantes foram divididas entre os astronautas"""

palavras = texto.split()  # Separa o texto em strings indivíduais
# print(palavras)

res = Counter(palavras)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))






