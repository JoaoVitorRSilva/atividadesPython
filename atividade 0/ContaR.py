print("Faça seu cadastro")
nome = input("Digite seu Nome: ")
nascimento = input("Digite sua data de nascimento: ")
cpf = input("Digite seu CPF: ")
if len(cpf) < 11:
    cpf = cpf.zfill(11)
print("__________")
print("Cadastro")
print("Nome:",nome)
print("Nascimento:", f'{nascimento[:2]}\{nascimento[2:4]}\{nascimento[4:8]}')
print("CPF:", f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
print("__________")
print("Crie uma senha")
senha = input("Digite sua senha: ")
csenha = input("Confirme a senha: ")
print("__________")

while senha != csenha:
    print("As senhas são diferentes\nTente Novamente...")
    senha = input("Digite sua senha: ")
    csenha = input("Confirme a senha: ")
    print("Bem vindo ao site ///, \nFaça login na sua conta")
    print("__________")

print("Conta cadastrado com sucesso.")
user = input("Digite o nome do user:")
while user != nome:
    print("Nome de usuario invalido!!!")
    user = input("Digite o nome do user novamente:")
    print("__________")

lsenha = input("Digite sua senha:")
while lsenha != senha:
    print("Senha invalida!!!")
    lsenha = input("Digite sua senha:")
if lsenha == senha:
    print("Login feito com Sucesso")
