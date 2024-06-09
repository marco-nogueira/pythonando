# print('\n# Exemplo 1: Cria um arquivo pessoas.txt e escreve (write) algum texto. Write escreve e sobreescreve o texto')
# arquivo = open('pessoas.txt', 'w')
# i = 0
# while True:
#     if i > 2:
#         break
#     arquivo.write(input('\nDigite o nome de uma pessoa: ') + '\n')
#     i += 1    

# print('\n# Exemplo 2: Cria um arquivo pessoas.txt, se já existe então usa o existente e escreve/adiciona (append) algum texto. Append escreve/adiciona o texto')
# arquivo = open('pessoas.txt', 'a')
# i = 0
# while True:
#     if i > 2:
#         break
#     arquivo.write(input('\nDigite o nome de uma pessoa: ') + ' ' + input('Digite a idade: ') + '\n')
#     i += 1
    
print('\n# Exemplo 3: Lê o arquivo pessoas.txt e imprime no console')
arquivo = open('pessoas.txt', 'r')
resultado = arquivo.read()
print(resultado)

print('\n# Exemplo 4: Lê o arquivo pessoas.txt e imprime no console um caracter por linha')
arquivo = open('pessoas.txt', 'r')
resultado = arquivo.read()
for i in resultado:
    print(i)
    
print('\n# Exemplo 5: Lê o arquivo pessoas.txt e imprime no console uma linha em cada linha')
arquivo = open('pessoas.txt', 'r')
resultado = arquivo.readlines()
for i in resultado:
    print(i)
    
print('\n# Exemplo 5: Lê o arquivo pessoas.txt e imprime no console como o python lê o arquivo, uma lista de strings')
arquivo = open('pessoas.txt', 'r')
resultado = arquivo.readlines()
print(resultado)

print('\n# Exemplo 6: Lê o arquivo pessoas.txt, separa os elementos da lista em lista dentro da lista x, e imprime no console')
arquivo = open('pessoas.txt', 'r')
resultado = arquivo.readlines()
x = []
for i in resultado:
    x.append(i.split())
print(x)

print('\n# Exemplo 7: Lê o arquivo pessoas.txt, separa os elementos da lista em lista dentro da lista x, e imprime no console')
arquivo = open('pessoas.txt', 'r')
resultado = arquivo.readlines()
x = []
for i in resultado:
    x.append(i.split())
print(x)

print('\n# Exemplo 8: Lê o arquivo pessoas.txt, separa os elementos da lista em lista dentro da lista x, e imprime no console a lista na posição 4 na lista x')
arquivo = open('pessoas.txt', 'r')
resultado = arquivo.readlines()
x = []
for i in resultado:
    x.append(i.split())
print(x[4])

print('\n# Exemplo 9: Lê o arquivo pessoas.txt, separa os elementos da lista em lista dentro da lista x, e imprime no console o elemento da posição 1 da lista na posição 4 na lista x. Por último fecha o arquivo.')
arquivo = open('pessoas.txt', 'r')
resultado = arquivo.readlines()
x = []
for i in resultado:
    x.append(i.split())
print(x[4][1])
arquivo.close() # Sempre depois de usar deve fechar o arquivo. Evitará vulnerabilidades e outros bugs.

print('\n# Exemplo 10: Lê o arquivo pessoas.txt, utiliza with, assim o sistema se encarrega de abrir e fechar o arquivo.')
with open('pessoas.txt', 'r') as arq:
    x = arq.read()
    print(x)
