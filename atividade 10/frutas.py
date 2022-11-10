from classe import Frutas

frutas_0 = Frutas("Abacate")
frutas_1 = Frutas("Maça")
frutas_2 = Frutas("Laranja")
frutas_3 = Frutas("Abacaxi")
frutas_4 = Frutas("Açai")
frutas_5 = Frutas("Acerola")
frutas_6 = Frutas("Amora")
frutas_7 = Frutas("Banana")
frutas_8 = Frutas("Carambola")
frutas_9 = Frutas("Cereja")

print("Bem-vindo(a)! Temos varias frutas para você")
cliente = input("Digite seu nome para iniciarmos: ")
print(cliente, "Temos 10 opções de frutas para você: ",
"\n 0 - ", frutas_0.frutas, "\n 1 - ", frutas_1.frutas,"\n 2 -", frutas_2.frutas,"\n 3 -", frutas_3.frutas, "\n 4 - ", frutas_4.frutas, "\n 5 - ", frutas_5.frutas, "\n 6 - ", frutas_6.frutas, "\n 7 - ", frutas_7.frutas, "\n 8 - ", frutas_8.frutas, "\n 9 - ", frutas_9.frutas)

selecao = int(input("Selecione o número da fruta que lhe interessa: "))

lista_frutas = [frutas_0, frutas_1, frutas_2, frutas_3, frutas_4, frutas_5, frutas_6, frutas_7, frutas_8, frutas_9]
opcao_sel = int(selecao)

for opcao in lista_frutas:
    if opcao_sel >= 10:
        print("\n##############################################")
        print("Essa opção não está incluida no nosso catálogo")
        print("##############################################\n")
        break
    if opcao_sel <= 9:
        print("---------------------------------------")
        print("Olá" ,cliente, "sua fruta escolhida foi", lista_frutas[opcao_sel].frutas)
        print("---------------------------------------")
        print("Obrigado por comprar na nossa vendinha!\n")
        break
