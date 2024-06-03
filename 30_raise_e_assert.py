print('\n# Exemplo 1: Levantar exceções')
def soma(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError('n1 e n2 não podem ser negativos')
    return n1 + n2

print(soma(2, -2))

print('\n# Exemplo 2: Forçar assert')
x = -2
assert x > 0, 'x deve ser maior que 0'
print(x)