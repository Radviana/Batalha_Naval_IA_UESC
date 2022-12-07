import numpy as np
from copy import deepcopy
from create_set_ship.create_set_ship import *

agua = "~"
falha = "X"
acerto = "*"
barco = '1' # '^'

# Variáveis MAPA
tamanho = 10
vida_jog , vida_ia = (45, 45)

mapa_ia_consulta = np.zeros((tamanho, tamanho), dtype=int) # Consulta
mapa_jogador_consulta = np.zeros((tamanho, tamanho), dtype=int) # Consulta

mapa_ia_visivel = np.zeros((tamanho, tamanho), dtype=int) # Visivel
mapa_jogador_visivel = np.zeros((tamanho, tamanho), dtype=int) # Visivel

# Navios
submarino = [criar_navio(1, 1, [1])]
corvetas = [criar_navio(2, 1, [1, 2]), criar_navio(1, 2, [1, 2])]
fragatas = [criar_navio(3, 1, [1, 2, 3]), criar_navio(1, 3, [1, 2, 3])]
cruzadores = [criar_navio(4, 1, [1, 2, 3, 4]), criar_navio(1, 4, [1, 2, 3, 4])]
porta_avioes = [criar_navio(5, 1, [1, 2, 3, 4, 5]), criar_navio(1, 5, [1, 2, 3, 4, 5])]
hidro_avioes = [criar_navio(2, 3, [2, 4, 6]), criar_navio(2, 3, [1, 3, 5]), criar_navio(3, 2, [1, 4, 5]),
               criar_navio(3, 2, [2, 3, 6])]

qtd_submarino = 3
qtd_corveta = 2
qtd_fragata = 3
qtd_cruzador = 1
qtd_porta_aviao = 1
qtd_hidro_aviao = 2

# Variáveis IA
acerto_ia = False
posicao_acerto = None

def substitui_print(element):
    if element == '0':
        element = agua
    elif element == '1':
        element = barco
    elif element == '2':
        element = acerto
    elif element == '3':
        element = 'O'
    else:
        element = falha
        
    return element

def printa_navio(ship):
    row, column = ship.shape
    
    for i in range(row):
        for j in range(column):
            if ship[i][j] == 0:
                print("  ", end='')
            else:
                print(" 1", end='')
        print()
    print()
    
def printa_mapa() -> None:
    #numbers = [i for i in range(1, 11)]
    print("\t   IA\t\t\t   Player")
    print("    1 2 3 4 5 6 7 8 9 10 || 1 2 3 4 5 6 7 8 9 10")
    print("    _____________________||_____________________")
    for linha in range(tamanho):
        if linha == 9:
            espaco = " " * 1
        else:
            espaco = " " * 2 
          
        tmp_ia = list(map(str, list(mapa_ia_visivel[linha])))
        tmp_jogador = list(map(str, list(mapa_jogador_visivel[linha])))
            
        tmp_ia = list(map(substitui_print, tmp_ia))
        tmp_jogador = list(map(substitui_print, tmp_jogador))
            
        tmp_ia = ' '.join(tmp_ia)
        tmp_jogador = ' '.join(tmp_jogador) 
             
        print(f"{linha + 1}{espaco}|{tmp_ia}  || {tmp_jogador} |")
    print("   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    
def coloca_navios(mapa):
    navios = [submarino, corvetas, fragatas, cruzadores, porta_avioes, hidro_avioes]
    nomes_navios = ['Submarino', 'Corveta', 'Fragata', 'Cruzador', 'Porta avião', 'Hidro Avião']
    qtd_navios = [qtd_submarino, qtd_corveta, qtd_fragata, qtd_cruzador, qtd_porta_aviao, qtd_hidro_aviao]
    
    for i in len(navios):
        op = -1
        while True:
            print(f"Colocando {nomes_navios}...")
            x_navio = int(input(f"Digite a posicão X do {nomes_navios[i]}: "))
            y_navio = int(input(f"Digite a posicão Y do {nomes_navios[i]}: "))
            orientacao_navio = int(input(f"Digite a orientação do {nomes_navios[i]}: "))
            print(f"X = {x_navio}")
            print(f"Y = {y_navio}")
            print(f"orientação = {orientacao_navio}")
            print(f"Navio = {navios[orientacao_navio]}")
            
            tmp_map = deepcopy(mapa)
            mapa = adicionar_navio(navios[orientacao_navio], (x_navio, y_navio), mapa)
            
            # Incrementa a quantidade de determinado návio no mapa
            if mapa != tmp_map:
                qtd_navios[i] += 1
            
            op = input("Digite 0 para Sair e qualquer outra tecla para continuar: ")
            print()
            
            if op == '0':
                break
      
    return mapa
    
def get_empty_positions(map):
    posicoes_vazias = set()
    qtds_navios = [qtd_submarino, qtd_corveta, qtd_fragata, qtd_cruzador, qtd_porta_aviao]
    limites_for = [10, 9, 8, 7, 6]
    qtds_vazios = [1, 2, 3, 4, 5]
    
    # Verifica posições livres návios, exceto hidro-aviões
    for qtd_navio, limite_for, qtd_vazio in zip(qtds_navios, limites_for, qtds_vazios):
        if qtd_navio > 0:
            for i in range(limite_for):
                for j in range(limite_for):
                    qtd_vazio_vertical = 0
                    qtd_vazio_horizontal = 0
                
                    for k in range(limite_for - 1):
                        if map[k][i] == 0:
                            qtd_vazio_vertical += 1
                        if map[i][k] == 0:
                            qtd_vazio_horizontal += 1
                    
                        if qtd_vazio_horizontal == qtd_vazio or qtd_vazio_vertical == qtd_vazio:
                            posicoes_vazias.add((i, j))
                    qtd_vazio_vertical, qtd_vazio_horizontal = 0, 0                          
         
    return posicoes_vazias     
    
def ataque(qtds_navios: list):
    print("Faça 3 ataques: ")
    for i in range(3):
        printa_mapa()
        
        while True:
            print(f"\nAtaque {i + 1}")
            
            x = int(input("Informe a linha: ")) - 1
            y = int(input("Informe a coluna: ")) - 1
            
            if map[x][y] == 0:
                mapa_ia_visivel[x][y] = -1
                break
            elif map[x][y] == 1:
                mapa_ia_visivel[x][y] = 2
                break
            else:
                print("Jogada Invalida, Animal...")
                        
    for i in range(3):
        printa_mapa()
        
        print(f"\nAtaque {i + 1}")
        
        jogadas_disponiveis = get_empty_positions(mapa_jogador_visivel)
        if not acerto_ia:
            numero_sorteado = np.random.randint(0, len(jogadas_disponiveis))
            x, y = jogadas_disponiveis[numero_sorteado]

            if map[x][y] == 0:
                mapa_jogador_visivel[x][y] = -1
            elif map[x][y] == 1:
                mapa_jogador_visivel[x][y] = 2
                acerto_ia = True
                posicao_acerto = (x, y)
        else:
            pass