''' LOGIN '''

class Usuario:   
    def __init__(self, firstName, lastName, email, senha, aptSize):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.senha = senha
        self.aptSize = aptSize

    def confirmar_senha(self, senha_passada):
        return self.senha == senha_passada
    
    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        print("Senha alterada com sucesso!")

def cadastrar_usuario():
    firstName = input("Digite o nome do usuário: ")
    lastName = input("Digite seu último nome: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")
    aptSize = input("Quantos m² sua casa ou apt têm?")
    
    novo_usuario = Usuario(firstName, lastName, email, senha, aptSize)
    return novo_usuario

usuarios_cadastrados = []
usuario_predefinido = Usuario("jacio", "filho", "jacioalves6", "jacioalves", 60)


usuarios_cadastrados.append(usuario_predefinido)

def recuperar_senha(email):
    for usuario in usuarios_cadastrados:
        if usuario.email == email:
            nova_senha = input("Digite a nova senha: ")
            usuario.alterar_senha(nova_senha)
            return
    print("Email não encontrado.")

def match(aptSize):
    melhor_opcao = None
    for pet in pets_cadastrados:
        if int(aptSize) >= 60 and pet.tamanho.upper() == 'G':
            melhor_opcao = pet
        elif 40 <= int(aptSize) < 60 and pet.tamanho.upper() == 'M':
            melhor_opcao = pet
        elif  int(aptSize) < 40 and pet.tamanho.upper() == 'P':
            melhor_opcao = pet
    return melhor_opcao

           

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
    def __init__(self, nome, idade, raca, abrigo, tamanho):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.abrigo = abrigo
        self.tamanho = tamanho

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
pets_predefinidos = [
    Pet("Bolinha", "3", "Poodle", "Abrigo A", "P"),
    Pet("Rex", "2", "Labrador", "Abrigo B", "M"),
    Pet("Mel", "1", "Vira-lata", "Abrigo C", "G"),
    Pet("Luna", "4", "Shih Tzu", "Abrigo D", "P"),
    Pet("Thor", "2", "Golden Retriever", "Abrigo E", "M"),
    Pet("Zeus", "1", "Pastor Alemão", "Abrigo F", "G"),
    Pet("Maya", "3", "Pinscher", "Abrigo G", "P"),
    Pet("Lucky", "2", "Husky Siberiano", "Abrigo H", "M"),
    Pet("Bela", "1", "Border Collie", "Abrigo I", "G"),
    Pet("Cookie", "4", "Bulldog Francês", "Abrigo J", "P"),
    Pet("Max", "2", "Bulldog Inglês", "Abrigo K", "M"),
    Pet("Simba", "1", "Dálmata", "Abrigo L", "G"),
    Pet("Daisy", "3", "Beagle", "Abrigo M", "P"),
    Pet("Rocky", "2", "Boxer", "Abrigo N", "M"),
    Pet("Molly", "1", "Cocker Spaniel", "Abrigo O", "G"),
    Pet("Jack", "4", "Chihuahua", "Abrigo P", "P"),
    Pet("Buddy", "2", "Dachshund", "Abrigo Q", "M"),
    Pet("Lucy", "1", "Doberman", "Abrigo R", "G"),
    Pet("Rosie", "3", "Rottweiler", "Abrigo S", "P"),
    Pet("Oscar", "2", "Schnauzer", "Abrigo T", "M")
]
pets_cadastrados.extend(pets_predefinidos)
def cadastrar_pet():
    nome = input("Nome do pet: ")
    idade = input("Idade do pet: ")
    raca = input("Raça do pet: ")
    abrigo = input("Abrigo onde o pet está: ")
    tamanho = input("Qual o tamanho do pet? P - Pequeno | M - Médio | G - Grande")
    
    novo_pet = Pet(nome, idade, raca, abrigo, tamanho)
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
    usuario_logado = login_usuario(usuarios_cadastrados)
    if usuario_logado:
        tamanho_apt_usuario = usuario_logado.aptSize
        melhor_opcao = match(tamanho_apt_usuario)
        if melhor_opcao:
            print("Melhor opção para adoção de acordo com o seu lifestyle:")
            print(f"Nome: {melhor_opcao.nome}, Idade: {melhor_opcao.idade}, Raça: {melhor_opcao.raca}, Abrigo: {melhor_opcao.abrigo}, Tamanho: {melhor_opcao.tamanho}")
            print("\nOutros pets disponíveis para adoção:")
            for pet in pets_cadastrados:
                if pet != melhor_opcao:
                    print(f"Nome: {pet.nome}, Idade: {pet.idade}, Raça: {pet.raca}, Abrigo: {pet.abrigo}, Tamanho: {pet.tamanho}")

        else:
            print("Não há pets disponíveis para adoção que atendam aos critérios.")
    else:
        print("Falha no login. Verifique suas credenciais e tente novamente.")

def opcao3_logado():
    print("Você escolheu 3")
    # PARTE DO CÓDIGO PARA ALTERAR INFORMAÇÕES DO PET 
    nome_pet = input("Digite o nome do pet que deseja atualizar: ")
    for pet in pets_cadastrados:
        if pet.nome == nome_pet:
            print("Digite as novas informações do pet:")
            pet.nome = input("Nome do pet: ")
            pet.idade = input("Idade do pet: ")
            pet.raca = input("Raça do pet: ")
            pet.abrigo = input("Abrigo onde o pet está: ")
            pet.tamanho = input("Qual o tamanho do pet? P - Pequeno | M - Médio | G - Grande")
            print("Informações do pet atualizadas com sucesso!")
            return
    print("Pet não encontrado.")

def opcao4_logado():
    print("Você escolheu 4")
    # PARTE DO CÓDIGO PARA EXCLUIR UM PET
    nome_pet = input("Nome do pet a ser removido: ")
    for pet in pets_cadastrados:
        if pet.nome == nome_pet:
            pet.delete_pet(nome_pet)
            break

def opcao5_logado():
    print("Pets disponíveis para adoção:")
    if not pets_cadastrados and not pets_predefinidos:
        print("Não há pets disponíveis para adoção no momento.")
    else:
        if pets_cadastrados:
            print("Pets cadastrados:")
            for pet in pets_cadastrados:
                print(f"Nome: {pet.nome}, Idade: {pet.idade}, Raça: {pet.raca}, Abrigo: {pet.abrigo}, Tamanho: {pet.tamanho}")
        

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
            print()  

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
