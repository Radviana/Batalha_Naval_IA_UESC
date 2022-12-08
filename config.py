import numpy as np
from create_set_ship.create_set_ship import *

agua = "~"
falha = "X"
acerto = "*"
barco = '1' # '^'

# Variáveis MAPA
tamanho = 10
vida_jog , vida_ia = (45, 45)

mapa_ia_consulta = np.zeros((tamanho, tamanho), dtype=int) # Consulta
mapa_jogador_consulta = np.zeros((tamanho, tamanho), dtype=int) # Consulta

mapa_ia_visivel = np.zeros((tamanho, tamanho), dtype=int) # Visivel
mapa_jogador_visivel = np.zeros((tamanho, tamanho), dtype=int) # Visivel

# Navios
submarino = [criar_navio(1, 1, [1])]
corvetas = [criar_navio(2, 1, [1, 2]), criar_navio(1, 2, [1, 2])]
fragatas = [criar_navio(3, 1, [1, 2, 3]), criar_navio(1, 3, [1, 2, 3])]
cruzadores = [criar_navio(4, 1, [1, 2, 3, 4]), criar_navio(1, 4, [1, 2, 3, 4])]
porta_avioes = [criar_navio(5, 1, [1, 2, 3, 4, 5]), criar_navio(1, 5, [1, 2, 3, 4, 5])]
hidro_avioes = [criar_navio(2, 3, [2, 4, 6]), criar_navio(2, 3, [1, 3, 5]), criar_navio(3, 2, [1, 4, 5]),
               criar_navio(3, 2, [2, 3, 6])]

qtd_submarino = 3
qtd_corveta = 2
qtd_fragata = 3
qtd_cruzador = 1
qtd_porta_aviao = 1
qtd_hidro_aviao = 2

# Variáveis IA
acerto_ia = False
posicao_acerto = None