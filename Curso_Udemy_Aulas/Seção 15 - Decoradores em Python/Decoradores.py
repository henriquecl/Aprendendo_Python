"""
Decorators (Decoradores)

- São funções;
- Envolvem outras funções e aprimoram seus comportamentos;
- Também são exemplos de higher order functions;
- Tem uma sintaxe própria usando "@" (Syntact Sugar)


# Decorators como funções (Sintaxe não recomendada/ sem syntact sugar

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) à Geek Univeristy')

# Testando 1
teste = seja_educado(saudacao)
teste()
def raiva():
    print('EU TE ODEIO!!')
raiva_educada = seja_educado(raiva)
raiva_educada()



# Decorators com Syntax Sugar


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir')


dormir()
"""


