from Requisitar_servico import Requisitar_servico
class Requisitar(Requisitar_servico):
    def _init_(self,passar_roupa, lavanderia, requisitar_servico, valor_servico):
        self.passar_roupa= passar_roupa
        self.lavanderia= lavanderia
        self.requisitar_servico= requisitar_servico
        self.valor_servico= valor_servico
    pass

def Registrar(self):
    print("'")