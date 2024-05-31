nomes = []

while True:
    nome=input('Digite -1 para sair ou cadastre um nome: ')
    
    if nome == '-1':
        break
    else:
        nomes.append(nome)
    
    print('Nomes cadastrados: ',nomes)