import numpy as np
from copy import deepcopy

agua = "~"
falha = "X"
acerto = "*"
barco = '1' # '^'

def replace_to_print(element):
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

def create_ship(row: int, column: int, ship_coord: list) -> np.ndarray:
    ship = np.zeros(row * column)
    
    for coord in ship_coord:
        ship[coord - 1] = 1
    ship = ship.reshape((row, column))
    
    return ship

def set_ship(ship: np.array, coords: set or list, mapa: np.array) -> bool:
    """Posiciona o navio no mapa
    ship: O Navio a ser posicionado
    coords: coordenada X e Y
    mapa: o mapa"""
    coord_x, coord_y = coords
    tmp_mapa = deepcopy(mapa)
    
    # Verifica Esquerda e direita do návio verificando se tem barco perto ou não
    for row in range(coord_x - 1, ship.shape[0] + coord_x):
        if 0 <= coord_y - 2 <= 9 and 0 <= row <= 9 and mapa[row][coord_y - 2] != 0:
            print("tem navio na esquerda")
            return mapa
        if coord_y + ship.shape[1] - 1 <= 9 and 0 <= row <= 9 and mapa[row][coord_y + ship.shape[1] - 1] != 0:
            print("tem navio na direita")
            return mapa
         
    # Verifica cima e baixo do návio verificando se tem barco perto ou não
    for column in range(coord_y - 1, ship.shape[1] + coord_y):
        if 0 <= coord_x - 2 <= 9 and 0 <= column <= 9 and mapa[coord_x - 2][column] != 0:
            print("tem navio em cima")  
            return mapa
        if 0 <= coord_x + ship.shape[0] - 1 <= 9 and 0 <= column <= 9 and mapa[coord_x + ship.shape[0] - 1][column] != 0: 
            print("tem navio em baixo")
            return mapa

    # Poem navio no mapa temporário
    for row in range(ship.shape[0]):
        tmp_x = coord_x
        tmp_y = coord_y
        
        for column in range(ship.shape[1]):
            tmp_y = coord_y + column - 1
            tmp_x = coord_x + row - 1
            
            # Verifica se a posição é agua e se o index não excede
            if (0 <= tmp_x <= 9 and 0 <= tmp_y <= 9 and tmp_mapa[tmp_x][tmp_y] == 0):  
                tmp_mapa[tmp_x][tmp_y] = ship[row][column]
            else:
                print("tem navio na área ou posição invalida...")
                return mapa
    return tmp_mapa

def print_ship(ship):
    row, column = ship.shape
    
    for i in range(row):
        for j in range(column):
            if ship[i][j] == 0:
                print("  ", end='')
            else:
                print(" 1", end='')
        print()
    print()