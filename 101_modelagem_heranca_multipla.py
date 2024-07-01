class Animal():
    
    def andar(self):
        print("Estou andando...")
        
class Felino(Animal):
    
    def info(self):
        print("Sou um felino...")
        
class Gato(Felino):
    
    def miar(self):
        print("Estou miando...")
    
    
g1 = Gato()
g1.andar()
g1.info()
g1.miar()