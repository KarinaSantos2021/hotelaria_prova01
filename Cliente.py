#fiz a classe clientes, em  que tera os campos: nome, telefone, reserva e fim_reserva, como tambem a data de inicio e a data final

from login import Login
class Cliente(Login):
    def _init_(self, nome, cpf, email, telefone, data_reserva, fim_reserva):
            self.nome = nome
            self.cpf= cpf
            self.email = email
            self.telefone= telefone
            self.data_reserva= data_reserva
            self.fim_reserva= fim_reserva


            def reserva_Cliente(self):
                print("'")