elencos = []


def adicionar_elenco(cod_elenco, cod_ator, cod_filme, tipo):
    elenco = [cod_elenco, cod_ator, cod_filme, tipo]
    elencos.append(elenco)

def listar_elencos():
    return elencos

def buscar_elenco(cod_elenco):
    for m in elencos:
        if (m[0] == cod_elenco):
            return m
    return None

def buscar_elenco_por_filme(cod_filme):
    for m in elencos:
        if (m[2] == cod_filme):
            return m
        return None



def remover_elenco(cod_elenco):
    for m in elencos:
        if (m[0] == cod_elenco):
            elencos.remove(m)
            return True
    return False

def remover_todos_elencos():
    global elencos
    elencos =  []

def iniciar_elencos():
    adicionar_elenco(2222, 3333, 4444, "Carlos")
    adicionar_elenco(1111, 2222, 3333, "Maria")

