from logica import elenco

def imprimir_elenco(elenco):
    print ("Codigo elenco: ",  elenco[0])
    print ("Nome: ", elenco[1])
    
    print ()

def menu_adicionar():
    print ("\nAdicionar elenco \n")
    cod_elenco = int(input("Código do Elenco: "))
    nome = str (input("Nome: "))
    
    elenco.adicionar_elenco(cod_elenco, nome)

def menu_listar():
    print ("\nListar medicos \n")
    elencos = elenco.listar_elencos()
    for m in elencos:
        imprimir_elenco(m)


def menu_buscar():
    print ("\nBuscar elenco pelo código \n")
    cod_elenco = int(input("Código: "))
    m = elenco.buscar_elenco(cod_elenco)
    if (m == None):
        print ("elenco não encontrado")
    else:
        imprimir_elenco(m)
  
def menu_remover():
    print ("\nRemover elenco \n")
    cod_elenco = int(input("Código do elenco: "))
    m = elenco.remover_elenco(cod_elenco)
    if (m == False):
        print ("Elenco não encontrado")
    else:
        print ("Elenco removido")
    

def mostrar_menu():
    run_elenco = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo Elenco \n" +
             "(2) Listar elencos \n" +
             "(3) Buscar elenco por Codigo do elenco \n" +
             "(4) Remover elenco \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_elenco):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif (op == 4):
            menu_remover()
        elif (op == 0):
            run_medico = False

if __name__ == "__main__":
    mostrar_menu()
    
