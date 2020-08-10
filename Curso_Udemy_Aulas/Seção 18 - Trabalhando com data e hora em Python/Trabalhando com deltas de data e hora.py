"""
Deltas de data e hora

data_fim - data_inicial
"""
import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2021, 3, 7, 0)
tempo_evento = aniversario - data_hoje
print(tempo_evento)
print(type(tempo_evento))
print(repr(tempo_evento))

