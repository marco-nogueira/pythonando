class Pessoa:
    def andar(self):
        print("Andando...")
        
    def falar(self):
        print("Falando...")

class Vendedor(Pessoa):
    def vender(self):
        print("Vendendo...")
        
class Cliente(Pessoa):
    def comprar(self):
        print("Comprando...")
        
        
p1 = Pessoa()
v1 = Vendedor()
c1 = Cliente()

p1.andar()
v1.andar()
c1.andar()