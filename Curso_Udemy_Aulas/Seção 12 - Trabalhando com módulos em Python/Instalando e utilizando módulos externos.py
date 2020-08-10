"""
Módulos externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package
Todos os pacotes externos oficiais se encontrame em: https://pypi.org/

colorama -> É utilizado para permitir impressão de textos coloridos no terminal

Instalando um módulo: pip install nome-do-modulo  (geralmente no site do módulo já diz como fazer)
----------------Utilizando o pacote instalado (Colorama)------------
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.BLACK + 'Dale')
print(Back.WHITE + 'Dale')
"""
import pydf
pdf = pydf.generate_pdf('<h1>Geek University</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
