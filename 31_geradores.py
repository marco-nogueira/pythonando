from pympler.asizeof import asizesof

print('\n# Exemplo 1: Verifica o tamanho de espaço em memória necessário para armazenar o dado')
print(asizesof(1))
print(asizesof(100000000000000000000000000000000000000000))
print(asizesof("Marco"))

print('\n# Exemplo 2: Função normal')
def dobro(lista):
    lista_dobro = []
    for i in lista:
        lista_dobro.append(i*2)
        
    return lista_dobro

y = dobro(range(0, 100))
x = asizesof(dobro(range(0, 100))) # Se aumentar o tamanho do número, aumenta o tamanho da memória gasta.
print(y)
print(f'A quantidade de memória gasta para armazenar a lista foi de: {x} bits')

print('\n# Exemplo 3: Função geradora - vai oferecer memória de acordo com a necessidade, não armazena tudo direto')
def dobro_b():
    yield 1
    yield 2
    yield 3

x = dobro_b()

print(next(x))
print(next(x))
print(next(x))

print('\n# Exemplo 4: Função geradora - Estoura quando tenta prover um número que não existe')
def dobro_c():
    yield 1
    yield 2
    yield 3

x = dobro_c()

print(next(x))
print(next(x))
print(next(x))
# print(next(x)) # Descomentar para que funcione

print('\n# Exemplo 5: Função geradora - prove infinito')
def dobro_d():
    i = 0
    while True:
        i = i + 1
        yield i

x = dobro_d()

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print('\n# Exemplo 6: Função geradora - com for e lista')
def dobro_e(lista):
    for i in lista:
        yield i

x = dobro_e([1, 2, 3, 4, 5, 6])

print(next(x))
print(next(x))
print(next(x))
print(next(x))

print('\n# Exemplo 7: Função geradora - com for e lista, passando via range')
def dobro_f(lista):
    for i in lista:
        yield i

x = dobro_f(range(0, 100))

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print('\n# Exemplo 8: Função geradora - comparando memória de função geradora e função normal')
def dobro_g(lista):
    for i in lista:
        yield i*2

def dobro_g2(lista):
    lista_2 = []
    for i in lista:
        lista_2.append(i*2)
    return lista_2

x = dobro_g(range(0, 10000))
y = dobro_g2(range(0, 10000))

size_of_x = (asizesof(x))
size_of_y = (asizesof(y))

print(f'A quantidade de memória gasta para armazenar a lista pela função geradora foi de: {size_of_x} bits')
print(f'A quantidade de memória gasta para armazenar a lista pela função normal foi de: {size_of_y} bits')

# o FOR é um um iterador gerador, usa a função geradora por baixo dos panos