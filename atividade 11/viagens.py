from classe import Locais

local_0 = Locais("China")
local_1 = Locais("Japão")
local_2 = Locais("Russia")
local_3 = Locais("Finlândia")
local_4 = Locais("Afeganistão")

print("Bem-vindo(a)! Temos ofertas para você")
cliente = input("Digite seu nome para iniciarmos: ")
print(cliente, "Temos 5 opções de locais para viagem: ",
"\n 0 - ", local_0.locais, "\n 1 - ", local_1.locais,"\n 2 -", local_2.locais,"\n 3 -", local_3.locais, "\n 4 - ", local_4.locais)

selecao = int(input("Selecione o número do local que lhe interessa: "))

lista_locais = [local_0, local_1, local_2, local_3, local_4]

opcao_sel = int(selecao)

for opcao in lista_locais:
    if opcao_sel >= 5:
        print("\n##############################################")
        print("Essa opção não está incluida no nosso catálogo")
        print("##############################################\n")
        break
    if opcao_sel <= 4:
        print("---------------------------------------")
        print("Olá" ,cliente, "seu local escolhido foi", lista_locais[opcao_sel].locais)
        print("---------------------------------------")
        print("Obrigado, Boa Viagem!\n")
        break
