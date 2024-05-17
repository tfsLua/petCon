''' LOGIN '''

class Usuario:   
    def __init__(self, firstName, lastName, email, senha):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.senha = senha

    def confirmar_senha(self, senha_verificacao):
        return self.senha == senha_verificacao
    
    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        print("Senha alterada com sucesso!")

def cadastrar_usuario():
    firstName = input("Digite o nome do usuário: ")
    lastName = input("Digite seu último nome: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")
    
    novo_usuario = Usuario(firstName, lastName, email, senha)
    return novo_usuario

usuarios_cadastrados = []
usuario_predefinido = Usuario("jacio", "filho", "jacioalves6", "jacioalves")


usuarios_cadastrados.append(usuario_predefinido)

def recuperar_senha(email):
    for usuario in usuarios_cadastrados:
        if usuario.email == email:
            nova_senha = input("Digite a nova senha: ")
            usuario.alterar_senha(nova_senha)
            return
    print("Email não encontrado.")

class Abrigo:
    def __init__(self, abrigoName, contato, endereco, foto=None):
        self.abrigoName = abrigoName
        self.contato = contato
        self.endereco = endereco
        self.foto = foto

def cadastrar_abrigo():
    abrigoName = input("Qual o nome do seu abrigo? ")
    contato = input("Número de contato: ")
    endereco = input("Endereço do abrigo: ")
    foto = input("Link da foto do abrigo (opcional): ")
    
    novo_abrigo = Abrigo(abrigoName, contato, endereco, foto)
    return novo_abrigo

abrigos_cadastrados = []

class Pet:
    def __init__(self, nome, idade, raca, abrigo):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.abrigo = abrigo

    def delete_pet(self, nome):
        pet_found = False
        for pet in pets_cadastrados:
            if pet.nome == nome:
                pets_cadastrados.remove(pet)
                print(f"{nome} removido com sucesso!")
                pet_found = True
                break
        if not pet_found:
            print(f"Pet com nome '{nome}' não encontrado.")

pets_cadastrados = []

def cadastrar_pet():
    nome = input("Nome do pet: ")
    idade = input("Idade do pet: ")
    raca = input("Raça do pet: ")
    abrigo = input("Abrigo onde o pet está: ")
    
    novo_pet = Pet(nome, idade, raca, abrigo)
    pets_cadastrados.append(novo_pet)
    print("Pet cadastrado com sucesso!")

def login_usuario(usuarios):
    while True:
        email = input("Digite seu email: ")
        senha_passada = input("Digite a senha: ")

        for usuario in usuarios:
            if usuario.email == email:
                if usuario.confirmar_senha(senha_passada):
                    print("Bem-vindo(a) à nossa plataforma!")
                    return usuario

        print("Credenciais incorretas. Tente novamente ou digite 'sair' para voltar ao menu principal.")
        resposta = input("Digite 'sair' para voltar ao menu principal ou pressione Enter para tentar novamente: ")
        if resposta.lower() == 'sair':
            break

    return None

def opcao1_logado():
    print("Adicione um pet!")
    cadastrar_pet()

def opcao2_logado():
    print("Você escolheu 2")
    # PARTE DO CÓDIGO PARA ADOTAR UM PET

def opcao3_logado():
    print("Você escolheu 3")
    # PARTE DO CÓDIGO PARA ALTERAR INFORMAÇÕES DO PET 

def opcao4_logado():
    print("Você escolheu 4")
    # PARTE DO CÓDIGO PARA EXCLUIR UM PET
    nome_pet = input("Nome do pet a ser removido: ")
    for pet in pets_cadastrados:
        if pet.nome == nome_pet:
            pet.delete_pet(nome_pet)
            break

def opcao5_logado():
    print("Pets disponiveis para adoção")
    if not pets_cadastrados:
        print("Não há pets disponíveis para adoção no momento.")
    else:
        print("Pets disponíveis para adoção:")
        for pet in pets_cadastrados:
            print(f"Nome: {pet.nome}, Idade: {pet.idade}, Raça: {pet.raca}, Abrigo: {pet.abrigo}")

def opcao6_logado():
    if not abrigos_cadastrados:
        print("Não há abrigos cadastrados no momento.")
    else:
        print("Abrigos cadastrados:")
        for idx, abrigo in enumerate(abrigos_cadastrados, start=1):
            print(f"Abrigo {idx}:")
            print(f"Nome: {abrigo.abrigoName}")
            print(f"Contato: {abrigo.contato}")
            print(f"Endereço: {abrigo.endereco}")
            print()  # Adiciona uma linha em branco entre os abrigos

def opcao7_logado():
    print("Você escolheu 7")
    # PARTE DO CÓDIGO PARA SAIR     

def opcao1():
    print("Bem-vindo(a) à nossa plataforma.")
    novo_usuario = cadastrar_usuario()
    usuarios_cadastrados.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")
   
def opcao2():
    print("Você escolheu a opção 2.")
    usuario_logado = login_usuario(usuarios_cadastrados)
    if usuario_logado:
        while True:
            print("\nEscolha uma opção:\n1 - Adicionar novo Pet\n2 - Adotar um Pet\n3 - Alterar informações do pet\n4 - Excluir um Pet\n5 - Ver os pets disponíveis para adoção\n6 - Ver abrigos disponíveis\n7 - Encerrar a Sessão\n")
            escolha_logado = input()
            
            if escolha_logado == '1':
                opcao1_logado()
            elif escolha_logado == '2':
                opcao2_logado()
            elif escolha_logado == '3':
                opcao3_logado()
            elif escolha_logado == '4':
                opcao4_logado()
            elif escolha_logado == '5':
                opcao5_logado()
            elif escolha_logado == '6':
                opcao6_logado()
            elif escolha_logado == '7':
                opcao7_logado()
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Falha no login. Verifique suas credenciais e tente novamente.")

def opcao3():
    print("Você escolheu a opção 3.")
    novo_abrigo = cadastrar_abrigo()
    abrigos_cadastrados.append(novo_abrigo)
    print("Abrigo cadastrado com sucesso!")
def opcao4():
    print("Você escolheu a opção 4")
    email_recuperacao = input("Digite o email para recuperar a senha: ")
    recuperar_senha(email_recuperacao)

while True:
    print("Bem-vindo(a) à Pet.Con! O que você deseja fazer?")
    print("\n1 - Cadastrar novo Usuário\n2 - Login\n3 - Cadastrar novo Abrigo\n4 - Recuperar Senha\n")
    escolha = input()

    if escolha == '1' :
        opcao1()
    elif escolha == '2':
        opcao2()
    elif escolha == '3':
        opcao3()
    elif escolha == '4':
        opcao4()
    else:
        print("Opção inválida. Tente novamente.")
