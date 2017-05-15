atores = []


def adicionar_ator(cod_ator, nome, nacionalidade, idade):    
    ator = [cod_ator, nome, nacionalidade, idade]
    atores.append(ator)
    
def listar_atores():
    return atores

def buscar_ator(cod_ator):
    for p in atores:
        if (p[0] == cod_ator):
            return p
    return None
        
def remover_ator(cod_ator):
    for p in atores:
        if (p[0] == cod_ator):
            atores.remove(p)
            return True
    return False

def remover_todos_atores():
    global atores
    atores = []       
    
def iniciar_atores():
    adicionar_ator(22222222222, "Charles", "Brazil", 15)
    adicionar_ator(11111111111, "Joao", "puta que pariu", 16)
    
