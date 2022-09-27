class Conta:
    def __init__(self, idd, nick, cash, level):
        self.idd = idd
        self.nick = nick
        self.cash = cash
        self.level = level

    def pay(self, valor):
        self.cash += valor

    def reembolso(self, valor):
        if (self.cash < valor):
            print('Cash atual é', self.cash, ', o valor da tentativa de reembolso foi,', valor)
            print('Valor Invalido')
        else:
            print('Cash atual é,', self.cash,', o valor do reembolso foi,', valor)
            print('Valor Reembolsado')
            self.cash -= valor
            return True
        
    def uplevel(self, valor):
        self.level += valor

    def extrato(self):
        print('Conta\n Id:',self.idd, '\n  Nick:', self.nick, '\n   Cash:', self.cash, '\n    Level:', self.level)
from classe import Conta

contaJao = Conta('9391-0', 'Jao', 2000.0, 124.0)
contaJao.reembolso(1540.0)
contaJao.uplevel(5)
contaJao.extrato()
