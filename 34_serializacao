import pickle
from pympler.asizeof import asizesof

print('\n# Exemplo 1: Print o valor de x em formato binário, veja a letra b em frente a string.')
x = 1
print(pickle.dumps(x))

print('\n# Exemplo 2: Faz a serialização, salva com binário na variável e depois converte a variável serializada no formato original')
a = [1, 2, 3, 4, 5]
a_serializado = pickle.dumps(a)
print(pickle.loads(a_serializado))

print('\n# Exemplo 3: Faz a serialização, salva com binário na variável e depois converte a variável serializada no formato original. Ao fim exibe o seu tipo.')
a = [1, 2, 3, 4, 5]
a_serializado = pickle.dumps(a)
print(type(pickle.loads(a_serializado)))

print('\n# Exemplo 4: Faz a serialização, salva com binário na variável e depois converte a variável serializada no formato original. Ao fim exibe o seu tipo.')
a = [1, 2, 3, 4, 5]
a_serializado = pickle.dumps(a)
print(type(pickle.loads(a_serializado)))

print('\n# Exemplo 5: Obtem um nome de dentro de um dicionário')
b = {'nome': 'caio', 'idade': 20} 
b_string = pickle.dumps(b) # Escreve b serializado dentro da variável string.
print(pickle.loads(b_string)['nome']) # Print o conteúdo do arquivo serializado.
print(asizesof(b)) # Print o tamanha de b.
print(asizesof(b_string)) # Print o tamanha de b_string serializado.

# print('\n# Exemplo 6: Abre um arquivo para salvar os valores em formato binário. Faz a serialização, salva com binário na variável e depois converte a variável serializada no formato original. Ao fim exibe o seu tipo.')
# b = [1, 2, 3, 4, 5]
# b_binario = open('arquivo.pkl', 'wb') # Abre o arquivo serializado e prepara para escrever.
# pickle.dumps(b_binario, b) # Escreve b serializado dentro do arquivo arquivo.pkl.
# print(type(pickle.loads(b_binario))) # Print o conteúdo do arquivo serializado.

