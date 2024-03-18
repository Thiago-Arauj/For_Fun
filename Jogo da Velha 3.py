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

Win_Condition = (Table[0][0] == Table[0][1] == Table[0][2] or
                 Table[1][0] == Table[1][1] == Table[2][2] or
                 Table[2][0] == Table[2][1] == Table[2][2] or
                 Table[0][0] == Table[1][0] == Table[2][0] or
                 Table[0][1] == Table[1][1] == Table[2][1] or
                 Table[0][2] == Table[1][2] == Table[2][2] or
                 Table[0][0] == Table[1][1] == Table[2][2] or
                 Table[0][2] == Table[1][1] == Table[2][0])

print(type(Win_Condition))

# ============================================================================
#  Acima definimos variavéis importantes para o jogo num geral
#=============================================================================


def CheckWin2P (Table, Win_Condition):
    
    if Win_Condition == True:
        print("Temos um vencedor!")
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
        CheckWin2P(Table, Win_Condition)
        MovePlayer2(Table, P2_Char)
        CheckWin2P(Table, Win_Condition)
        

