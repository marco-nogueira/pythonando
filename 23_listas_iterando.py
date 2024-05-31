
idades = [79, 68, 22, 12, 10, 7, 5, 4, 3, 2, 1]
idades.sort()

for i in range(0, len(idades)):
    print(i, idades[i])

    
x = list(enumerate(idades))
print(x)

for i in range(0, len(idades)):
    print(idades[i])
    
idades_pares = []
for i in idades:
    if i % 2 == 0:
        idades_pares.append(i)

print(idades_pares)