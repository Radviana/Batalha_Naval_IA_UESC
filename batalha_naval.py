import json
# import time
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
    print("\n\t   IA\t\t\t   Player")
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
    
def interface_colocar_navios(mapa, qtd_navios):
    navios = [submarino, corvetas, fragatas, cruzadores, porta_avioes, hidro_avioes]
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
    qtds_navios = [qtd_submarino_ia, qtd_corveta_ia, qtd_corveta_ia, qtd_fragata_ia, qtd_fragata_ia, qtd_cruzador_ia, 
                   qtd_cruzador_ia, qtd_porta_aviao_ia, qtd_porta_aviao_ia, qtd_hidro_aviao_ia, qtd_hidro_aviao_ia, 
                   qtd_hidro_aviao_ia, qtd_hidro_aviao_ia]
    tipos_navios = submarino + corvetas + fragatas + cruzadores + porta_avioes + hidro_avioes
    id_navios = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6, 6]
   
    for id_navio, tipo_navio, qtd_navio in zip(id_navios, tipos_navios, qtds_navios):
        if qtd_navio > 0:
            for i in range(1, 11):
                for j in range(1, 11):
                    tmp_mapa = adicionar_navio(tipo_navio, (i, j), id_navio, mapa)
                    
                    if not np.array_equal(tmp_mapa, mapa):
                        posicoes_vazias.add((i, j))
                        
    return sorted(list(posicoes_vazias))

def verifica_acertos(mapa_consulta, coords, qtds_acertos, qtds_navios, nome_jogador):
    global lados_jogar, jogadas_ia, jogadas_jogador, navios_afundados
    x, y = coords
    
    if nome_jogador.lower() == "ia" and (x, y) not in jogadas_ia:
        qtds_acertos[mapa_consulta[x][y] - 1] += 1
        jogadas_ia.append((x, y))
    elif nome_jogador.lower() == "jogador" and (x, y) not in jogadas_jogador:
        qtds_acertos[mapa_consulta[x][y] - 1] += 1
        jogadas_jogador.append((x, y))
        
    if qtds_acertos[mapa_consulta[x][y] - 1] == limite_acertos[mapa_consulta[x][y] - 1]: 
        print(f"{nome_jogador} jogou ({x + 1}, {y + 1}) e derrubou um {nomes_navios[mapa_consulta[x][y] - 1]}")
        qtds_navios[mapa_consulta[x][y] - 1] -= 1
        qtds_acertos[mapa_consulta[x][y] - 1] = 0
        navios_afundados +=1
        
        if nome_jogador.lower() == "ia":
            lados_jogar = []
    else:
        print(f"{nome_jogador} jogou ({x + 1}, {y + 1}) e acertou uma parte de uma {nomes_navios[mapa_consulta[x][y] - 1]}")
        
def verifica_lados_jogar(x, y):
    global lados_jogar
    
    if x == 0:
        if y == 0:
            lados_jogar = ['baixo', 'direita']
        elif y == 9:
            lados_jogar = ['baixo', 'esquerda']
        else:
            lados_jogar = ['baixo', 'direita', 'esquerda']
    elif x == 9:
        if y == 0:
            lados_jogar = ['cima', 'direita']
        elif y == 9:
            lados_jogar = ['cima', 'esquerda']
        else:
            lados_jogar = ['cima', 'direita', 'esquerda']
    elif 0 < x < 9:
        if y == 0:
            lados_jogar = ['baixo', 'cima', 'direita']
        elif y == 9:
            lados_jogar = ['baixo', 'cima', 'esquerda']
        else:
            lados_jogar = ['baixo', 'cima', 'direita', 'esquerda']
    
