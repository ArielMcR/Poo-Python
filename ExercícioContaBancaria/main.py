import pessoa, conta
from banco import *


b1 = Banco()
cliente1 = pessoa.Pessoa("Rodrigo", 123456789)
cliente1.conta = conta.ContaCorrente(222, 12008, 123)

cliente2 = pessoa.Pessoa("Maria", 987654321)
cliente2.conta = conta.ContaPoupanca(111, 2222, 222)

cliente3 = pessoa.Pessoa("João", 321456789)
cliente3.conta = conta.ContaCorrente(222, 3333, 333)

b1.clientes.extend([cliente1, cliente2, cliente3])
b1.agencias.extend([111, 222])
b1.contas.extend([cliente1.conta, cliente2.conta, cliente3.conta])

if b1.autenticar(cliente1, cliente3.conta): 
    cliente1.conta.sacar(2)
    cliente1.conta.depositar(100)
    cliente1.conta.sacar(10000)
print("Erro ao acessar a conta")