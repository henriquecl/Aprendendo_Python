"""
Bloco With

Passos para se trabalhar com arquivos
1 - Abrir o arquivos
2 - Fazer o que precisar
3 - Fechar o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with.
"""

# Bloco with - Forma Pythônica de manipular arquivos

with open('texto.txt', encoding='UTF-8') as arquivo:
    print(arquivo.read())
    print(arquivo.closed)
    arquivo.seek(0)
    print(arquivo.read())
print(arquivo.closed)
