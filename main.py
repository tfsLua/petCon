''' 
Nosso projeto da Pet.Con vai entrar aqui tá. As divisões vão ser feitas por sessão.

'''

''' LOGIN '''

class Usuario:   
    def __init__(self, firstName, lastName,  email, senha):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.senha = senha

    def confirmar_senha(self, senha_verificacao):
        return self.senha == senha_verificacao 


def cadastrar_usuario():
    firstName = input("Digite o nome do usuário: ")
    lastName = input("Digite seu último nome: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")
    
    novo_usuario = Usuario(firstName, lastName, email, senha)
    return novo_usuario

usuarios_cadastrados =[]


class Abrigo:
    def __init__(self, abrigoName, contato, endereco, foto):
        self.abrigoName = abrigoName
        self.contato = contato
        self.endereco = endereco
        self.foto = foto



def cadastrar_abrigo():
    abrigoName = input("Qual o nome do seu abrigo? ")
    contato = input("Número de contato: ")
    endereco = input("Endereço do abrigo: ")
    
    novo_abrigo = Abrigo(abrigoName, contato, endereco)

    return novo_abrigo

abrigos_cadastrados = []


def login_usuario(usuarios):
    email = input("Digite seu email: ")
   

    while True: 
        senha_passada = input("Digite a senha: ")
        for usuario  in usuarios:
            if usuario.email == email:
                if usuario.confirmar_senha(senha_passada):
                    print("Bem vindo a nossa plataforma!")
                    return usuario
                
                else:
                    print("Senha ou Email incorretos, refaça o login")
                    break

def opcao1_logado():
    print("voce escolheu 1")
    # PARTE DO CODIGO PARA ADICIONAR UM NOVO PET
def opcao2_logado():
    print("você escolheu 2")
    # PARTE DO CODIGO PARA ADOTAR UM PET
def opcao3_logado():
    print("você escolheu 3")
    # PARTE DO CODIGO PARA ALTERAR INFORMACOES DO PET 
def opcao4_logado():
    print("você escolheu 4")
    # PARTE DO CODIGO PARA EXCLUIR UM PET
def opcao5_logado():
    print("você escolheu 5")
    # PARTE DO CODIGO PARA VER OS PETS DISPONIVEIS PARA ADOÇÃO
def opcao6_logado():
    print("você escolheu 6")
    # PARTE DO CODIGO PARA VER ABRIGOS DISPONIVEIS
def opcao7_logado():
    print("você escolheu 7")      
    # PARTE DO CODIGO PARA SAIR     

def opcao1():
    print("Bem vindo a nossa plataforma.")
    novo_usuario = cadastrar_usuario()
    usuarios_cadastrados.append(novo_usuario)
   
    
def opcao2():
   
    print("Você escolheu a opção 2.")
    usuario_logado = login_usuario(usuarios_cadastrados)
    if usuario_logado:
        print("Login bem-sucedido!")

        while True:
            print(" \n 1 - Adicionar novo Pet \n \n 2 - Adotar um Pet \n \n 3 - Alterar informações do pet \n \n 4 - Excluir um Pet \n \n 5 - Ver os pets disponiveis para adoção \n \n 6 - Ver abrigos disponíveis \n \n 7 - Encerrar a Sessão \n")
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
        
            else:
                print("Digite um valor válido")
  
    
        

        




        
    else:
        print("Falha no login. Verifique suas credenciais e tente novamente.")


def opcao3():
    novo_abrigo = cadastrar_abrigo()
    abrigos_cadastrados.append(novo_abrigo)

    

while True:
    print("Bem vindo a Pet.Con o que você deseja fazer?")
    print("\n1 - Cadastrar novo Usuário\n  \n2 - Login\n \n3 - Cadastrar novo Abrigo\n")
    escolha = input()

    if  escolha == '1':
        opcao1()
    elif escolha == '2':
        opcao2()
        break
    elif escolha == '3':
        opcao3()
   
    else:
        print("Opção inválida.")

