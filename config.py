import numpy as np
from utils.criar_definir_navio import *

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

nomes_navios = ['Submarino', 'Corveta','Fragata', 'Cruzador', 'Porta Avião', 'Hidro Avião']

# Quantidades de navios jogador
qtd_submarino_jogador = 3
qtd_corveta_jogador = 2
qtd_fragata_jogador = 3
qtd_cruzador_jogador = 1 
qtd_porta_aviao_jogador = 1
qtd_hidro_aviao_jogador = 2
qtds_navios_jogador = [qtd_submarino_jogador, qtd_corveta_jogador, qtd_fragata_jogador, qtd_cruzador_jogador, 
                      qtd_porta_aviao_jogador, qtd_hidro_aviao_jogador]

# Quantidades de navios IA
qtd_submarino_ia = 3
qtd_corveta_ia = 2
qtd_fragata_ia = 3
qtd_cruzador_ia = 1
qtd_porta_aviao_ia = 1
qtd_hidro_aviao_ia = 2
qtds_navios_ia = [qtd_submarino_ia, qtd_corveta_ia, qtd_fragata_ia, qtd_cruzador_ia, 
                      qtd_porta_aviao_ia, qtd_hidro_aviao_ia]

# Quantidade de acertos jogador
acertos_submarino_jogador = 0
acertos_corveta_jogador = 0
acertos_fragata_jogador = 0
acertos_cruzador_jogador = 0
acertos_porta_aviao_jogador = 0
acertos_hidro_aviao_jogador = 0
qtds_acertos_jogador = [acertos_submarino_jogador, acertos_corveta_jogador, acertos_fragata_jogador, acertos_cruzador_jogador, 
                        acertos_porta_aviao_jogador, acertos_hidro_aviao_jogador]

# Quantidade de acertos IA
acertos_submarino_ia = 0
acertos_corveta_ia = 0
acertos_fragata_ia = 0
acertos_cruzador_ia = 0
acertos_porta_aviao_ia = 0
acertos_hidro_aviao_ia = 0
qtds_acertos_ia = [acertos_submarino_ia, acertos_corveta_ia, acertos_fragata_ia, acertos_cruzador_ia, 
                        acertos_porta_aviao_ia, acertos_hidro_aviao_ia]

# Limites acertos navios
limite_acertos = [1, 2, 3, 4, 5, 3]

# Variáveis IA
acerto_ia = False
posicao_acerto = None
lados_jogar = []
navio_acertado = None
deslocamento = 0

acerto_cima_esq = False
acerto_cima_dir = False
acerto_baixo_esq = False
acerto_baixo_dir = False

navios_afundados = 0
x, y = 0, 0