import copy
from utils.utils import *
from config import *

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

ship = create_ship(2, 3, [2, 4, 6])
posicao_x = 1
posicao_y = 2


        
player_radar = copy.deepcopy(mapa_pc)
player_board = copy.deepcopy(mar_pc)
ai_radar = copy.deepcopy(mapa_ia)
ai_board = copy.deepcopy(mar_ia)
#number_board = copy.deepcopy(mapa_pc)

#iniciar = int(input("Informe 1 para começar ou 2 para o computador começar: "))


""" create_ship(2, 3, [2, 4, 6])
create_ship(2, 3, [1, 3, 5])
create_ship(3, 2, [1, 4, 5])
create_ship(3, 2, [2, 3, 6]) """



print_board()