def ataque():
    global acerto_ia
    global deslocamento
    global lados_jogar
    global posicao_acerto
    global navio_acertado
    global qtds_acertos_ia, qtds_acertos_jogador
    global acerto_baixo_dir, acerto_baixo_esq, acerto_cima_dir, acerto_cima_esq
    global x,y
    
    """ printa_mapa()
    print("Vez do jogador, Faça 3 ataques: ")
    for i in range(3):
        while True:
            print(f"Ataque {i + 1}")
            
            x = int(input("Informe a linha: ")) - 1
            y = int(input("Informe a coluna: ")) - 1
            print()
            
            if x > 9 or x < 0 or y > 9 or y < 0:
                printa_mapa()
                print("Jogada invalida..")
            elif mapa_ia_consulta[x][y] == 0 and mapa_ia_visivel[x][y] == 0:
                mapa_ia_visivel[x][y] = -1
                printa_mapa()
                print("\nVocê errou, tiro ao mar...\n")
                break
            elif mapa_ia_consulta[x][y] in [1, 2, 3, 4, 5, 6] and mapa_ia_visivel[x][y] == 0:
                mapa_ia_visivel[x][y] = 7
                printa_mapa()
                verifica_acertos(mapa_ia_consulta, (x, y), qtds_acertos_jogador, qtds_navios_jogador, "Jogador")
                break
            else:
                printa_mapa()
                print("Jogada Invalida, repita a jogada...") """
    
    print("\n-------------VEZ DA IA----------------")  
    i = 0                 
    while i < 5:
        jogadas_disponiveis = pega_posicoes_disponiveis(mapa_jogador_visivel)
        if len(jogadas_disponiveis) == 0:
            print("entrou aqui, numero de jogadas = ", len(jogadas_disponiveis))
            break
        if not acerto_ia:
            numero_sorteado = np.random.randint(0, len(jogadas_disponiveis))
            x, y = jogadas_disponiveis[numero_sorteado]
            #x, y = x-1, y-1
            x, y = 0, 4
            
            if mapa_jogador_consulta[x][y] == 0:
                mapa_jogador_visivel[x][y] = -1
                print(f"IA jogou ({x + 1}, {y + 1}) e errou, tiro ao mar...")
            elif mapa_jogador_consulta[x][y] in [1, 2, 3, 4, 5, 6]:
                mapa_jogador_visivel[x][y] = 7
                verifica_acertos(mapa_jogador_consulta, (x, y), qtds_acertos_ia, qtds_navios_ia, "IA")
                
                if mapa_jogador_consulta[x][y] != 1:
                    acerto_ia = True
                
                # Verifica quais lado a IA pode jogar
                if acerto_ia:
                    verifica_lados_jogar(x, y)
                    
                posicao_acerto = (x, y)
                navio_acertado = mapa_jogador_consulta[x][y]     
            i+=1
        else:
            """ if not acerto_cima_esq and not acerto_baixo_esq and not acerto_cima_dir and not acerto_baixo_dir: """
            x, y = posicao_acerto
            if lados_jogar == []:
                acerto_ia = False
                deslocamento = 0
                print('Acerto ia False 1')
                
            elif navio_acertado in [1, 2, 3, 4, 5]: # Verifica se é um dos návios base
                if lados_jogar[0] == 'esquerda' and y-1-deslocamento >= 0 and mapa_jogador_visivel[x][y-1-deslocamento] == 0:
                    if mapa_jogador_consulta[x][y-1-deslocamento] == navio_acertado:
                        mapa_jogador_visivel[x][y-1-deslocamento] = 7
                        verifica_acertos(mapa_jogador_consulta, (x, y-1-deslocamento), qtds_acertos_ia, qtds_navios_ia, "IA")
                        deslocamento += 1
                    else:
                        print(f"IA jogou ({x+1}, {y-deslocamento}) e errou, tiro ao mar...")
                        mapa_jogador_visivel[x][y-1-deslocamento] = -1
                        deslocamento = 0
                        del lados_jogar[0]
                elif lados_jogar[0] == 'direita' and y+1+deslocamento <= 9 and mapa_jogador_visivel[x][y+1+deslocamento] == 0:
                    if mapa_jogador_consulta[x][y+1+deslocamento] == navio_acertado:
                        mapa_jogador_visivel[x][y+1+deslocamento] = 7
                        verifica_acertos(mapa_jogador_consulta, (x, y+1+deslocamento), qtds_acertos_ia, qtds_navios_ia, "IA")
                        deslocamento += 1
                    else:
                        print(f"IA jogou ({x+1}, {y+2+deslocamento}) e errou, tiro ao mar...")
                        mapa_jogador_visivel[x][y+1+deslocamento] = -1
                        deslocamento = 0
                        del lados_jogar[0]
                elif lados_jogar[0] == 'cima' and x-1-deslocamento >= 0 and mapa_jogador_visivel[x-1-deslocamento][y] == 0:
                    if mapa_jogador_consulta[x-1-deslocamento][y] == navio_acertado:
                        mapa_jogador_visivel[x-1-deslocamento][y] = 7
                        verifica_acertos(mapa_jogador_consulta, (x-1-deslocamento, y), qtds_acertos_ia, qtds_navios_ia, "IA")
                        deslocamento += 1
                    else:
                        print(f"IA jogou ({x-deslocamento}, {y+1}) e errou, tiro ao mar...")
                        mapa_jogador_visivel[x-1-deslocamento][y] = -1
                        deslocamento = 0
                        del lados_jogar[0]
                elif lados_jogar[0] == 'baixo' and x+1+deslocamento <= 9 and mapa_jogador_visivel[x+1+deslocamento][y] == 0:
                    if mapa_jogador_consulta[x+1+deslocamento][y] == navio_acertado:
                        mapa_jogador_visivel[x+1+deslocamento][y] = 7
                        verifica_acertos(mapa_jogador_consulta, (x+1+deslocamento, y), qtds_acertos_ia, qtds_navios_ia, "IA")
                        deslocamento += 1
                    else:
                        print(f"IA jogou ({x+2+deslocamento}, {y+1}) e errou, tiro ao mar...")
                        mapa_jogador_visivel[x+1+deslocamento][y] = -1
                        deslocamento = 0
                        del lados_jogar[0] 
                else:
                    deslocamento = 0
                    lados_jogar = []
                i+=1
                 
            else: # Verifica Hidro Aviões  
                if 'baixo' in lados_jogar and 'cima' not in lados_jogar: # Baixo e não cima
                    print("baixo e não cima")
                    if 'direita' in lados_jogar and y+1 <= 9:
                        if mapa_jogador_consulta[x+1][y+1] == navio_acertado and mapa_jogador_visivel[x+1][y+1] == 0:
                            mapa_jogador_visivel[x+1][y+1] = 7
                            verifica_acertos(mapa_jogador_consulta, (x+1, y+1), qtds_acertos_ia, qtds_navios_ia, "IA")
                            if "direita" in lados_jogar: 
                                lados_jogar.remove("direita")
                        elif mapa_jogador_consulta[x+1][y+1] != navio_acertado and mapa_jogador_visivel[x+1][y+1] == 0:
                            mapa_jogador_visivel[x+1][y+1] = -1
                            print(f"IA jogou ({x+1}, {y+1}) e errou, tiro ao mar...")
                            if "direita" in lados_jogar: 
                                lados_jogar.remove("direita")         
                    elif 'esquerda' in lados_jogar and y-1 >= 0:
                        if mapa_jogador_consulta[x+1][y-1] == navio_acertado and mapa_jogador_visivel[x+1][y-1] == 0:
                            mapa_jogador_visivel[x+1][y-1] = 7
                            verifica_acertos(mapa_jogador_consulta, (x+1, y-1), qtds_acertos_ia, qtds_navios_ia, "IA")
                            if "esquerda" in lados_jogar: 
                                lados_jogar.remove("esquerda")
                        elif mapa_jogador_consulta[x+1][y-1] != navio_acertado and mapa_jogador_visivel[x+1][y-1] == 0:
                            mapa_jogador_visivel[x+1][y-1] = -1
                            print(f"IA jogou ({x+1}, {y-1}) e errou, tiro ao mar...")
                            if "esquerda" in lados_jogar: 
                                lados_jogar.remove("esquerda")
                    elif qtds_acertos_ia[5] == 2 and x+2 <= 9:
                        if mapa_jogador_consulta[x+2][y] == navio_acertado and mapa_jogador_visivel[x+2][y] == 0:
                            mapa_jogador_visivel[x+2][y] = 7
                            verifica_acertos(mapa_jogador_consulta, (x+2, y), qtds_acertos_ia, qtds_navios_ia, "IA")
                            if "baixo" in lados_jogar: 
                                lados_jogar.remove("baixo")
                        elif mapa_jogador_consulta[x+2][y] != navio_acertado and mapa_jogador_visivel[x+2][y] == 0:
                            mapa_jogador_visivel[x+2][y] = -1
                            print(f"IA jogou ({x+2}, {y}) e errou, tiro ao mar...")
                            if "baixo" in lados_jogar: 
                                lados_jogar.remove("baixo") 
                    else:
                        lados_jogar = []
                         
                elif 'cima' in lados_jogar and 'baixo' not in lados_jogar: # Cima e não baixo
                    print("cima e não baixo")
                    if 'direita' in lados_jogar and y+1 <= 9:
                        if mapa_jogador_consulta[x-1][y+1] == navio_acertado and mapa_jogador_visivel[x-1][y+1] == 0:
                            mapa_jogador_visivel[x-1][y+1] = 7
                            verifica_acertos(mapa_jogador_consulta, (x-1, y+1), qtds_acertos_ia, qtds_navios_ia, "IA")
                            if "direita" in lados_jogar: 
                                lados_jogar.remove("direita")
                        elif mapa_jogador_consulta[x-1][y+1] != navio_acertado and mapa_jogador_visivel[x-1][y+1] == 0:
                            mapa_jogador_visivel[x-1][y+1] = -1
                            print(f"IA jogou ({x-1}, {y+1}) e errou, tiro ao mar...")
                            if "direita" in lados_jogar: 
                                lados_jogar.remove("direita")
                    elif 'esquerda' in lados_jogar and y-1 >= 0:
                        if mapa_jogador_consulta[x-1][y-1] == navio_acertado and mapa_jogador_visivel[x-1][y-1] == 0:
                            mapa_jogador_visivel[x-1][y-1] = 7
                            verifica_acertos(mapa_jogador_consulta, (x-1, y-1), qtds_acertos_ia, qtds_navios_ia, "IA")
                            if "esquerda" in lados_jogar: 
                                lados_jogar.remove("esquerda")
                        elif mapa_jogador_consulta[x-1][y-1] != navio_acertado and mapa_jogador_visivel[x-1][y-1] == 0:
                            mapa_jogador_visivel[x-1][y-1] = -1
                            print(f"IA jogou ({x-1}, {y-1}) e errou, tiro ao mar...")
                            if "esquerda" in lados_jogar: 
                                lados_jogar.remove("esquerda")  
                    elif qtds_acertos_ia[5] == 2 and x-2 >= 0:
                        if mapa_jogador_consulta[x-2][y] == navio_acertado and mapa_jogador_visivel[x-2][y] == 0:
                            mapa_jogador_visivel[x-2][y] = 7
                            verifica_acertos(mapa_jogador_consulta, (x-2, y), qtds_acertos_ia, qtds_navios_ia, "IA")
                            if "cima" in lados_jogar: 
                                lados_jogar.remove("cima") 
                        elif mapa_jogador_consulta[x-2][y] != navio_acertado and mapa_jogador_visivel[x-2][y] == 0:
                            mapa_jogador_visivel[x-2][y] = -1
                            print(f"IA jogou ({x-2}, {y}) e errou, tiro ao mar...")
                            if "cima" in lados_jogar: 
                                lados_jogar.remove("cima")
                    else:
                        lados_jogar = []
                        
                elif 'cima' in lados_jogar and 'baixo' in lados_jogar:
                    if 'esquerda' in lados_jogar and 'direita' not in lados_jogar and y-1>= 0:
                        if mapa_jogador_consulta[x-1][y-1] == navio_acertado and mapa_jogador_visivel[x-1][y-1] == 0:
                            mapa_jogador_visivel[x-1][y-1] = 7
                            verifica_acertos(mapa_jogador_consulta, (x-1, y-1), qtds_acertos_ia, qtds_navios_ia, "IA")
                        elif mapa_jogador_consulta[x-1][y-1] != navio_acertado and mapa_jogador_visivel[x-1][y-1] == 0:
                            mapa_jogador_visivel[x-1][y-1] = -1
                            print(f"IA jogou ({x}, {y}) e errou, tiro ao mar...")
                        elif mapa_jogador_consulta[x+1][y-1] == navio_acertado and mapa_jogador_visivel[x+1][y-1] == 0:
                            mapa_jogador_visivel[x+1][y-1] = 7
                            verifica_acertos(mapa_jogador_consulta, (x+1, y-1), qtds_acertos_ia, qtds_navios_ia, "IA")
                        elif mapa_jogador_consulta[x+1][y-1] != navio_acertado and mapa_jogador_visivel[x+1][y-1] == 0:
                            mapa_jogador_visivel[x+1][y-1] = -1
                            print(f"IA jogou ({x+2}, {y}) e errou, tiro ao mar...")
                        elif qtds_acertos_ia[5] == 2:
                            if x-2>=0 and mapa_jogador_visivel[x-1][y-1] == 7 and mapa_jogador_consulta[x-2][y] == navio_acertado\
                            and mapa_jogador_visivel[x-2][y] == 0:
                                mapa_jogador_visivel[x-2][y] = 7
                                verifica_acertos(mapa_jogador_consulta, (x-2, y), qtds_acertos_ia, qtds_navios_ia, "IA") 
                            elif x-2>=0 and mapa_jogador_visivel[x-1][y-1] == 7 and mapa_jogador_consulta[x-2][y] != navio_acertado \
                            and mapa_jogador_visivel[x-2][y] == 0:
                                mapa_jogador_visivel[x-2][y] = -1
                                print(f"IA jogou ({x-1}, {y+1}) e errou, tiro ao mar...")
                            elif y-2>=0 and mapa_jogador_consulta[x][y-2] == navio_acertado and mapa_jogador_visivel[x][y-2] == 0:
                                mapa_jogador_visivel[x][y-2] = 7
                                verifica_acertos(mapa_jogador_consulta, (x, y-2), qtds_acertos_ia, qtds_navios_ia, "IA") 
                            elif y-2>=0 and mapa_jogador_consulta[x][y-2] != navio_acertado and mapa_jogador_visivel[x][y-2] == 0:
                                mapa_jogador_visivel[x][y-2] = -1
                                print(f"IA jogou ({x+1}, {y-1}) e errou, tiro ao mar...")
                            elif x+2 <=9 and mapa_jogador_consulta[x+2][y] == navio_acertado and mapa_jogador_visivel[x+2][y] == 0:
                                mapa_jogador_visivel[x+2][y] = 7
                                verifica_acertos(mapa_jogador_consulta, (x+2, y), qtds_acertos_ia, qtds_navios_ia, "IA") 
                            elif x+2 <=9 and mapa_jogador_consulta[x+2][y] != navio_acertado and mapa_jogador_visivel[x+2][y] == 0:
                                mapa_jogador_visivel[x+2][y] = -1
                                print(f"IA jogou ({x+3}, {y+1}) e errou, tiro ao mar...")
                        else:
                            lados_jogar = [] 
                        
                    elif 'direita' in lados_jogar and 'esquerda' not in lados_jogar and y+1 >= 0:
                        if mapa_jogador_consulta[x-1][y+1] == navio_acertado and mapa_jogador_visivel[x-1][y+1] == 0:
                            mapa_jogador_visivel[x-1][y+1] = 7
                            verifica_acertos(mapa_jogador_consulta, (x-1, y+1), qtds_acertos_ia, qtds_navios_ia, "IA")
                        elif mapa_jogador_consulta[x-1][y+1] != navio_acertado and mapa_jogador_visivel[x-1][y+1] == 0:
                            mapa_jogador_visivel[x-1][y+1] = -1
                            print(f"IA jogou ({x}, {y+2}) e errou, tiro ao mar...")
                        elif mapa_jogador_consulta[x+1][y+1] == navio_acertado and mapa_jogador_visivel[x+1][y+1] == 0:
                            mapa_jogador_visivel[x+1][y+1] = 7
                            verifica_acertos(mapa_jogador_consulta, (x+1, y+1), qtds_acertos_ia, qtds_navios_ia, "IA")
                        elif mapa_jogador_consulta[x+1][y+1] != navio_acertado and mapa_jogador_visivel[x+1][y+1] == 0:
                            mapa_jogador_visivel[x+1][y+1] = -1
                            print(f"IA jogou ({x+2}, {y+2}) e errou, tiro ao mar...")
                        elif qtds_acertos_ia[5] == 2:
                            if x-2>=0 and mapa_jogador_visivel[x-1][y+1] == 7 and mapa_jogador_consulta[x-2][y] == navio_acertado\
                            and mapa_jogador_visivel[x-2][y] == 0:
                                mapa_jogador_visivel[x-2][y] = 7
                                verifica_acertos(mapa_jogador_consulta, (x-2, y), qtds_acertos_ia, qtds_navios_ia, "IA") 
                            elif x-2>=0 and mapa_jogador_visivel[x-1][y+1] == 7 and mapa_jogador_consulta[x-2][y] != navio_acertado \
                            and mapa_jogador_visivel[x-2][y] == 0:
                                mapa_jogador_visivel[x-2][y] = -1
                                print(f"IA jogou ({x-1}, {y+1}) e errou, tiro ao mar...")
                            elif y+2>=0 and mapa_jogador_consulta[x][y+2] == navio_acertado and mapa_jogador_visivel[x][y+2] == 0:
                                mapa_jogador_visivel[x][y+2] = 7
                                verifica_acertos(mapa_jogador_consulta, (x, y+2), qtds_acertos_ia, qtds_navios_ia, "IA") 
                            elif y+2>=0 and mapa_jogador_consulta[x][y+2] != navio_acertado and mapa_jogador_visivel[x][y+2] == 0:
                                mapa_jogador_visivel[x][y+2] = -1
                                print(f"IA jogou ({x+1}, {y+3}) e errou, tiro ao mar...") 
                            elif x+2 <=9 and mapa_jogador_consulta[x+2][y] == navio_acertado and mapa_jogador_visivel[x+2][y] == 0:
                                mapa_jogador_visivel[x+2][y] = 7
                                verifica_acertos(mapa_jogador_consulta, (x+2, y), qtds_acertos_ia, qtds_navios_ia, "IA") 
                            elif x+2 <=9 and mapa_jogador_consulta[x+2][y] != navio_acertado and mapa_jogador_visivel[x+2][y] == 0:
                                mapa_jogador_visivel[x+2][y] = -1
                                print(f"IA jogou ({x+3}, {y+1}) e errou, tiro ao mar...")
                        else:
                            lados_jogar = []

                    elif 'direita' in lados_jogar and 'esquerda' in lados_jogar:
                        print(x, y)
                        # Cima Esquerda
                        if x-1 >= 0 and y-1 >= 0 and mapa_jogador_consulta[x-1][y-1] == navio_acertado\
                        and mapa_jogador_visivel[x-1][y-1] == 0:
                            mapa_jogador_visivel[x-1][y-1] = 7 
                            verifica_acertos(mapa_jogador_consulta, (x-1, y-1), qtds_acertos_ia, qtds_navios_ia, "IA")
                            acerto_cima_esq = True
                            x, y = x-1, y-1
                        elif x-1 >= 0 and y-1 >= 0 and  mapa_jogador_consulta[x-1][y-1] != navio_acertado\
                        and mapa_jogador_visivel[x-1][y-1] == 0:
                            mapa_jogador_visivel[x-1][y-1] = -1
                            print(f"IA jogou ({x}, {y}) e errou, tiro ao mar...")
                         
                        # Baixo Esquerda   
                        elif x+1 <= 9 and y-1 >= 0 and mapa_jogador_consulta[x+1][y-1] == navio_acertado\
                        and mapa_jogador_visivel[x+1][y-1] == 0:
                            mapa_jogador_visivel[x+1][y-1] = 7
                            verifica_acertos(mapa_jogador_consulta, (x+1, y-1), qtds_acertos_ia, qtds_navios_ia, "IA")
                            acerto_baixo_esq = True
                            x, y = x+1, y-1
                        elif x+1 <= 9 and y-1 >= 0 and mapa_jogador_consulta[x+1][y-1] != navio_acertado\
                        and mapa_jogador_visivel[x+1][y-1] == 0:
                            mapa_jogador_visivel[x+1][y-1] = -1
                            print(f"IA jogou ({x+2}, {y}) e errou, tiro ao mar...")
                        
                        # Cima direita    
                        elif x-1 >= 0 and y+1 <= 9 and mapa_jogador_consulta[x-1][y+1] == navio_acertado\
                        and mapa_jogador_visivel[x-1][y+1] == 0:
                            mapa_jogador_visivel[x-1][y+1] = 7
                            verifica_acertos(mapa_jogador_consulta, (x-1, y+1), qtds_acertos_ia, qtds_navios_ia, "IA")
                            acerto_cima_dir = True
                            x, y = x-1, y+1
                        elif x-1 >= 0 and y+1 <= 9 and mapa_jogador_consulta[x-1][y+1] != navio_acertado\
                        and mapa_jogador_visivel[x-1][y+1] == 0:
                            mapa_jogador_visivel[x-1][y+1] = -1
                            print(f"IA jogou ({x}, {y+2}) e errou, tiro ao mar...")    
                           
                        # Baixo Direita
                        elif x+1 <= 9 and y+1 <= 9 and mapa_jogador_consulta[x+1][y+1] == navio_acertado\
                        and mapa_jogador_visivel[x+1][y+1] == 0:
                            mapa_jogador_visivel[x+1][y+1] = 7
                            verifica_acertos(mapa_jogador_consulta, (x+1, y+1), qtds_acertos_ia, qtds_navios_ia, "IA")
                            acerto_cima_dir = True
                            x, y = x+1, y+1
                        elif x+1 <= 9 and y+1 <= 9 and mapa_jogador_consulta[x+1][y+1] != navio_acertado\
                        and mapa_jogador_visivel[x+1][y+1] == 0:
                            mapa_jogador_visivel[x+1][y+1] = -1
                            print(f"IA jogou ({x+2}, {y+2}) e errou, tiro ao mar...")      
                        """ else:
                            print(x, y)
                            print("esse else")
                            lados_jogar = []
                            acerto_baixo_dir = acerto_baixo_esq = acerto_cima_dir = acerto_cima_esq = False """
                    else:
                        print("esse outro else")
                        lados_jogar = []
                        acerto_baixo_dir = acerto_baixo_esq = acerto_cima_dir = acerto_cima_esq = False  
                else:
                    print("entrou aqui no else")
                    deslocamento = 0
                    lados_jogar = []
                i+=1    
    #printa_mapa()

