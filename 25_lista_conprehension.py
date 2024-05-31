print("\n# Modo 1")
x = [i for i in range(0, 10)]

print("\n# Modo 2")
y = []
for i in range(0, 10):
    y.append(i)
    
print(x)
print(y)

print("\n# Modo 3 - Adicione o valor 10, 10 vezes dentro da variável x")
a = [10 for i in range(0, 10)]

print(a)

print("\n# Modo 4 - Adicione uma String 10 vezes dentro da variável a")
a = ["Coin, " for i in range(0, 6)]

print(a)

print("\n# Modo 5 - Adicione a multiplicação de 2, 10 vezes dentro da variável b")
b = [1*2 for i in range(0, 10)]

print(b)

print("\n# Modo 6 - Adicione 3 Strings dadas pelo usuário, dentro da variável c")
# c= [input("Digite seu nome: ") for i in range(0, 3)]

# print(c)

print("\n# Modo 7 - Adicione uma lista dentro de outras listas, dentro da variável x")
d = [[j for j in range(4, 7)] for i in range(0, 3)]

print(d)

print("\n# Modo 8 - Adicione uma lista dentro de outras listas, dentro da variável x")
e = [ [[input() for h in range(0, 2)] for j in range(0, 2)] for i in range(0, 2)]

print(e)

print("\n# Modo 9 - Adiciona na lista variável f só se for maior que 4.")
f = [i for i in range(0, 10) if i > 4]

print(f)

print("\n# Modo 10 - Na lista variável f, se for maior que 4, adiciona.")
g = []
for i in range(0, 10):
    if i > 4:
        g.append(i)
        
print(g)

print("\n#11 - Referência para o endereço: y=x aponta para o mesmo endereço de memória, então se alterar a lista y, a alteração também ocorre em x, já no caso de z=x.copy() tem endereço de memória diferente, se alterar x, z nada sofre.")
x =  [1, 2, 3]
y = x
z = x.copy()

print(hex(id(x)))
print(hex(id(z)))
print(hex(id(x)))