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

print('\n# Exemplo 6: Abre um arquivo para salvar os valores em formato binário. Faz a serialização, salva com binário na variável e depois converte a variável serializada no formato original. Ao fim exibe o seu tipo.')
b = [1, 2, 3, 4, 5]

b_binario = open('arquivo.pkl', 'wb') # Abre o arquivo serializado e prepara para escrever.
pickle.dump(b, b_binario) # Escreve b serializado dentro do arquivo arquivo.pkl.

b_binario = open('arquivo.pkl', 'rb') # Abre para ler
print(type(pickle.load(b_binario))) # Print o conteúdo do arquivo serializado.

print('\n# Exemplo 7: Cria uma classe, abre o arquivo, serializa em binário, abre para leitura, extrai a informação e desserializa, ao fim print o nome da pessoa.')
class Pessoa:
    nome = 'Marco'
    idade = 44

c = open('arquivo_c.pkl', 'wb')
pickle.dump(Pessoa, c)

c = open('arquivo_c.pkl', 'rb')
retorno = pickle.load(c)

print(retorno.nome)

print('\n# Exemplo 8: Cria uma classe, abre o arquivo, serializa em binário, abre para leitura, extrai a informação e desserializa, ao fim print o nome da pessoa.')
class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
p1 = Pessoas('Caio', 20)

c = open('arquivo_c.pkl', 'ab')
pickle.dump(Pessoa, c)

c = open('arquivo_c.pkl', 'rb')
retorno = pickle.load(c)

print(retorno.nome)

retorno = pickle.load(c)
print(retorno.nome)
