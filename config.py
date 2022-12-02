import numpy as np
from utils.utils import *

# Variáveis MAPA
tamanho = 10
vida_jog , vida_ia = (45, 45)

mapa_ia = np.zeros((tamanho, tamanho), dtype=int) # Consulta
mapa_pc = np.zeros((tamanho, tamanho), dtype=int) # Consulta

mar_ia = np.zeros((tamanho, tamanho), dtype=int) # Visivel
mar_pc = np.zeros((tamanho, tamanho), dtype=int) # Visivel

# Navios
submarino = [create_ship(1, 1, [1])]
corvetas = [create_ship(2, 1, [1, 2]), create_ship(1, 2, [1, 2])]
fragatas = [create_ship(3, 1, [1, 2, 3]), create_ship(1, 3, [1, 2, 3])]
cruzadores = [create_ship(4, 1, [1, 2, 3, 4]), create_ship(1, 4, [1, 2, 3, 4])]
porta_avioes = [create_ship(5, 1, [1, 2, 3, 4, 5]), create_ship(1, 5, [1, 2, 3, 4, 5])]
hidro_avioes = [create_ship(2, 3, [2, 4, 6]), create_ship(2, 3, [1, 3, 5]), create_ship(3, 2, [1, 4, 5]),
               create_ship(3, 2, [2, 3, 6])]

qtd_submarino = 0
qtd_corveta = 0
qtd_fragata = 0
qtd_cruzador = 0
qtd_porta_aviao = 0
qtd_hidro_aviao = 0