from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('Projeto Mercearia/categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('Projeto Mercearia/categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        print(cls.categoria)    
        
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat
class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('Projeto Mercearia/venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + "|"
                            + venda.itensVendidos.preco + "|"
                            + venda.itensVendidos.categoria + "|"
                            + venda.vendedor + "|"
                            + venda.comprador + "|"
                            + str(venda.quantidadeVendida) + "|"
                            + venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('Projeto Mercearia/venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
            
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        print(cls.venda) 

        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return vend

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('Projeto Mercearia/estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + "|"
                            + produto.preco + "|"
                            + produto.categoria + "|"
                            + str(quantidade))
            arq.writelines('\n')
        
    @classmethod
    def ler(cls):
        with open('Projeto Mercearia/estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
            
            cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
            cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2], i[3])))
        return est

# Cria Categorias
DaoCategoria.salvar('Frutas')
DaoCategoria.salvar('Verduras')
DaoCategoria.salvar('Legumes')
DaoCategoria.ler()

# Cria Vendas
x = Produtos('Banana', '12', 'Frutas')     
y = Venda(x, 'Marco', 'Pedro', '3')
DaoVenda.salvar(y)
a = DaoVenda.ler()
print(a[0].itensVendidos.nome)

# Cria Produto em Estoque
x_estoque = Estoque(x, '200')
DaoEstoque.salvar(x_estoque)
DaoEstoque.ler()