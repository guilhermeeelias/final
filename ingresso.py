ingressoLIST = []

#venda_ingresso_meia
#venda_ingresso_inteira


def criar_sessao():
    ingresso = []
    sessaoLIST.append(sessao)

#ingressos vendidos

def listar_ingressos():
    return ingresso


def buscar_ingresso(cod_ingresso):
    for p in ingresso:
        if (p[0]==cod_ingresso):
            return cod_ingresso
        return None


def remover_ingresso(cod_ingresso):
    for p in ingresso:
        if (p[0] == cod_ingresso):
            ingressoLIST.remove(p)
            return True
    return False


def remover_todos_ingressos():
    global ingresso
    ingresso = []
