elencos = []


def adicionar_elenco(cod_elenco, nome):    
    elenco = [cod_elenco, nome]
    elencos.append(elenco)
    
def listar_elencos():
    return elencos

def buscar_elenco(cod_elenco):
    for m in elencos:
        if (m[0] == cod_elenco):
            return m
    return None

# def buscar elenco_por_filme(cod_filme)


        
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
    adicionar_elenco(2222, "Carlos")
    adicionar_elenco(1111, "Maria")
    
