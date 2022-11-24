import numpy as np
from copy import deepcopy
from config import *

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
    
    print_ship(ship)
    
    return ship

def set_ship(ship: np.array, coords: set or list, mapa: np.array) -> bool:
    """Posiciona o navio no mapa
    ship: O Navio a ser posicionado
    coords: coordenada X e Y
    mapa: o mapa"""
    coord_x, coord_y = coords
    tmp_mapa = deepcopy(mapa)

    for row in range(ship.shape[0]):
        tmp_x = coord_x
        tmp_y = coord_y
        
        for column in range(ship.shape[1]):
            tmp_y = coord_y + column - 1
            tmp_x = coord_x + row - 1
                
            tmp_mapa[tmp_x][tmp_y] = ship[row][column]
    mapa = tmp_mapa
    return True

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