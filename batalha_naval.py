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
    
def interface_colocar_navios():
    navios = [submarino, corvetas, fragatas, cruzadores, porta_avioes, hidro_avioes]
    id_navios = [1, 2, 3, 4, 5, 6]
    global qtds_navios_jogador, mapa_jogador_consulta
  
    for i in range(len(navios)):
        op = -1
        while True:
            print(f"Colocando {nomes_navios[i]}...")
            x_navio = int(input(f"Digite a posicão X do {nomes_navios[i]}: "))
            y_navio = int(input(f"Digite a posicão Y do {nomes_navios[i]}: "))
            orientacao_navio = int(input(f"Digite a orientação do {nomes_navios[i]}: "))
            
            tmp_mapa = deepcopy(mapa_jogador_consulta)
            tmp_mapa = adicionar_navio(navios[i][orientacao_navio], (x_navio, y_navio), id_navios[i], mapa_jogador_consulta)
            
            # Incrementa a quantidade de determinado návio no mapa
            if not np.array_equal(tmp_mapa, mapa_jogador_consulta):
                qtds_navios_jogador[i] += 1
                print(f"\nFoi adicionado um {nomes_navios[i]} na posição ({x_navio}, {y_navio}).")
                mapa_jogador_consulta = tmp_mapa
            else:
                print(f"\nErro ao adicionar o {nomes_navios[i]} na posição ({x_navio}, {y_navio}).")
            
            op = input("Digite 0 para Sair e qualquer outra tecla para continuar: ")
            print()
            
            if op == '0':
                break  
     
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
    return list(posicoes_vazias)