def menu():
    opt = 0
    print("\t______         _           _  _               _   _                       _ ")
    print("\t| ___ \       | |         | || |             | \ | |                     | |")
    print("\t| |_/ /  __ _ | |_   __ _ | || |__    __ _   |  \| |  __ _ __   __  __ _ | |")
    print("\t| ___ \ / _` || __| / _` || || '_ \  / _` |  | . ` | / _` |\ \ / / / _` || |")
    print("\t| |_/ /| (_| || |_ | (_| || || | | || (_| |  | |\  || (_| | \ V / | (_| || |")
    print("\t\____/  \__,_| \__| \__,_||_||_| |_| \__,_|  \_| \_/ \__,_|  \_/   \__,_||_|")
    opt = int(input("\n\nAperte 1 para começar ou 2 para o computador começar: "))
    while (opt!=1 or opt!=2):
        if(opt==1):
            #ataque do pc
            break
        elif(opt==2):
            #ataque da ia
            break
        else:
            print("Opção inválida.")
            print("Aperte 1 para começar ou 2 para o computador começar: ")

if __name__ == "__main__":

    with open("mapas.json", 'r') as file:
        dict_json = json.load(file)
        mapa_pc = dict_json['mapa_aux0']
        mapa_ia = dict_json['mapa_ia']
    
        mapa_ia_consulta = deepcopy(mapa_ia)
        mapa_jogador_consulta = deepcopy(mapa_pc)
        #mapa_ia_visivel = deepcopy(mapa_ia)
        #mapa_jogador_visivel = deepcopy(mapa_pc)
    #printa_mapa()
    i = 0
    while i < 1:
        ataque()
        i+=1
    printa_mapa()
    print(navios_afundados)
    """ mapa_jogador_visivel = adicionar_navio(hidro_avioes[1], (3, 3), 6, mapa_jogador_visivel)
    mapa_jogador_visivel = adicionar_navio(submarino[0], (5, 2), 1, mapa_jogador_visivel)
    mapa_jogador_visivel = adicionar_navio(submarino[0], (5, 6), 1, mapa_jogador_visivel)
    mapa_jogador_visivel = adicionar_navio(submarino[0], (2, 3), 1, mapa_jogador_visivel) """
       