positions = range(3)  #Define a dimensões do tabuleiro.

#Essa função apenas exibe o tabuleiro.
def exibir_tabuleiro(tabuleiro):
    for p in positions: print(tabuleiro[p])
    
#Essa função apenas valida se a entrada s é um dos valores no iteravel p.
def validar_entrada(s, p):
    return s.isdigit() and (int(s) in p)

#Pede para o usuário entrar com um valor de acordo com o rotulo.
def selecionar(rotulo):
    while True:
      e = input(f"Escolha uma {rotulo}: ")
      if not validar_entrada(e, positions):
          print(f"Erro: {rotulo} inválida!{tuple(positions)}")
          continue
      return int(e)
    
#Retorna a célula (linha, coluna) selecionada pelo usuário.
def selecionar_celula():
    return tuple(selecionar(r) for r in ["linha", "coluna"]) 
    
#Informa qual o jogador da vez.
def informar_jogador(s):
    print(f"Jogador {s}...")
    
#Verifica se uma jogada é ou não válida.
def validar_jogada(l, c, t):
    return all(p in positions for p in {l, c}) and (t[l][c] == "")
   
#Efetua uma jogada para o jogador no tabuleiro. O comportamento do interpretador é iniciar o default apenas na primeira chamada da função.
def jogada(jogador, tabuleiro=[[""]*len(positions) for p in positions]):
    valida = False
    exibir_tabuleiro(tabuleiro)
    while not valida:
        informar_jogador(jogador)
        linha, coluna = selecionar_celula()
        valida = validar_jogada(linha, coluna, tabuleiro)
        if valida:
            tabuleiro[linha][coluna] = jogador
        else:
            print(f"{'-'*3} A posição {(linha, coluna)} já está ocupada, jogue novamente {'-'*3}")
            
    return tabuleiro
    
#Testa um vetor para saber se tem todos os caracteres iguais e se sim retorna o caractere senão retorna None 
def vetor_vencedor(v):
    if v.count(v[0]) == len(v):
        if v[0] != "" : 
            #print(f"Vencedor jogador {v[0]}.")
            return v[0]
    
#Testa cada uma das linhas do tabuleiro para saber se tem todos os caracteres iguais e se sim retorna o caractere senão retorna None    
def verificar_linhas(tabuleiro):
    for linha in tabuleiro:
        if vetor_vencedor(linha):
            return linha[0]

#Testa cada uma das colunas do tabuleiro para saber se tem todos os caracteres iguais e se sim retorna o caractere senão retorna None 
def verificar_colunas(tabuleiro):
    for c in positions:
        coluna = [linha[c] for linha in tabuleiro]
        if vetor_vencedor(coluna):
            return coluna[0]
    
#Testa a diagonal principal do tabuleiro para saber se tem todos os caracteres iguais e se sim retorna o caractere senão retorna None    
def verificar_diagonal_principal(tabuleiro):
    diagonal = [tabuleiro[p][p] for p in positions]
    if vetor_vencedor(diagonal):
        return diagonal[0]

#Testa a diagonal secundária do tabuleiro para saber se tem todos os caracteres iguais e se sim retorna o caractere senão retorna None
def verificar_diagonal_secundaria(tabuleiro):
    diagonal = [tabuleiro[positions[-1] - p][p] for p in positions]
    if vetor_vencedor(diagonal):
        return diagonal[0]
        
#Testa o a procura de um vencedor, se houver um vencedor o retorna senão retorna None.
def vencedor(tabuleiro):
    v = (verificar_linhas(tabuleiro) or 
         verificar_colunas(tabuleiro) or
         verificar_diagonal_principal(tabuleiro) or
         verificar_diagonal_secundaria(tabuleiro))
    if v: 
        print(f"{'-'*10} Jogo encerrado {'-'*10}")
        print(f"Vencedor jogador {v}.")
        exibir_tabuleiro(tabuleiro)
        return v
  
#Closure biestado, a cada execução da função seu retorno alterna entre 0 e 1.
def flag():
    f = True
    def __flag():
        nonlocal f
        f = not f
        return int(f)
    return __flag
    
flag = flag() #Obtém o closure

while not vencedor(jogada("XO"[flag()])):
    print(f"{'-'*10} Jogada encerrada {'-'*10}")