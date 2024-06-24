class Pessoas:
    tem_olho = True # Atributo de classe
    tem_boca = True
    
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

p1 = Pessoas('Marco', 44, '00455360901')       
p2 = Pessoas('Elaine', 40, '04065737940')

print(p1.nome)
print(p2.nome)

p1.logar_no_sistema()
p2.logar_no_sistema()

p1.tem_boca()