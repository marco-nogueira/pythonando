from model import Pessoa 

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade )+ " " + pessoa.cpf)
            
    @classmethod        
    def ler(cls):
        with open('pessoas.txt', 'r') as arq:
            nome = 'Marco'
            idade = 44
            cpf = '12345678901'
            return Pessoa(nome, idade, cpf)
        
p1 = Pessoa('Marco', 44, '004123')
print(PessoaDal.ler().cpf)