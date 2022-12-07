import json
from batalha_naval import *
         
def main():
    pass
                        
#mapa_pc = put_ships(mapa_pc)
#mapa_ia = put_ships(mapa_ia)

with open("mapas.json", 'r') as file:
    dict_json = json.load(file)
    mapa_pc = dict_json['mapa_pc']
    mapa_ia = dict_json['mapa_ia']
    #mapa_ia_visivel = dict_json['mapa_ia']
    #mapa_pc_visivel = dict_json['mapa_pc']
    
#ataque(mapa_pc, mapa_pc_visivel)

             
printa_mapa()