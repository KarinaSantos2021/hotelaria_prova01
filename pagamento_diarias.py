#Criei a classe Cliente, para que quando uma diária for paga, seno exclusivamente pelo cliente ou nao

from Cliente import Cliente
class Pagamento(Cliente):
    def _init_(self, nome, diaria1, diaria2, diaria3, diaria4,  forma_pagamento, data_execucao):
        self.nome=nome
        self.diaria1=diaria1
        self.diaria2=diaria2
        self.diaria3=diaria3
        self.diaria4=diaria4
        self.forma_pagamento=forma_pagamento
        self.data_execucao= data_execucao

        def Pagar(self):
            print(self.diaria1, self.diaria2, self.diaria3, self.diaria4)

            def total(self):
                print(self.forma_pagamento, self.data_execucao)




