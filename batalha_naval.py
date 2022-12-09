import json
import random
from config import *
from copy import deepcopy

def substitui_print(element):
    if element == '0':
        element = agua
    elif element == '7':
        element = acerto
    elif element not in ['1', '2', '3', '4', '5', '6']:
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
    id_navios = [1, 2, 3, 4, 5, 6]
    
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
            mapa = adicionar_navio(navios[orientacao_navio], (x_navio, y_navio), id_navios[i], mapa)
            
            # Incrementa a quantidade de determinado návio no mapa
            if mapa != tmp_map:
                qtd_navios[i] += 1
            
            op = input("Digite 0 para Sair e qualquer outra tecla para continuar: ")
            print()
            
            if op == '0':
                break
      
    return mapa
     
def pega_posicoes_disponiveis(mapa):
    posicoes_vazias = set()
    qtds_navios = [qtd_submarino, qtd_corveta, qtd_corveta, qtd_fragata, qtd_fragata, qtd_cruzador, qtd_cruzador, 
                   qtd_porta_aviao, qtd_porta_aviao, qtd_hidro_aviao, qtd_hidro_aviao, qtd_hidro_aviao, qtd_hidro_aviao]
    tipos_navios = submarino + corvetas + fragatas + cruzadores + porta_avioes + hidro_avioes
    id_navios = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6, 6]
    
    for id_navio, tipo_navio, qtd_navio in zip(id_navios, tipos_navios, qtds_navios):
        if qtd_navio > 0:
            for i in range(1, 11):
                for j in range(1, 11):
                    tmp_mapa = adicionar_navio(tipo_navio, (i, j), id_navio, mapa)
                    
                    if ~np.array_equal(tmp_mapa, mapa):
                        posicoes_vazias.add((i, j))
                        
    return list(posicoes_vazias)
    
