from actions.operations import Conta, ContaCorrente, Historico, Transacao, Saque, Deposito
from client.client import Cliente, PessoaFisica

class Main:
    def __init__(self):
        self.client = Cliente()
        self.pessoa_fisica = PessoaFisica()

if __name__ == "__main__":
    main = Main()