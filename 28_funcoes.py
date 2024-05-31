print('\n# Exemplo 1: Simples função')
def minha_funcao():
    print('Olá mundo!')
minha_funcao()

print('\n# Exemplo 2: Função recebe valor')
def soma_numeros(n1):
    print(n1)
soma_numeros(2)

print('\n# Exemplo 3: Função recebe 2 valores')
def soma_dois_numeros(n1, n2):
    print(n1 + n2)
soma_dois_numeros(2, 3)
soma_dois_numeros(n1 = 5, n2 = 6)
soma_dois_numeros(n2 = 3, n1 = 4)

print('\n# Exemplo 4: Função recebe vários valores, não se sabe quantos')
def passando_varios_numeros(*args):
    print(args)
passando_varios_numeros(1, 2, 3, 4, 5)

def passando_varios_numeros_b(n1, n2, *args):
    print(f'n1 = {n1}, n2 = {n2} e args = {args}')
passando_varios_numeros_b(1, 2, 3, 4, 5)

print('\n# Exemplo 5: Função recebe vários valores, não se sabe quantos e soma')
def somando_varios_numeros(*args):
    print(sum(args))
somando_varios_numeros(1, 2, 3, 4, 5, 6)

def soma_varios_numeros(*args):
    soma = 0
    for i in args:
        soma = soma + i
    print(soma)
soma_varios_numeros(1, 2, 3, 9, 4) 

print('\n# Exemplo 6: Função recebe vários valores e organiza como dicionário')
def meu_dicionario(**kwargs):
    print(kwargs)
meu_dicionario(teste1 = 1, teste2 = 2, teste3 = 3)

print('\n# Exemplo 7: Função recebe vários valores e organiza como dicionário, verifica se o valor do dicionário existe')
def meu_dicionario(**kwargs):
    x = kwargs.get('teste1')
    if x:
        print('foi passado')
    else:
        print('não foi passado')
meu_dicionario(teste1 = 1, teste2 = 2, teste3 = 3)

def meu_dicionario(**kwargs):
    y = kwargs.get('teste4')
    if y:
        print('foi passado')
    else:
        print('não foi passado')
meu_dicionario(teste1 = 1, teste2 = 2, teste3 = 3)
        
print('\n# Exemplo 8: Função retorna valor, mas não mantém a variável')
def soma_valores(n1, n2):
    print(n1 + n2)

y = soma_valores(1, 2)
print(y)

print('\n# Exemplo 9: Função retorna valor, mas e mantém a variável')
def soma_valores(n1, n2):
    soma = n1 + n2
    return soma

print(soma_valores(1, 2))
y = soma_valores(1, 2) +1
print(y)