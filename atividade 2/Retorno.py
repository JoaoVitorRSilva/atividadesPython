def cria_conta(idd, nick, cash, level):
    conta = {'idd': idd, 'nick': nick, 'cash': cash, 'level': level}
    return conta

def pay(conta, valor):
    conta['cash'] += valor

def reembolso(conta, valor):
    if (conta['cash'] < valor):
        print('Cash atual é', conta['cash'],', o valor da tentativa de reembolso foi,', valor)
        print('Valor Invalido')
    else:
        print('Cash atual é,', conta['cash'],', o valor do reembolso foi,', valor)
        print('Valor Reembolsado')
        conta['cash'] -= valor
        return True
    
def uplevel(conta, valor):
    conta['level'] += valor

def extrato(conta):
    print('Conta\n Id:',conta['idd'], '\n  Nick:',conta['nick'], '\n   Cash:',conta['cash'], '\n    Level:',conta['level'])

contaJao = cria_conta('9391-0', 'Jao', 2000.0, 124.0)
reembolso(contaJao, 1540.0)
uplevel(contaJao, 5)
extrato(contaJao)
