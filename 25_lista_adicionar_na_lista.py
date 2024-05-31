# Receba 10 valores e exiba a soma de todos eles

# x = [input() for i in range(0, 10)]
# print(x)

# Transforma em int antes de adicionar na lista
x = [int(input()) for i in range(1, 3)]

soma = 0
for i in x:
    soma += i
    
print(soma)