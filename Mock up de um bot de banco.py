#Mock up de um bot de banco

reselect = ()

saldo_user = 1500

opcao = int(input('''
===============================
Seja Bem-Vindo ao banco Thigas!
Digite a opção que deseja:
[1] Consultar Saldo.
[2] Fazer um saque.
[3] Deixar reclamação.
[4] Falar com atendente.
[0] Cancelar atendimento.
===============================
'''))

# pt-br: Acima temos a variavel que é responsável por fazer a interface com o usuário.
# en-us: Directly above is the variable responsible for being the interface for the user.
  
def Consulta_de_saldo (nome, saldo_user):
    nome = input('''Nome do titular da conta:
                 ''')
    print(f"Olá {nome}! Seu saldo é de {saldo_user}")

def Fazer_Saque (saque):
    saque = int(input("Digite o valor que deseja sacar: "))
    return saque

def reclamcao (opiniao):
    opiniao = input('''
===========================
Pedimos desculpa por não
termos atendido suas 
expectativas, como podemos
melhorar?
===========================
                    ''')
    print("Obrigado por ter compartilhado conosco sua opinião!")
    return opiniao

def redirecionamento ():
    print("Tudo bem! Iremos te direcionar para um de nossos atendentes")

# pt-br: Acima nós definimos todas as funções a serem utilizadas na nossa função principal.
# en-us: Above we've defined all functions we'll be using in our main function.
    
def selecao (reselect):
    reselect = int(input('''
===============================
Podemos te ajudar com mais
alguma coisa:
[1] Consultar Saldo.
[2] Fazer um saque.
[3] Deixar reclamação.
[4] Falar com atendente.
[0] Cancelar atendimento.
===============================
          '''))
    return reselect

# pt-br: Aqui definimos a função de reseleção, onde o usuário poderá decidir se contrinua usando a interface ou se irá encerrar o programa.
# en-us: Here we have our reselection function, where the user will be able to choose another option to continue or end the program.

def main(opcao):
    nome = ()
    saque = ()
    opiniao = ()

    if opcao == 1:
        Consulta_de_saldo(nome, saldo_user)
    elif opcao == 2:
        valor = Fazer_Saque(saque)
        if valor > saldo_user:
            print("Seu saldo não é suficiente para essa operação.")
        else:
            saldo_novo = saldo_user - valor
            print(f"Você sacou com sucesso o valor de {valor}. Seu novo saldo é de {saldo_novo}")
    elif opcao == 3:
        reclamcao(opiniao)
    else:
        redirecionamento()

# pt-br: Aqui nós definimos nossa função principal que a depender da opção selecionada irá rodar a opção adequada.
# en-us: Here we'll be defining our main function which will be responsible for running our entire code based on the option we choose.
    
while opcao > 0:
    main(opcao)
    opcao = selecao(reselect)
else:
    print("Volte sempre!")

# pt-br: Aqui temos nosso loop que se encerra quando o usuário digitar 0 na reseleção.
# en-us: Here we have our loop that ends when the user chooses 0 on the reselection function.