import numpy as np
from copy import deepcopy

def criar_navio(linha: int, coluna: int, coord_navio: list) -> np.ndarray:
    navio = np.zeros(linha * coluna)
    
    for coord in coord_navio:
        navio[coord - 1] = 1
    navio = navio.reshape((linha, coluna))
    
    return navio

def adicionar_navio(navio: np.array, coords: set or list, mapa: np.array) -> np.array:
    """Posiciona o navio no mapa
    ship: O Navio a ser posicionado
    coords: coordenada X e Y
    mapa: o mapa"""
    coord_x, coord_y = coords
    tmp_mapa = deepcopy(mapa)
    
    # Verifica Esquerda e direita do návio verificando se tem barco perto ou não
    for linha in range(coord_x - 1, navio.shape[0] + coord_x):
        if 0 <= coord_y - 2 <= 9 and 0 <= linha <= 9 and mapa[linha][coord_y - 2] != 0:
            # print("tem navio na esquerda")
            return mapa
        if coord_y + navio.shape[1] - 1 <= 9 and 0 <= linha <= 9 and mapa[linha][coord_y + navio.shape[1] - 1] != 0:
            # print("tem navio na direita")
            return mapa
         
    # Verifica cima e baixo do návio verificando se tem barco perto ou não
    for coluna in range(coord_y - 1, navio.shape[1] + coord_y):
        if 0 <= coord_x - 2 <= 9 and 0 <= coluna <= 9 and mapa[coord_x - 2][coluna] != 0:
            # print("tem navio em cima")  
            return mapa
        if 0 <= coord_x + navio.shape[0] - 1 <= 9 and 0 <= coluna <= 9 and mapa[coord_x + navio.shape[0] - 1][coluna] != 0: 
            # print("tem navio em baixo")
            return mapa

    # Poem navio no mapa temporário
    for linha in range(navio.shape[0]):
        tmp_x = coord_x
        tmp_y = coord_y
        
        for coluna in range(navio.shape[1]):
            tmp_y = coord_y + coluna - 1
            tmp_x = coord_x + linha - 1
            
            # Verifica se a posição é agua e se o index não excede
            if (0 <= tmp_x <= 9 and 0 <= tmp_y <= 9 and tmp_mapa[tmp_x][tmp_y] == 0):  
                tmp_mapa[tmp_x][tmp_y] = navio[linha][coluna]
            else:
                # print("tem navio na área ou posição invalida...")
                return mapa
    return tmp_mapa