"""
Questão 24 - Implemente um controle simples de mercadorias em uma despensa doméstica. Para cada produto armazene um códi
-go numérico, descrição e quantidade atual. O programa deve ter opções para entrada e retirada de produtos, bem como um
relatório geral e um de produtos não disponíveis.
"""

# Cadastrando Produto
funcao = input('Digite qual função você deseja: "Cadastrar", "Consultar": ')

if funcao == 'Cadastrar':
    with open('questao24.txt', 'a', encoding='UTF-8') as arquivo:
        while True:
            produto = input("Digite o nome do produto que deseja cadastrar, para parar o cadastro digite 'parar': ")
            if produto == 'parar':
                break
            quantidade = input('Quantos produtos: ')
            linha = produto + ' ' + quantidade + '\n'
            arquivo.write(linha)

