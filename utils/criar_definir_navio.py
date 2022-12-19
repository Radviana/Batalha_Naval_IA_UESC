import numpy as np
from copy import deepcopy

def criar_navio(linha: int, coluna: int, coord_navio: list) -> np.ndarray:
    navio = np.zeros(linha * coluna)
    
    for coord in coord_navio:
        navio[coord - 1] = 1
    navio = navio.reshape((linha, coluna))
    return navio

def pega_tipo_hidro_aviao(navio: np.array) -> int:
    hidro_avioes = [criar_navio(2, 3, [2, 4, 6]), criar_navio(2, 3, [1, 3, 5]), criar_navio(3, 2, [1, 4, 5]),
                    criar_navio(3, 2, [2, 3, 6])]
    
    for i in range(len(hidro_avioes)):
        if np.array_equal(navio, hidro_avioes[i]):
            return i
    return -1

def adicionar_navio(navio: np.array, coords: set or list, id_navio, mapa: np.array):
    """Posiciona o navio no mapa
    ship: O Navio a ser posicionado
    coords: coordenada X e Y
    mapa: o mapa"""
    coord_x, coord_y = coords # 1 1 -> 0, 0
    tmp_mapa = deepcopy(mapa)
    tipo_hidro_aviao = pega_tipo_hidro_aviao(navio)
    deslocamentos = {'esq': [(1, 0), (0, -1), (0, 0), (1, -1)],
               'dir': [(1, 0), (0, -1), (1, -1), (0, 0)]}
    
    desl_inf_esq, desl_sup_esq, desl_inf_dir, desl_sup_dir = (0, 0, 0, 0)
    
    if id_navio == 6:
        temp_esq = deslocamentos['esq']
        temp_dir = deslocamentos['dir']
        desl_inf_esq, desl_sup_esq = temp_esq[tipo_hidro_aviao]
        desl_inf_dir, desl_sup_dir = temp_dir[tipo_hidro_aviao]
        
    # Verifica Esquerda do návio verificando se tem barco perto ou não
    for linha in range(coord_x - 2 + desl_inf_esq, navio.shape[0] + coord_x + desl_sup_esq): #0, 4
        if 0 <= coord_y - 2 <= 9 and 0 <= linha <= 9 and mapa[linha][coord_y - 2] not in [0, -1]:
            print("tem navio na esquerda")  
            return mapa
        
    # Verifica direita do návio verificando se tem barco perto ou não    
    for linha in range(coord_x - 2 + desl_inf_dir, navio.shape[0] + coord_x + desl_sup_dir):
        if coord_y + navio.shape[1] - 1 <= 9 and 0 <= linha <= 9 and mapa[linha][coord_y + navio.shape[1] - 1] not in [0, -1]:
            print("tem navio na direita")
            return mapa
         
    # Verifica cima e baixo do návio verificando se tem barco perto ou não
    for coluna in range(coord_y - 2, navio.shape[1] + coord_y):
        if 0 <= coord_x - 2 <= 9 and 0 <= coluna <= 9 and mapa[coord_x - 2][coluna] not in [0, -1]:
            print("tem navio em cima")  
            return mapa
        if 0 <= coord_x + navio.shape[0] - 1 <= 9 and 0 <= coluna <= 9 and mapa[coord_x + navio.shape[0] - 1][coluna] not in [0, -1]: 
            print("tem navio em baixo")
            return mapa

    # Poem navio no mapa temporário
    for linha in range(navio.shape[0]):
        tmp_x = coord_x
        tmp_y = coord_y
        
        for coluna in range(navio.shape[1]):
            tmp_y = coord_y + coluna - 1
            tmp_x = coord_x + linha - 1
            
            # Verifica se a posição é agua e se o index não excede
            #print(0 <= tmp_x <= 9 and 0 <= tmp_y <= 9 and tmp_mapa[tmp_x][tmp_y] == 0) and (navio[linha][coluna] == 1)
            if (0 <= tmp_x <= 9 and 0 <= tmp_y <= 9 and tmp_mapa[tmp_x][tmp_y] == 0):
                if (navio[linha][coluna] == 1):  
                    tmp_mapa[tmp_x][tmp_y] = id_navio 
            else:
                # print("tem navio na área ou posição invalida...")
                return mapa
    return tmp_mapa

""" elif 0 <= coord_x-2 and 0 <= coord_y-2 and (tipo_hidro_aviao == 1 or tipo_hidro_aviao == 3)\
        and (navio.shape[0] + coord_x, coord_y-2) == (linha+1, coord_y-2):
            continue
        elif 0 <= coord_x-2 and 0 <= coord_y-2 and (tipo_hidro_aviao == 0 or tipo_hidro_aviao == 2)\
        and (navio.shape[0] + coord_x, coord_y-2) == (linha, coord_y-2):
            continue
        elif 0 <= coord_x-2 and 0 <= coord_y-2 and (tipo_hidro_aviao == 1 or tipo_hidro_aviao == 3)\
        and (navio.shape[0] + coord_x, coord_y-2) == (linha, coord_y-2):
            continue """