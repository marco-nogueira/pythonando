# Função lambda sempre retorna alguma coisa, por mais que não se utilize a palavra return

print('\n# Exemplo 1: Função Lambda usando OS para limpar linha de comando, mas não é chamada.')
import os
x = lambda: os.system('cls')
# x()

print('\n# Exemplo 2: Função Lambda simples print, qual o tipo de x.')
x = lambda: print('olá')
print(type(x))

print('\n# Exemplo 3: Função Lambda, mostra o tipo de função e a alocação da memória')
print(x)

print('\n# Exemplo 4: Função Lambda, executa a função no print, mas a função já é um print')
print(x())

print('\n# Exemplo 5: Função Lambda, executa a função da forma correta')
x()

print('\n# Exemplo 6: Função Lambda, retorna o valor e printa')
x = lambda: 10
print(x())

print('\n# Exemplo 7: Função Lambda, apenas retorna o valor mas não printa, pois não foi pedido')
x = lambda: 10
x()

print('\n# Exemplo 8: Função Lambda, com parâmetros, se não passar parâmetros dará erro')
x = lambda nome, idade: print(f'nome = {nome}\nidade = {idade}')
x('Marco', 44)

print('\n# Exemplo 9: Função Lambda, com parâmetros, sem esperar um número exato de parâmetros')
x = lambda *nomes: print(f'nomes = {nomes}')
x('Marco', 'Eduardo', 'Elaine', 'Bella')

print('\n# Exemplo 10: Função Lambda, dentro de uma função')
def funcao():
    return lambda *nomes: print(f'nomes = {nomes}')
x = funcao()
x('Marco', 'Elaine', 'Bella')