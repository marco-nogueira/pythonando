print('\n# Exemplo 1: Função Lambda com Map, adiciona 10 para os valores menores que 18, converte o map em lista')
x = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

x = list(map(lambda x: 10 if x < 18 else(x), x)) # Converte em lista para poder retornar com print

print(x)

print('\n# Exemplo 2: Função Lambda com Map, adiciona 10 para dicionário menores que 30, converte o map em lista')
x = [{'nome': 'Caio', 'idade': 20},{'nome': 'Marco', 'idade': 40}]

x = list(map(lambda x: 10 if x['idade'] < 30 else(x), x)) # Converte em lista para poder retornar com print

print(x)

print('\n# Exemplo 3: Função Lambda com Map, adiciona 10 no lugar da idade, para dicionário menores que 30, converte o map em lista')
x = [{'nome': 'Caio', 'idade': 20},{'nome': 'Marco', 'idade': 40}]

x = list(map(lambda x: {'nome': 'Caio', 'idade': 'menor que 30 anos'} if x['idade'] < 30 else(x), x)) # Converte em lista para poder retornar com print

print(x)

print('\n# Exemplo 4: Função Lambda com Map, um erro de substituição, adiciona 10 no lugar da idade, para dicionário menores que 30, converte o map em lista')
x = [{'nome': 'Caio', 'idade': 20},{'nome': 'Marco', 'idade': 23}]

x = list(map(lambda x: {'nome': 'Caio', 'idade': 'menor que 30 anos'} if x['idade'] < 30 else(x), x)) # Converte em lista para poder retornar com print

print(x) # Vai mudar os 2 dicionários para Caio.

print('\n# Exemplo 5: Função Lambda com Map, corrige o problema anterior, mantêm o nome, adiciona 10 no lugar da idade, para dicionário menores que 30, converte o map em lista')
x = [{'nome': 'Caio', 'idade': 20},{'nome': 'Marco', 'idade': 23}]

x = list(map(lambda x: {'nome': x['nome'], 'idade': 'menor que 30 anos'} if x['idade'] < 30 else(x), x)) # Converte em lista para poder retornar com print

print(x) # Não vai mudar os 2 dicionários para Caio.