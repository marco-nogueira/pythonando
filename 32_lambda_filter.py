print('\n# Exemplo 1: Função Lambda com Filter, converte o filter em lista')
x = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

x = list(filter(lambda x: x < 18 or x % 2 == 0, x)) # Converte em lista para poder retornar com print

print(x)

print('\n# Exemplo 2: Função Lambda com Filter, trabalhando com uma lista de dicionários, filtra pelo dicionário')
x = [{'nome': 'Caio', 'idade': 20},{'nome': 'Marco', 'idade': 40}]

x = list(filter(lambda x: x['idade'] >= 40, x)) # Converte em lista para poder retornar com print

print(x)