def verifica_acertos(mapa_consulta, coords, qtds_acertos, qtds_navios, nome_jogador):
    global lados_jogar, jogadas_ia, jogadas_jogador, navios_afundados_ia
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
        
        if nome_jogador.lower() == "ia":
            lados_jogar = []
            navios_afundados_ia +=1
        elif nome_jogador.lower() == 'jogador':
            navios_afundados_jogador +=1
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
    global acerto_baixo_dir, acerto_baixo_esq, acerto_cima_dir, acerto_cima_esq, acerto_hidro_aviao
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
    while i < 3:
        jogadas_disponiveis = pega_posicoes_disponiveis(mapa_jogador_visivel)
        if len(jogadas_disponiveis) == 0:
            print("Não há mais jogadas disponíveis...\n")
            break
        if not acerto_ia:
            numero_sorteado = np.random.randint(0, len(jogadas_disponiveis))
            x, y = jogadas_disponiveis[numero_sorteado]
            x, y = x-1, y-1

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
            x, y = posicao_acerto
            if lados_jogar == []:
                acerto_ia = False
                deslocamento = 0
                
            elif navio_acertado in [1, 2, 3, 4, 5]: # Verifica se é um dos návios base
                print(lados_jogar)
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
                    del lados_jogar[0]
                i+=1
                
             # Verifica Hidro Aviões      
            else: 
                if 'direita' in lados_jogar:
                    # Direita inferior
                    if x+1 <= 9 and mapa_jogador_consulta[x+1][y+1] == navio_acertado and mapa_jogador_visivel[x+1][y+1] == 0 \
                    and not acerto_cima_esq:
                        mapa_jogador_visivel[x+1][y+1] = 7
                        verifica_acertos(mapa_jogador_consulta, (x+1, y+1), qtds_acertos_ia, qtds_navios_ia, "IA")
                        if not acerto_hidro_aviao:
                            acerto_baixo_dir = True
                            acerto_hidro_aviao = True
                    elif x+1 <= 9 and mapa_jogador_consulta[x+1][y+1] != navio_acertado and mapa_jogador_visivel[x+1][y+1] == 0 \
                    and not acerto_cima_esq:
                        mapa_jogador_visivel[x+1][y+1] = -1
                        print(f"IA jogou ({x+2}, {y+2}) e errou, tiro ao mar...")  
                            
                    # Direita Superior
                    elif x-1 >= 0 and mapa_jogador_consulta[x-1][y+1] == navio_acertado and mapa_jogador_visivel[x-1][y+1] == 0 \
                    and not acerto_baixo_esq:
                        mapa_jogador_visivel[x-1][y+1] = 7
                        verifica_acertos(mapa_jogador_consulta, (x-1, y+1), qtds_acertos_ia, qtds_navios_ia, "IA")
                        if not acerto_hidro_aviao:
                            acerto_cima_dir = True
                            acerto_hidro_aviao = True
                    elif x-1 >= 0 and mapa_jogador_consulta[x-1][y+1] != navio_acertado and mapa_jogador_visivel[x-1][y+1] == 0 \
                    and not acerto_baixo_esq:
                        mapa_jogador_visivel[x-1][y+1] = -1
                        print(f"IA jogou ({x}, {y+2}) e errou, tiro ao mar...")
                    else:
                        lados_jogar.remove("direita") 
                        
                    i+=1              
                elif 'esquerda' in lados_jogar:
                    # Esquerda inferior
                    if x+1 <= 9 and mapa_jogador_consulta[x+1][y-1] == navio_acertado and mapa_jogador_visivel[x+1][y-1] == 0 \
                    and not acerto_cima_dir:
                        mapa_jogador_visivel[x+1][y-1] = 7
                        verifica_acertos(mapa_jogador_consulta, (x+1, y-1), qtds_acertos_ia, qtds_navios_ia, "IA")
                        if not acerto_hidro_aviao:
                            acerto_baixo_esq = True
                            acerto_hidro_aviao = True
                    elif x+1 <= 9 and mapa_jogador_consulta[x+1][y-1] != navio_acertado and mapa_jogador_visivel[x+1][y-1] == 0 \
                    and not acerto_cima_dir:
                        mapa_jogador_visivel[x+1][y-1] = -1
                        print(f"IA jogou ({x+2}, {y}) e errou, tiro ao mar...")
                        
                    # Esquerda Superior
                    elif x-1 >= 0 and mapa_jogador_consulta[x-1][y-1] == navio_acertado and mapa_jogador_visivel[x-1][y-1] == 0 \
                    and not acerto_baixo_dir:
                        mapa_jogador_visivel[x-1][y-1] = 7
                        verifica_acertos(mapa_jogador_consulta, (x, y-1), qtds_acertos_ia, qtds_navios_ia, "IA")
                        if not acerto_hidro_aviao:
                            acerto_cima_esq = True
                            acerto_hidro_aviao = True
                    elif x-1 >= 0 and mapa_jogador_consulta[x-1][y-1] != navio_acertado and mapa_jogador_visivel[x-1][y-1] == 0 \
                    and not acerto_baixo_dir:
                        mapa_jogador_visivel[x-1][y-1] = -1
                        print(f"IA jogou ({x}, {y}) e errou, tiro ao mar...")    
                    else:
                        lados_jogar.remove("esquerda")
                        
                    i+=1
                # Outros lados        
                elif qtds_acertos_ia[5] == 2:
                    # Baixo
                    if x+2 <= 9 and mapa_jogador_consulta[x+2][y] == navio_acertado and mapa_jogador_visivel[x+2][y] == 0 \
                    and not acerto_cima_dir and not acerto_cima_esq:
                        mapa_jogador_visivel[x+2][y] = 7
                        verifica_acertos(mapa_jogador_consulta, (x+2, y), qtds_acertos_ia, qtds_navios_ia, "IA")
                    elif x+2 <= 9 and mapa_jogador_consulta[x+2][y] != navio_acertado and mapa_jogador_visivel[x+2][y] == 0 \
                    and not acerto_cima_dir and not acerto_cima_esq:
                        mapa_jogador_visivel[x+2][y] = -1
                        print(f"IA jogou ({x+3}, {y+1}) e errou, tiro ao mar...")
                        
                    # Cima
                    elif x-2 >= 0 and mapa_jogador_consulta[x-2][y] == navio_acertado and mapa_jogador_visivel[x-2][y] == 0 \
                    and not acerto_baixo_dir and not acerto_baixo_esq:
                        mapa_jogador_visivel[x-2][y] = 7
                        verifica_acertos(mapa_jogador_consulta, (x-2, y), qtds_acertos_ia, qtds_navios_ia, "IA")
                    elif x-2 >= 0 and mapa_jogador_consulta[x-2][y] != navio_acertado and mapa_jogador_visivel[x-2][y] == 0 \
                    and not acerto_baixo_dir and not acerto_baixo_esq:
                        mapa_jogador_visivel[x-2][y] = -1
                        print(f"IA jogou ({x-1}, {y+1}) e errou, tiro ao mar...")
                        
                    # Direita
                    elif y+2 <= 9 and mapa_jogador_consulta[x][y+2] == navio_acertado and mapa_jogador_visivel[x][y+2] == 0 \
                    and not acerto_baixo_esq and not acerto_cima_esq:
                        mapa_jogador_visivel[x][y+2] = 7
                        verifica_acertos(mapa_jogador_consulta, (x, y+2), qtds_acertos_ia, qtds_navios_ia, "IA")
                    elif y+2 <= 9 and mapa_jogador_consulta[x][y+2] != navio_acertado and mapa_jogador_visivel[x][y+2] == 0 \
                    and not acerto_baixo_esq and not acerto_cima_esq:
                        mapa_jogador_visivel[x][y+2] = -1
                        print(f"IA jogou ({x+1}, {y+3}) e errou, tiro ao mar...")
                        
                    # esquerda
                    elif y-2 >= 0 and mapa_jogador_consulta[x][y-2] == navio_acertado and mapa_jogador_visivel[x][y-2] == 0 \
                    and not acerto_baixo_dir and not acerto_cima_dir:
                        mapa_jogador_visivel[x][y-2] = 7
                        verifica_acertos(mapa_jogador_consulta, (x, y-2), qtds_acertos_ia, qtds_navios_ia, "IA")
                    elif y-2 >= 0 and mapa_jogador_consulta[x][y-2] != navio_acertado and mapa_jogador_visivel[x][y-2] == 0 \
                    and not acerto_baixo_dir and not acerto_cima_dir:
                        mapa_jogador_visivel[x][y-2] = -1
                        print(f"IA jogou ({x+1}, {y+1}) e errou, tiro ao mar...")
                        
                    else:
                        qtds_acertos_ia[5] = 0  
                    i+=1   
                else:
                    lados_jogar = []
                    acerto_hidro_aviao = False        
                      
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
            #Escolher quem vai atacar primeiro
            # Iniciar Jogo (Ataque)
            break
        elif(opt==2):
            # Definir Mapa Jogador
            break
        elif(opt==3):
            # Mostrar Mapas
            break
        else:
            print("Opção inválida.")
            print("Aperte 1 para começar ou 2 para o computador começar: ")

if __name__ == "__main__":
    with open("mapas.json", 'r') as file:
        dict_json = json.load(file)
        mapa_pc = dict_json['mapa_ia_2']
        mapa_ia = dict_json['mapa_pc']
    
        mapa_ia_consulta = deepcopy(mapa_ia)
        mapa_jogador_consulta = deepcopy(mapa_pc)
    
    #interface_colocar_navios()   
    for i in range(30):
        ataque()
    printa_mapa()
    print(navios_afundados_ia)

    #mapa_jogador_visivel = adicionar_navio(porta_avioes[0], (1, 1), 5, mapa_jogador_visivel)