salasLIS = []  


def add_sala(cod_sala,lotacao):
    sala = [cod_sala,lotacao]
    salasLIS.append(sala)


def definir_status_ocupada(cod_sala):
    lotacao=='Ocupada'
    return salas



def definir_status_livre(cod_sala):
    lotacao==livre
    return salas



def listar_salas():
    return salasLIS

def buscar_salas(cod_sala):
    for p in filme:
        if (p[0] == cod_sala):
            return cod_sala
    return None

def remover_filme(cod_filme):
    for p in salasLIS:
        if (p[0] == cod_sala):
            salasLIS.remove(p)
            return True
    return False

def remover_todas_salas():
    global salasLIS
    salasLIS = []

def iniciar_salas():
    iniciar_salas('123456790','Disponivel')