def ataque():
    global acerto_ia
    global deslocamento
    global lados_jogar
    global posicao_acerto
    global navio_acertado
    
    """  print("Vez do jogador, Faça 3 ataques: \n")
    printa_mapa()
    for i in range(3):
        while True:
            print(f"Ataque {i + 1}")
            
            x = int(input("Informe a linha: ")) - 1
            y = int(input("Informe a coluna: ")) - 1
            print()
            
            if x > 9 or x < 0 or y > 9 or y < 0:
                print("Jogada invalida..")
                continue
            
            if mapa_ia_consulta[x][y] == 0:
                mapa_ia_visivel[x][y] = -1
                break
            elif mapa_ia_consulta[x][y] in [1, 2, 3, 4, 5, 6]:
                print(f"Você acertou uma parte de uma {nomes_navios[mapa_ia_consulta[x][y] - 1]}\n")
                mapa_ia_visivel[x][y] = 7
                break
            else:
                print("Jogada Invalida, Animal...")
        printa_mapa() """
    
    print("\nVez da IA\n")  
    i = 0                 
    while i < 3:
        jogadas_disponiveis = pega_posicoes_disponiveis(mapa_jogador_visivel)
        if not acerto_ia:
            numero_sorteado = random.randint(0, len(jogadas_disponiveis) - 1)
            x, y = jogadas_disponiveis[numero_sorteado]
            x, y = x-1, y-1

            if mapa_jogador_consulta[x][y] == 0:
                mapa_jogador_visivel[x][y] = -1
            elif mapa_jogador_consulta[x][y] in [1, 2, 3, 4, 5, 6]:
                mapa_jogador_visivel[x][y] = 7
                print(f"IA acertou uma parte de uma {nomes_navios[mapa_ia_consulta[x][y] - 1]}")
                
                if mapa_jogador_consulta[x][y] != 1:
                    acerto_ia = True
                
                # Verifica quais lado a IA pode jogar
                if x == 0 and acerto_ia:
                    if y == 0:
                        lados_jogar = ['baixo', 'direita']
                    elif y == 9:
                        lados_jogar = ['baixo', 'esquerda']
                    else:
                        lados_jogar = ['baixo', 'direita', 'esquerda']
                elif x == 9 and acerto_ia:
                    if y == 0:
                        lados_jogar = ['cima', 'direita']
                    elif y == 9:
                        lados_jogar = ['cima', 'esquerda']
                    else:
                        lados_jogar = ['cima', 'direita', 'esquerda']
                elif acerto_ia:
                    lados_jogar = ['baixo', 'cima', 'direita', 'esquerda']
                    
                posicao_acerto = (x, y)
                navio_acertado = mapa_jogador_consulta[x][y]  
                 
            i+=1
        else:
            x, y = posicao_acerto
            if lados_jogar == []:
                acerto_ia = False
            elif navio_acertado in [1, 2, 3, 4, 5, 6]: # Verifica se é um dos návios base
                if lados_jogar[0] == 'esquerda' and y-1-deslocamento >= 0 and mapa_jogador_visivel[x][y-1-deslocamento] == 0:
                    print("tentou esquerda")
                    
                    if mapa_jogador_consulta[x][y-1-deslocamento] == navio_acertado:
                        mapa_jogador_visivel[x][y-1-deslocamento] = 7
                        deslocamento += 1
                    else:
                        mapa_jogador_visivel[x][y-1-deslocamento] = 8
                        deslocamento = 0
                        del lados_jogar[0]
                    
                elif lados_jogar[0] == 'direita' and y+1+deslocamento <= 9 and mapa_jogador_visivel[x][y+1+deslocamento] == 0:
                    print("tentou direita")
                    
                    if mapa_jogador_consulta[x][y+1+deslocamento] == navio_acertado:
                        mapa_jogador_visivel[x][y+1+deslocamento] = 7
                        deslocamento += 1
                    else:
                        mapa_jogador_visivel[x][y+1+deslocamento] = 8
                        deslocamento = 0
                        del lados_jogar[0]
    
                elif lados_jogar[0] == 'cima' and x-1-deslocamento >= 0 and mapa_jogador_visivel[x-1-deslocamento][y] == 0:
                    print("tentou cima")
                    
                    if mapa_jogador_consulta[x-1-deslocamento][y] == navio_acertado:
                        mapa_jogador_visivel[x-1-deslocamento][y] = 7
                        deslocamento += 1
                    else:
                        mapa_jogador_visivel[x-1-deslocamento][y] = 8
                        deslocamento = 0
                        del lados_jogar[0]
                    
                elif lados_jogar[0] == 'baixo' and x+1+deslocamento <= 9 and mapa_jogador_visivel[x+1+deslocamento][y] == 0:
                    print("tentou baixo")
                    
                    if mapa_jogador_consulta[x+1+deslocamento][y] == navio_acertado:
                        mapa_jogador_visivel[x+1+deslocamento][y] = 7
                        deslocamento += 1
                    else:
                        mapa_jogador_visivel[x+1+deslocamento][y] = 8
                        deslocamento = 0
                        del lados_jogar[0]
                        
                i+=1
            else:
                print("aqui")
                i+=1  
    printa_mapa()

if __name__ == "__main__":
    mapa_ia = None
    mapa_pc = None

    with open("mapas.json", 'r') as file:
        dict_json = json.load(file)
        mapa_pc = dict_json['mapa_pc']
        mapa_ia = dict_json['mapa_ia']
        #mapa_ia_visivel = dict_json['mapa_ia']
        #mapa_pc_visivel = dict_json['mapa_pc'] """
        
    #pos = pega_posicoes_disponiveis(mapa_ia)
    #print(len(pos))
    #print(sorted(pos))

    mapa_ia_consulta = deepcopy(mapa_ia)
    mapa_jogador_consulta = deepcopy(mapa_pc)
    #mapa_ia_visivel = deepcopy(mapa_ia)
    #mapa_jogador_visivel = deepcopy(mapa_pc)
         
    #printa_mapa()
    i = 0
    while i < 3:
        ataque()
        i+=1