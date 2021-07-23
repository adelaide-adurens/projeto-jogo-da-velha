import re

#Função exibeTabuleiro é chamada toda vez que se quer mostrar o tabuleiro e as posições já preenchidas ao usuário.
def exibeTabuleiro(tabuleiro):
    print(*tabuleiro[0][0],*tabuleiro[0][1], *tabuleiro[0][2])
    print(*tabuleiro[1][0],*tabuleiro[1][1], *tabuleiro[1][2])
    print(*tabuleiro[2][0],*tabuleiro[2][1], *tabuleiro[2][2])

# Função entradaValida recebe o input do usuário e verifica se está entre as opções válidas, retornando True ou False.
def entradaValida(entrada):
    valido = True
    entradasValidas = ["1", "2", "3"]
    if entrada not in entradasValidas:
        valido = False
        print("Jogada Inválida.")
        exibeTabuleiro(listaTabuleiro)
        
    return valido   

#Função posicaoJogada perguntará a posição que o jogador quer colocar seu marcador. 
# Recebe o número da jogada e retorna a posição da mesma.
def posicaoJogada(n):
    jogador = ''
    if n % 2 != 0:
        jogador = 'X'
    else:
        jogador = 'O'
    #a variável 'n' é usada para decidir se é o jogador 1 (X) ou jogador 2    
    jogada = [] 
        
    opcao = ['linha', 'coluna']

    while jogada in (listaJogadas) or jogada == []:

        n = 0
        while n <= 1:
            #nesse laço recebe-se a opção de posição do jogador e verifica-se se é válida com a Função entradaValida
            jogadaInvalida = False
            while jogadaInvalida == False:
                jogadaOpcao = input(f"Em que {opcao[n]} você quer colocar seu {jogador}? Digite '1', '2' ou '3'.")    
                jogadaInvalida = entradaValida(jogadaOpcao)
            jogada.append(int(jogadaOpcao))
            n+=1
        #nesse if eu verifico se a opção de posição do jogador, apesar de válida, já não está ocupada
        if jogada in (listaJogadas):
            jogada = []
            print("Essa posição do tabuleiro já está ocupada. Por favor, tente outra jogada.")
            exibeTabuleiro(listaTabuleiro)
    listaJogadas.append(jogada)
        
    return jogada    

#Função recebe o número da jogada e as coordenadas de posição para poder retornar a alteração do tabuleiro com a jogada.
def tabuleiro (n, jogadaLinha, jogadaColuna):    
    jogador = ''
    if n % 2 != 0:
        jogador = 'X'
    else:
        jogador = 'O'
    
    fim = '_'
    if jogadaLinha == 3:
        fim = ' '

    barra = '| '
    if jogadaColuna == 1:
        barra = ''

    listaTabuleiro[jogadaLinha-1][jogadaColuna-1] = [barra+jogador+fim]

#Função recebe a string da posição no tabuleiro e retorna somente o marcador do jogador para ser usado nas funções que verificam o resultado do jogo.
def remover(texto):
    charRemover = "[ |_]"
    elementNovo = re.sub(charRemover,'',texto)
    
    return elementNovo

#Função que recebe as posições do tabuleiro e o marcador para verificar vitórias nas linhas dos tabuleiros.
def linhasIguais(tabuleiro, jogador):
    ganhou = False
    for element in tabuleiro:
        if remover(element[0][0]) == remover(element[1][0]) and remover(element[1][0]) == remover(element[2][0]) and remover(element[2][0]) == jogador:
            ganhou = True
    return ganhou

#Função que recebe as posições do tabuleiro e o marcador para verificar vitórias nas colunas dos tabuleiros.
def colunasIguais(tabuleiro, jogador):
    ganhou = False
    n = 0
    while n <= 2:
        if remover(tabuleiro[0][n][0]) == remover(tabuleiro[1][n][0]) and remover(tabuleiro[1][n][0]) == remover(tabuleiro[2][n][0]) and remover(tabuleiro[2][n][0]) == jogador:
            ganhou = True
        n+=1 
    return ganhou

#Função que recebe as posições do tabuleiro e o marcador para verificar vitórias nas diagonais dos tabuleiros.
def diagonal(tabuleiro, jogador):
    ganhou = False
    if remover(tabuleiro[0][0][0]) == remover(tabuleiro[1][1][0]) and remover(tabuleiro[1][1][0]) == remover(tabuleiro[2][2][0]) and remover(tabuleiro[2][2][0]) == jogador:
        ganhou = True
    elif remover(tabuleiro[0][2][0]) == remover(tabuleiro[1][1][0]) and remover(tabuleiro[1][1][0]) == remover(tabuleiro[2][0][0]) and remover(tabuleiro[2][0][0]) == jogador:
        ganhou = True
    return ganhou

#Recebe o número da jogada e utiliza outras funções para analisar o resultado do jogo a partir da 5ª jogada.
def vitoria(n):
    acabou = False
    if n >=5:
        if linhasIguais(listaTabuleiro, 'X') or colunasIguais(listaTabuleiro, 'X') or diagonal(listaTabuleiro, 'X'):
            print("Parabéns o Jogador 1 ganhou!")
            acabou = True
        elif linhasIguais(listaTabuleiro, 'O') or colunasIguais(listaTabuleiro, 'O') or diagonal(listaTabuleiro, 'O'):
            print("Parabéns o Jogador 2 ganhou!") 
            acabou = True
        elif n == 9:
            print("Deu velha!")
    return acabou   

# Código principal
listaTabuleiro = [
    [['__'],['| __'],['| __']],
    [['__'],['| __'],['| __']],
    [['  '],['|   '],['|   ']]
]

listaJogadas = []
n=1

exibeTabuleiro(listaTabuleiro)

#Laço que se repete por 9 vezes (número de jogadas possíveis) e chama as funções para posicionar as jogadas e verificar o resultado do jogo.
while n < 10:
    posicaoTabuleiro = posicaoJogada(n)
    tabuleiro(n,posicaoTabuleiro[0], posicaoTabuleiro[1])
    exibeTabuleiro(listaTabuleiro)
    acabou = vitoria(n)
    if acabou == True:
        break

    n +=1


