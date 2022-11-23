import numpy as np

def create_ship(row: int, column: int, ship_coord: list) -> np.ndarray:
    ship = np.zeros(row * column)
    
    for coord in ship_coord:
        ship[coord - 1] = 1
    ship = ship.reshape((row, column))
    print(ship)
    
    return ship