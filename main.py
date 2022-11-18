import numpy as np
from random import randint
import copy

oceano = "~"
agua = "X"
acerto = "*"
tamanho = 10
vida_jog = 45
vida_ia = 45

mar = []
for x in range(tamanho):
    mar.append([oceano] * tamanho)

def print_board():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("    1 2 3 4 5 6 7 8 9 10 || 1 2 3 4 5 6 7 8 9 10")
    i = 0
    for row in range(tamanho):
        print(i+1, " ", " ".join(player_radar[row]), " ||" , " ".join(player_board[row]))
        i += 1

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

iniciar = int(input("Informe 1 para começar ou 2 para o computador começar: "))

print_board()