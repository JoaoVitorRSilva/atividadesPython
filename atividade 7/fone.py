from classe import Fones

fone_Mae = Fones("Mae:")
fone_Pai = Fones("Pai:")
fone_Joao = Fones("Jão:")
fone_Maria = Fones("Maria:")
fone_Paula = Fones("Paula:")
fone_Igor = Fones("Igor:")

print("Quer ligar para quem?: ",
"\n 0 - ", fone_Mae.fone, "992000000""\n 1 - ", fone_Pai.fone, "990000034""\n 2 -", fone_Joao.fone ,"992074178""\n 3 -", fone_Maria.fone, "990000076""\n 4 - ", fone_Paula.fone, "990000012""\n 5 - ", fone_Igor.fone,"990000075\n")

selecao = int(input("Selecione o número do contato que queres ligar: "))

lista_fones = [fone_Mae, fone_Pai, fone_Joao, fone_Maria, fone_Paula, fone_Igor]
opcao_sel = int(selecao)

for opcao in lista_fones:
    if opcao_sel >= 6:
        print("\n##############################################")
        print("Essa opção não está incluida nos contatos")
        print("##############################################\n")
        break
    if opcao_sel <= 5:
        print("---------------------------------------")
        print("Ligando para", lista_fones[opcao_sel].fone)
        print("---------------------------------------")
        print(lista_fones[opcao_sel].fone, "- Olô...")
        print("---------------------------------------")
        break
