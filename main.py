from model.cliente import Cliente
from model.reserva import Reserva
from model.quarto import Quartos
from model.funcionario import Funcionario
from model.aluguel import Aluguel
from model.consumo import Consumo


def menu():
    while True:
        print('-' * 21)
        print('| HOTEL RIO PRETO |')
        print('-' * 21)
        print('(1) - CADASTRAR HOSPEDE')
        print('(2) - REALIZAR RESERVA')
        print('(3) - CADASTRAR QUARTO')
        print('(4) - ALUGAR QUARTO')
        print('(5) - LANÇAR CONSUMO')
        print('(6) - CADASTRAR FUNCIONÁRIOS')
        print('(7) - SAIR')

        res = int(input('Digite uma opção: '))
        print(res)
        if res == 1:
            Cliente.inserir_hospede()
            pass
        elif res == 2:
            Reserva.fazer_reserva()
            pass
        elif res == 3:
            Quartos.inserir_quarto()
            pass
        elif res == 4:
            Aluguel.realizar_aluguel()
            pass
        elif res == 5:
            Consumo.realizar_consumo()
            pass
        elif res == 6:
            Funcionario.inserir_funcionario()
            pass
        elif res == 7:
            break
        else:
            print('Opção invalida!')
            menu()


menu()
