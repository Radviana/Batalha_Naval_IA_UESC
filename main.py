import numpy as np
from random import randint
import copy
from utils.utils import *
from config import *

mar = []
for x in range(tamanho):
    mar.append([oceano] * tamanho)

def print_board() -> None:
    #numbers = [i for i in range(1, 11)]
    print("    1 2 3 4 5 6 7 8 9 10 || 1 2 3 4 5 6 7 8 9 10")
    
    espace = " " * 3
    for i, row in enumerate(range(tamanho), 1):
        if i == 10:
            espace = " " * 2    
        print(f"{i}{espace}{' '.join(player_radar[row])}  || {' '.join(player_board[row])}")
            
def ataque():
        print("Faça 3 ataques: ")
        for i in range(3):
                x = int(input("Informe a linha: "))
                y = int(input("Informe a coluna: "))

player_radar = copy.deepcopy(mar)
player_board = copy.deepcopy(mar)
ai_radar = copy.deepcopy(mar)
ai_board = copy.deepcopy(mar)
number_board = copy.deepcopy(mar)

#iniciar = int(input("Informe 1 para começar ou 2 para o computador começar: "))

#print_board()
create_ship(2, 3, [2, 4, 6])