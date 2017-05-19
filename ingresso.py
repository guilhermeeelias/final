ingressos=[]

def venda_ingresso_meia(cod_sessao):
    ##tbd##

def venda_ingresso_inteira(cod_sessao):

def listar_ingressos_vendidos(cod_sessao):


def buscar_ingressos(cod_ingresso):
    for i in ingressos:
        if(i[0]==cod_ingresso):
            return i
        return None

def remover_ingresso(cod_ingresso):
    for i in ingressos:
        if (i[0]==cod+ingresso):
            infressos.remove(i)
            return True
        return False

def remover_todos_ingressos():
    global ingressos
    ingressos=[]

