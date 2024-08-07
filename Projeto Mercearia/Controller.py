from Models import Categoria, Estoque, Produtos, Fornecedor, Pessoa, Funcionario, Venda
from DAO import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
                
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso')
        else:
            print('A categoria que deseja cadastrar já que existe')
            
    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        
        if len(cat) <= 0:
            print('Categoria não encontrada')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')
        # TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            
            with open('Projeto Mercearia/categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        
        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))
        
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x),x))
                print('A alteração foi efetuada com sucesso')
                # TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            else:
                print('A categoria que deseja alterar já existe')
                
        else:
            print('A categoria que deseja alterar não existe')
            
        with open('Projeto Mercearia/categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')
            
    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if(len(categorias)) == 0:
            print('Não há categorias cadastradas')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')
                
class ControllerEstoque:
    def cadastrarProdutos(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))
        
        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print('O produto já existe no estoque')
        else:
            print('A categoria não existe')
                
        
        
        
# a = ControllerCategoria()
# a.cadastrarCategoria('Frutas')
# a.removerCategoria('Frutas')
# a.alterarCategoria('Frutas', 'Carnes')
# a.mostrarCategoria()

a = ControllerEstoque()
a.cadastrarProdutos('Maçã', '5', 'Frutas',  10)
