from abc import ABC

import conta


class Pessoa(ABC):
    def __init__(self, nome, cpf): 
        self._nome = nome 
        self._cpf = cpf
    
    @property 
    def getNome(self): 
        return self._nome
    @getNome.setter
    def setNome(self,nomeNovo):
        self._nome = nomeNovo
        return self._nome 

    @property 
    def getCpf(self): 
        return self._cpf
    @getCpf.setter
    def setCPF(self,cpfNovo):
        self._cpf = cpfNovo
        return self._cpf

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.getNome!r}, {self._cpf!r}'
        return f'{class_name}({attrs})'
        
class Cliente(Pessoa):
    def __init__(self, nome, cpf,):
        super().__init__(nome, cpf)
        self.conta: conta.Conta | None = None
 

if __name__ == '__main__':
    cliente = Cliente("Rodrigo", 123456789)
    cliente.conta = conta.ContaCorrente("002", '12008', 123)
    print(cliente.__repr__())
    print(cliente.conta.__repr__())
    print(10*'-')
    cliente2 = Cliente("maria", 123456789)
    cliente2.conta = conta.ContaCorrente("002", '12008', 123)
    print(cliente2.__repr__())
    print(cliente2.conta.__repr__())
