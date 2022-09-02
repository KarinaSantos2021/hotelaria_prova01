#criar a classe servico para junto com a classe solicitar,o hospede possa solicitar serviços do hotel, como passar roupa e usar a lavanderia
from Solicitação_de_serviço import Solicitar
class Servico(Solicitar):
    def _init_(self,passar_roupa, lavanderia, descricao_servico, valor_servico):
        self.passar_roupa=passar_roupa
        self.lavanderia=lavanderia
        self.descricao_servico
        self.valor_servico
    pass

def Registrar(self):
    print("'")