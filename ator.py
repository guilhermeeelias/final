ator = []


def adicionar_ator(cod_ator,nome, nacionalidade, idade):
    atores = [cod_ator,nome, nacionalidade, idade]
    ator.append(atores)

def buscar_ator(cod_ator):
    for p in atores:
        if (p[0] == cod_ator):
            return cod_ator
    return None

def remover_ator(cod_ator):
    for p in atores:
        if (p[0] == cod_ator):
            ator.remove(p)
            return True
    return False

def remover_todos_atores():
    global atores
    atores = []

def iniciar_atores():
    adicionar_ator(22222222222, "Guilherme", "Brasileiro", 19)
    adicionar_ator(11111111111, "Daniel", "Romeno", 21)

