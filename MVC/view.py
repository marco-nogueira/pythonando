from controller import PessoaController

while True:
    decisao = int(input('Digite 1 para salvar uma pessoa ou digite 2 para ver a pessoa salva'))
    if decisao == 3:
        break
    if decisao == 1:
        nome = input('Digite o nome da pessoa: ')
        idade = int(input('Digite a idade da pessoa: '))
        cpf = input('Digite o cpf da pessoa: ')
        if PessoaController.cadastrar(nome, idade, cpf):
            print('Usuário cadastrado com sucesso')
        else:
            print('Digite valores validos')
        