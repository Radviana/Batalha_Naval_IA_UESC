import numpy as np

# Variáveis MAPA
agua = "~"
falha = "X"
acerto = "*"
barco = '^'
tamanho = 10
vida_jog , vida_ia = (45, 45)

mapa_ia = np.zeros((tamanho, tamanho), dtype=int) # Consulta
mapa_pc = np.zeros((tamanho, tamanho), dtype=int) # Consulta

mar_ia = np.zeros((tamanho, tamanho), dtype=int) # Visivel
mar_pc = np.zeros((tamanho, tamanho), dtype=int) # Visivel

# Navios
submarino = [1]

base_range = 2
base_ship = [{'shape': np.array([2, 1]), 'coordinate': [i for i in range(1, base_range + 1)]},
            {'shape': np.array([1, 2]), 'coordinate': [i for i in range(1, base_range + 1)]}]

tmp = base_ship[0]['shape']
# print(tmp + 1)