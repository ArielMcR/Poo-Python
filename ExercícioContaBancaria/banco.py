from types import *
import conta
import pessoa

class Banco: 
    def __init__(self, agencias: list[int] | None = None, clientes: list[pessoa.Pessoa] | None = None, contas: list[conta.Conta] | None = None):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
    
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agencias!r}, {self.clientes!r},{self.contas!r}'
        return f'{class_name}({attrs})'
    
    def autenticar_agencia(self, conta):
        if conta._agencia in self.agencias:
            # print('Autenticar Agencias', True)
            return True
        # print('Autenticar Agencias', False)
        return False
    def autenticar_cliente(self, cliente):
        if cliente in self.clientes:
            # print('Autenticar Cliente', True)
            return True
        # print('Autenticar Cliente', False)
        return False
    def autenticar_conta(self, conta):
        if conta in self.contas:
            # print('Autenticar Conta', True)
            return True
        # print('Autenticar Conta', False)
        return False
    def autenticar_Conta_cliente(self, conta, cliente):
        if conta is cliente.conta:
            # print('Autenticar conta cliente:',True)
            return True
        # print('Autenticar conta cliente:',False)
        return False


    def autenticar(self, cliente: pessoa.Pessoa, contas: conta.Conta):
        return self.autenticar_agencia(contas) and \
            self.autenticar_cliente(cliente) and \
            self.autenticar_conta(contas) and \
            self.autenticar_Conta_cliente(contas,cliente)

if __name__ == "__main__":
    b1 = Banco()
    cliente1 = pessoa.Pessoa("Rodrigo", 123456789)
    cliente1.conta = conta.ContaCorrente(222, 12008, 123)

    cliente2 = pessoa.Pessoa("Maria", 987654321)
    cliente2.conta = conta.ContaPoupanca(111, 2222, 222)

    cliente3 = pessoa.Pessoa("João", 321456789)
    cliente3.conta = conta.ContaCorrente(222, 3333, 333)

    b1 = Banco()

    b1.clientes.extend([cliente1, cliente2, cliente3])
    b1.agencias.extend([111, 222])
    b1.contas.extend([cliente1.conta, cliente2.conta, cliente3.conta])

    # b1.autenticar(cliente1, cliente1.conta)
    # print(cli)

    if b1.autenticar(cliente1, cliente3.conta): 
            cliente1.conta.sacar(2)
            cliente1.conta.depositar(100)
            cliente1.conta.sacar(10000)
    print("Erro ao acessar a conta")