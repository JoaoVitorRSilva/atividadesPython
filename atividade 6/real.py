from classe import Conta, Real

contaJao = Conta('9391-0', 'Jao', 2000.0, 124.0)
contaJao.reembolso(1540.0)
contaJao.uplevel(5)
contaJao.extrato()

Joao = Real('João', 'Silva', 20)
print('Dados Reais:', Joao.idade)
