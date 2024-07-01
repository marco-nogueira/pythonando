class Pessoas:
    possui_olho = True # Atributo de classe
    possui_boca = True
    raca = 'Ser humano'
    
    def __init__(self, nome, idade, cpf): # Método construtor
        self.nome = nome # Atributo de instância
        self.idade = idade
        self.cpf = cpf
            
    def logar_no_sistema(self): # Method de instância
        
        print(f"{self.nome}, você está logado no sistema")
        
    @classmethod
    def tem_olho(cls): # Método de classe
        print('Sim')
    
    def tem_boca(cls): # Método de classe
        print('Sim')
        
    def andar(cls, velocidade): # Método de classe
        cls.pernas = 2 # Quando o method é chamado então o atributo de classe pernas é criado.
        cls.possui_boca = True # Possui boca fica True
        print(f'Estou andando na velocidade {velocidade} m/s')
    
    @staticmethod
    def e_adulto(idade): # Método stático, apenas método utilitário, não consegue acessar e nem modificar atributo ou método de classe.
        if idade >= 18:
            return True
        else:
            return False

p1 = Pessoas('Marco', 44, '123456789')       
p2 = Pessoas('Elaine', 40, '987654321')

print(p1.nome) # Chamando um atributo de uma instância
print(p2.nome)

p1.logar_no_sistema()
p2.logar_no_sistema()

p1.tem_boca()
print(Pessoas.raca) # Chamando um atributo de classe

p1.possui_boca = False
print(p1.possui_boca)
print(p2.possui_boca)

Pessoas.possui_boca = False
print(p1.possui_boca)
print(p2.possui_boca)

p1.andar(10)
print(p1.pernas)
print(p1.possui_boca)

print(Pessoas.e_adulto(21))