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