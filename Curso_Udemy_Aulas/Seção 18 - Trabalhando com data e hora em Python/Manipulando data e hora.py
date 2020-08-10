"""
Manipulando data e hora

Python tem um módulo Built-in para se trabalhar com data e hora chamado datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.datetime.now())  # 2020-06-15 18:18:53.597045
print(repr(datetime.datetime.now()))  # datetime.datetime(year, month, day, hour, minute, second, microsecond)

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)
# Alterar o horário para 16 hrs, 0 0 0
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

# Recebendo dados do usuário e convertando para data

evento = datetime.datetime(2021, 1, 1, 0)
print(type(evento))
print(type('31/12/2018'))
print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')
print(nascimento)
nascimento = nascimento.split('/')
print(nascimento)
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)

"""
import datetime

evento = datetime.datetime.now()

# Acesso individual dos elementos da data e hora
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

print(dir(evento))