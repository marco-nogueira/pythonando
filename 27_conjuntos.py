print('\n# Exemplo 1: lista')
x = [1, 2, 3, 1, 1, 2, 3, 1, 4, 7]
print(x)

print('\n# Exemplo 2: Converte em um set, não permite valores repetidos')
x = set(x)
print(x)

print('\n# Exemplo 3: Criar um set')
y = {1, 2, 4, 4, 5, 6}
print(f'{y}\n')

print('\n# Exemplo 4: União de conjuntos, x união com y')
print(f'x = {x}')
print(f'y = {y}')
u = x.union(y)
print(f'x união com y = {u}')

print('\n# Exemplo 5: Intersecção de conjuntos, x Intersecção com y')
print(f'x = {x}')
print(f'y = {y}')
i = x.intersection(y)
print(f'x Intersecção com y = {i}')

print('\n# Exemplo 6: Diferença de conjuntos, x diferença com y')
print(f'x = {x}')
print(f'y = {y}')
d = x.difference(y)
print(f'x Diferença com y = {d}')

print('\n# Exemplo 7: Diferença de conjuntos, y diferença com x')
print(f'x = {x}')
print(f'y = {y}')
d2 = y.difference(x)
print(f'y Diferença com x = {d2}')