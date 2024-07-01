class Pessoa:
    
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def andar(self):
        print("Andando...")
        
    def falar(self):
        print("Falando...")

class Vendedor(Pessoa):
    def vender(self):
        print("Vendendo...")
        
class Cliente(Pessoa):
    
    def __init__(self, id_cliente, nome, cpf):
        super().__init__(nome, cpf)
        self.id_cliente = id_cliente
    
    def comprar(self):
        print("Comprando...")
        
    def falar(self):
        # super().falar()
        print("Fala fala fala...")
        
        
p1 = Pessoa('Bella', '0123456')
v1 = Vendedor('Elaine', '987654')
c1 = Cliente(20, 'Marco', '004553')

p1.andar()
v1.andar()
c1.andar()

p1.falar()
v1.falar()
c1.falar()

print(c1.id_cliente)
print(c1.nome)
print(c1.cpf)