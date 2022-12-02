import copy
from config import *
from utils.utils import *

def print_board() -> None:
    #numbers = [i for i in range(1, 11)]
    print("\t   IA\t\t\t   Player")
    print("    1 2 3 4 5 6 7 8 9 10 || 1 2 3 4 5 6 7 8 9 10")
    print("    _____________________||_____________________")
    for row in range(tamanho):
        if row == 9:
            espace = " " * 1
        else:
            espace = " " * 2 
          
        tmp_ia = list(map(str, list(ai_radar[row])))
        tmp_pc = list(map(str, list(player_radar[row])))
            
        tmp_ia = list(map(replace_to_print, tmp_ia))
        tmp_pc = list(map(replace_to_print, tmp_pc))
            
        tmp_ia = ' '.join(tmp_ia)
        tmp_pc = ' '.join(tmp_pc) 
             
        print(f"{row + 1}{espace}|{tmp_ia}  || {tmp_pc} |")
    print("   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
            
def ataque():
        print("Faça 3 ataques: ")
        for i in range(3):
                x = int(input("Informe a linha: "))
                y = int(input("Informe a coluna: "))

def put_ships(map):
    #ships = [submarino, corvetas, fragatas, cruzadores, porta_avioes, hidro_avioes]
    ships = [porta_avioes]
    #ship_names = ['Submarino', 'Corveta', 'Fragata', 'Cruzador', 'Porta avião', 'Hidro Avião']
    ship_names = ['Porta Avião']
    
    for ship, ship_name in zip(ships, ship_names):
        op = -1
        while True:
            print(f"Colocando {ship_name}...")
            x_ship = int(input(f"Digite a posicão X do {ship_name}: "))
            y_ship = int(input(f"Digite a posicão Y do {ship_name}: "))
            ship_orientation = int(input(f"Digite a orientação do {ship_name}: "))
            print(f"X = {x_ship}")
            print(f"Y = {y_ship}")
            print(f"orientação = {ship_orientation}")
            print(f"Navio = {ship[ship_orientation]}")
            
            map = set_ship(ship[ship_orientation], (x_ship, y_ship), map)
            
            op = input("Digite 0 para Sair e qualquer outra tecla para continuar: ")
            print()
            
            if op == '0':
                break
            
    return map
                        
mapa_pc = put_ships(mapa_pc)


player_radar = copy.deepcopy(mapa_pc)
player_board = copy.deepcopy(mar_pc)
ai_radar = copy.deepcopy(mapa_ia)
ai_board = copy.deepcopy(mar_ia)

print_board()