from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self,agencia, numConta, saldo:int):
        self._agencia = agencia
        self._numConta = numConta
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valorSaque):
        if self._saldo <= 0: 
            return print("Não é possível realizar o saque, valor em conta é negativo ou igual à 0")
        elif self._saldo < valorSaque: 
            return print("Não é possível realizar o saque, valor em conta é menor que o valor de saque")
        print(f'Saque no valor {valorSaque}R$ foi realizado na conta')
        self._saldo -= valorSaque
        print(f'Seu saldo agora é de {self._saldo}R$')
        return self._saldo

    def depositar(self,valorDeDeposito):
        self._saldo += valorDeDeposito
        print(f'Deposito de {valorDeDeposito} R$ realizado, seu saldo agora é de {self._saldo}')
        return self._saldo
    
    def informacoesDaConta(self):
        return print(f' Agência: {self._agencia}\n Numero da Conta: {self._numConta}\n Saldo: {self._saldo}\n tipo de Conta: {self.__class__.__name__}\n')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self._agencia!r}, {self._numConta!r}, {self._saldo!r})'
        return f'{class_name}{attrs}'


class ContaCorrente(Conta):
    def __init__(self, agencia, numConta, saldo, limite = 1000):
        super().__init__(agencia, numConta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self._saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self._saldo -= valor
            print(f"Saque realizado seu saldo agora é de {self._saldo}")
            return self._saldo

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        print(f"Saque de {valor} foi negado, valor maior que o limite")
    
    def informacoesDaConta(self):
        print( f'Limite: {self.limite}')
        return super().informacoesDaConta()

    def __repr__(self) -> str:
        # print(f"{self.limite}")
        return super().__repr__() 

class ContaPoupanca(Conta):

    def sacar(self, valorSaque):
        super().sacar(valorSaque)
        

if __name__ == "__main__":
    cp1 = ContaPoupanca(1111,222,0)
    # cp1.sacar(1)
    # cp1.depositar(2)
    # cp1.informacoesDaConta()
    print(cp1.__repr__())
    print(10*'-')
    cc1 = ContaCorrente(2222,333,0)
    print(cc1.__repr__())
    # cc1.informacoesDaConta()
    # cc1.sacar(1020)


