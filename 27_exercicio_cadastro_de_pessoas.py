pessoas = []

while True:
    decisão = int(input('Digite 1 para cadastrar uma pessoa e 2 para sair: '))
    if decisão == 2:
        break

    pessoa = {'nome': input("Digite o nome: "), 
              'idade': input("Digite a idade: "), 
              'altura': input("Digite a altura: ")}
    
    pessoas.append(pessoa)

    print(pessoas)