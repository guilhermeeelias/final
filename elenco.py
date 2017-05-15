elencolis = []


def adicionar_elenco(cod_elenco,cod_ator,cod_filme,tipo):
    elenco = [cod_elenco,cod_ator,cod_filme,tipo]
    elencolis.append(elenco)
    
def listar_elencos():
    return elencos


def consultar_atores_por_filme(cod_elenco):
    for p in filme:
        if (p[0] == cod_elenco):
            return cod_elenco
    return None

def remover_elenco(cod_elenco):
    for p in elencolis:
        if (p[0] == cod_elenco):
            elencolis.remove(p)
            return True
    return False

def buscar_elenco(cod_elenco):
    for p in elencolis:
        if (p[0] == cod_elenco):
            return cod_elenco
    return None

def buscar_elenco_por_filme(cod_filme):
    for p in elencolis:
        if (p[0] == cod_filme):
            return cod_filme
    return None
