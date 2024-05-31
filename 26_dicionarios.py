print('\n# Exemplo 1: manipulando dicionários')

x = {'nome':'Marco Nogueira', 'idade':21, 'CEP':'88200-000'}

print(x)
print(x['nome'])

x['nome'] = 'Pedro'

print(x['nome'])
print(x['CEP'])

print('\n# Exemplo 2: manipulando dicionários')

y = {'nome':[], 'idade':21, 'CEP':'88200-000'}

print(type(y['nome']))
y['nome'].append('Marco')
y['nome'].append('Pedro')

print(y['nome'])

print('\n# Exemplo 3: dicionário dentro de uma lista')

pessoas = [{'nome':'Marco', 'idade':21, 'altura':'182'},
           {'nome':'Caio', 'idade':21, 'altura':'173'},
           {'nome':'Pedro', 'idade':21, 'altura':'150'}]

print(type(pessoas))
print(type(pessoas[1]))

for pessoa in pessoas:
    print(pessoa['nome'])

print('\n# Exemplo 4: Update dentro de uma lista')
pessoa.update({'cep': '86079-400', 'rua': 'Minha rua'})
print(pessoa)
print(pessoas)

print('\n# Exemplo 5: Key Values de uma lista')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

for i in pessoa.items():
    print(i[0], i[1])

print('\n# Exemplo 6: Iterar Key Values de uma lista')
for d in pessoas:
    print(d['nome'], d['idade'], d['altura'])
    for i, j in d.items():
        print(f'i = {i} e j = {j}')
