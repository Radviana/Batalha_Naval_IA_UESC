""" def get_empty_positions(map):
    posicoes_vazias = set()
    #qtds_navios = [qtd_submarino, qtd_corveta, qtd_fragata, qtd_cruzador, qtd_porta_aviao]
    #limites_for = [10, 9, 8, 7, 6]
    #qtds_vazios = [1, 2, 3, 4, 5]
    qtds_navios = [qtd_fragata]
    limites_for = [8]
    qtds_vazios = [3]
    
    # Verifica posições livres návios, exceto hidro-aviões
    for qtd_navio, limite_for, qtd_vazio in zip(qtds_navios, limites_for, qtds_vazios):
        if qtd_navio > 0:
            for i in range(limite_for):
                for j in range(limite_for):
                    qtd_vazio_vertical = 0
                    qtd_vazio_horizontal = 0
                
                    for k in range(limite_for - 1):
                        if map[k][i] == 0:
                            qtd_vazio_vertical += 1
                        if map[i][k] == 0:
                            qtd_vazio_horizontal += 1
                    
                        if qtd_vazio_horizontal == qtd_vazio or qtd_vazio_vertical == qtd_vazio:
                            posicoes_vazias.add((i, j))
                    qtd_vazio_vertical, qtd_vazio_horizontal = 0, 0                          
         
    return posicoes_vazias """