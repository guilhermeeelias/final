sessoes=[]

def criar_sessao(cod_sessao, cod_filme,cod_sala,horario):
    sessao=[cod_sessao, cod_filme,cod_sala,horario]
    sessoes.append(sessao)

def buscar_sessao(cod_sessao):
    for s in sessoes:
        if ~(s[0]== cod_sessao):
            return s
    return None
def verificar_lotacao():
#tbd
def listar_sessoes():
    return sessoes

def remover_sessoes():
    for j in sessoes:
        if (j[0] == cod_sessao):
            sessoes.remove(p)
            return True
    return False

def remover_todas_as_sessoes():
    global sessoes
    sessoes=[]

def iniciar_ingressos():
    #tbd
