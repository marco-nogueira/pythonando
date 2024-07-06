from datetime import datetime

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        
class Produtos:
    def __init__(self, id, nome, preco, categoria: Categoria):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        
class Estoque:
    def __init__(self, id, produto: Produtos, quantidade):
        self.id = id
        self.produto = produto
        self.quantidade = quantidade
        
class Venda:
    def __init__(self, id, itensVendidos: Produtos, vendedor, comprador, quantidadeVendida, data = datetime.now()):
        self.id = id
        self.data = data
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        
class Fornecedor:
    def __init__(self, id, nome, cnpj, telefone, endereco, categoria: Categoria):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.enedereco = endereco
        self.categoria = categoria
    
class Pessoa:
    def __init__(self, id, nome, cpf, telefone, email, endereco):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, clt, id, nome, cpf, telefone, email, endereco):
        self.clt = clt
        super(Funcionario, self).__init__(id, nome, cpf, telefone, email, endereco)
        
class Cliente(Pessoa):
    def __init__(self, id, nome, cpf, telefone, email, endereco, numeroFidelizacao):
        self.numeroFidelizacao = numeroFidelizacao
        super(Cliente, self).__init__(id, nome, cpf, telefone, email, endereco)
