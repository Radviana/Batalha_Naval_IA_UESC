import json
from config import *
from copy import deepcopy

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
     
def pega_posicoes_disponiveis(mapa):
    posicoes_vazias = set()
    qtds_navios = [qtd_submarino, qtd_corveta, qtd_corveta, qtd_fragata, qtd_fragata, qtd_cruzador, qtd_cruzador, 
                   qtd_porta_aviao, qtd_porta_aviao, qtd_hidro_aviao, qtd_hidro_aviao, qtd_hidro_aviao, qtd_hidro_aviao]
    tipos_navios = submarino + corvetas + fragatas + cruzadores + porta_avioes + hidro_avioes
    
    for tipo_navio, qtd_navio in zip(tipos_navios, qtds_navios):
        if qtd_navio > 0:
            for i in range(1, 11):
                for j in range(1, 11):
                    tmp_mapa = adicionar_navio(tipo_navio, (i, j), mapa)
                    
                    if tmp_mapa != mapa:
                        posicoes_vazias.add((i, j))
                        
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
        
        jogadas_disponiveis = pega_posicoes_disponiveis(mapa_jogador_visivel)
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

if __name__ == "__main__":
    mapa_ia = None
    mapa_pc = None

    with open("mapas.json", 'r') as file:
        dict_json = json.load(file)
        mapa_pc = dict_json['mapa_pc']
        mapa_ia = dict_json['mapa_ia']
        mapa_ia_visivel = dict_json['mapa_ia']
        mapa_pc_visivel = dict_json['mapa_pc']
        
    pos = pega_posicoes_disponiveis(mapa_ia)
    print(len(pos))
    print(sorted(pos))

    #mapa_ia_visivel = mapa_ia
    #mapa_jogador_visivel = mapa_pc
         
    printa_mapa()