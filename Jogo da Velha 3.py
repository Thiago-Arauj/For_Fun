# Jogo da Velha

Table = [['0/0', '0/1', '0/2'],
         ['1/0', '1/1', '1/2'],
         ['2/0', '2/1', '2/2']]

Char = ("X", "O")

Modo_de_Jogo = int(input('''
   =======================
    Como deseja jogar?
    [1] Single Player
    [2] Multiplayer
    [0] Não quero jogar
   =======================
     '''))

# ============================================================================
#  Acima definimos variavéis importantes para o jogo num geral
#=============================================================================


def CheckWin2P (Table):

    if Table[0][0] == Table[0][1] == Table[0][2]:
        Modo_de_Jogo = 3

    elif Table[1][0] == Table[1][1] == Table[2][2]:
        Modo_de_Jogo = 3

    elif Table[2][0] == Table[2][1] == Table[2][2]:
        Modo_de_Jogo = 3

    elif Table[0][0] == Table[1][0] == Table[2][0]:
        Modo_de_Jogo = 3

    elif Table[0][1] == Table[1][1] == Table[2][1]:
        Modo_de_Jogo = 3

    elif Table[0][2] == Table[1][2] == Table[2][2]:
        Modo_de_Jogo = 3

    elif Table[0][0] == Table[1][1] == Table[2][2]:
        Modo_de_Jogo = 3

    elif Table[0][2] == Table[1][1] == Table[2][0]:
        Modo_de_Jogo = 3

    else:
        Modo_de_Jogo = 2

    return Modo_de_Jogo

    

def SelecChar (Char):
    P1_Char = input("X ou O? ").upper()
    if P1_Char == Char[0]:
        P2_Char = Char[1]
    elif P1_Char == Char[1]:
        P2_Char = Char[0]

    return P1_Char, P2_Char

# ===========================================================================



# ===========================================================================
# Aqui estão as jogadas dos jogadores humanos
# ===========================================================================

def MovePlayer1 (Table, P1_Char):

    TryAgain = 1
    
    while TryAgain > 0:

        Linha, Coluna = (input(f'''
    Jogador 1, digite o número da casa onde quer jogar
    da forma como está na tela:
   =======
    {Table[0][0]} {Table[0][1]} {Table[0][2]}
    {Table[1][0]} {Table[1][1]} {Table[1][2]}
    {Table[2][0]} {Table[2][1]} {Table[2][2]}
   =======
                     ''').split("/"))
        
        Linha = int(Linha)
        Coluna = int(Coluna)
        
        if Table[Linha][Coluna] not in Char:
            Table[Linha][Coluna] = P1_Char
            TryAgain = 0
        else:
            TryAgain = 1
            print("Você selecionou uma casa inválida, tente de novo!")
    
    return Table

def MovePlayer2 (Table, P2_Char):
    
    TryAgain = 1
    
    while TryAgain > 0:

        Linha, Coluna = (input(f'''
    Jogador 2, digite o número da casa onde quer jogar
    da forma como está na tela:
   =======
    {Table[0][0]} {Table[0][1]} {Table[0][2]}
    {Table[1][0]} {Table[1][1]} {Table[1][2]}
    {Table[2][0]} {Table[2][1]} {Table[2][2]}
   =======
                     ''').split("/"))
        
        Linha = int(Linha)
        Coluna = int(Coluna)
        
        if Table[Linha][Coluna] not in Char:
            Table[Linha][Coluna] = P2_Char
            TryAgain = 0
        else:
            TryAgain = 1
            print("Você selecionou uma casa inválida, tente de novo!")

    return Table

# ============================================================================  

while Modo_de_Jogo > 0:
    Table = [['0/0', '0/1', '0/2'],
             ['1/0', '1/1', '1/2'],
             ['2/0', '2/1', '2/2']]
    
    P1_Char, P2_Char = SelecChar(Char)

    Play_Again = 1
    

        
        
    
    while Modo_de_Jogo == 2:
        MovePlayer1(Table, P1_Char)
        Modo_de_Jogo = CheckWin2P(Table)
        if Modo_de_Jogo == 3:
            break
        MovePlayer2(Table, P2_Char)
        Modo_de_Jogo = CheckWin2P(Table)
    
    if Modo_de_Jogo == 3:

        print("Temos um vencedor!")
        print(f'''
    =======
    {Table[0][0]} {Table[0][1]} {Table[0][2]}
    {Table[1][0]} {Table[1][1]} {Table[1][2]}
    {Table[2][0]} {Table[2][1]} {Table[2][2]}
   =======
        ''')

        Play_Again = int(input('''
   =======================
    Deseja jogar de novo?
    [1] Sim
    [0] Não
       '''))

        if Play_Again ==  1:
            Modo_de_Jogo = int(input('''
    =======================
        Como deseja jogar?
        [1] Single Player
        [2] Multiplayer
        [0] Não quero jogar
    =======================
        '''))
        elif Play_Again == 0:
            print("Tudo bem! Foi um bom jogo.")
            Modo_de_Jogo = 0
        
