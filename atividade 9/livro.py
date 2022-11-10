from classe import Livros

livros_0 = Livros("Ao Farol (1927)")
livros_1 = Livros("O Rei Lear (1606)")
livros_2 = Livros("Moby Dick (1851)")
livros_3 = Livros("A Divina Comédia (1304—1321)")
livros_4 = Livros("Madame Bovary (1856)")
livros_5 = Livros("Viagem ao Fim da Noite (1932)")
livros_6 = Livros("Ilíada (séc. VIII a.C.)")
livros_7 = Livros("O Livro do Desassossego (1982)")
livros_8 = Livros("Pantagruel (1532)")
livros_9 = Livros("Guerra e Paz (1869)")

print("Bem-vindo(a)! Temos livros para você")
cliente = input("Digite seu nome para iniciarmos: ")
print(cliente, "Temos 10 opções de livros para você: ",
"\n 0 - ", livros_0.livros, "\n 1 - ", livros_1.livros,"\n 2 -", livros_2.livros,"\n 3 -", livros_3.livros, "\n 4 - ", livros_4.livros, "\n 5 - ", livros_5.livros, "\n 6 - ", livros_6.livros, "\n 7 - ", livros_7.livros, "\n 8 - ", livros_8.livros, "\n 9 - ", livros_9.livros)

selecao = int(input("Selecione o número do livro que lhe interessa: "))

lista_livros = [livros_0, livros_1, livros_2, livros_3, livros_4, livros_5, livros_6, livros_7, livros_8, livros_9]

opcao_sel = int(selecao)

for opcao in lista_livros:
    if opcao_sel >= 10:
        print("\n##############################################")
        print("Essa opção não está incluida no nosso catálogo")
        print("##############################################\n")
        break
    if opcao_sel <= 9:
        print("---------------------------------------")
        print("Olá" ,cliente, "seu livro escolhido foi", lista_livros[opcao_sel].livros)
        print("---------------------------------------")
        print("Obrigado, Boa Leitura!\n")
        break
