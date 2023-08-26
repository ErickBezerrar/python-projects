def eat_ghost(bolinha_energia_ativa, pacman_tocando_fantasma):
    if (bolinha_energia_ativa == True & pacman_tocando_fantasma == True):
        return True
    elif(bolinha_energia_ativa == False & pacman_tocando_fantasma == True):
        return False
    elif(bolinha_energia_ativa == False & pacman_tocando_fantasma == False):
        return False
    elif(bolinha_energia_ativa == True & pacman_tocando_fantasma == False):
        return False
    
    

def score(pacman_tocando_pallet_energia_ativa, pacman_tocando_ponto):
    return 0