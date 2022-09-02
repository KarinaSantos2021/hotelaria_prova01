##Criei a classe cliente, para que o  hóspede possa ser identificado no momento em que ocupa um quarto, mesmo
#que este seja pago por outro cliente, e se caso nao for, sera necessario fazer o cadastro


from Cliente import Cliente
class reserva(Cliente):
    def _init_(self, nome, data_check_in, data_checkout, novo_cadastro):
        self.nome= nome
        self.data_check_in= data_check_in
        self.data_checkout= data_checkout
        self.novo_cadastro= novo_cadastro

    def reserva_dairia(self):
           print(self.nome, self.data_inicio, self.data_final)

    def Realizar_cadastro( self):
        self.novo_cadastrop4
