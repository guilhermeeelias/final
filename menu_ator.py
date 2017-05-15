from logica import ator


def imprimir_ator(ator):
    print ("Código do ator: ",  ator[0])
    print ("Nome: ", ator[1])
    print ("Nacionalidade: ",  ator[2])
    print ("Idade: ", ator[3])
    print ()

def menu_adicionar():
    print ("\nAdicionar ator \n")
    cod_ator = int(input("Código do ator: "))
    nome = str (input("Nome: "))
    nacionalidade = str(input("Nacionalidade: "))
    idade = int(input("Idade: "))
    ator.adicionar_ator(cod_ator, nome, nacionalidade, idade)

def menu_listar():
    print ("\nListar Atores \n")
    atores = ator.listar_atores()
    for p in atores:
        imprimir_ator(p)


def menu_buscar():
    print ("\nBuscar ator por código \n")
    cod_ator = int(input("Código do ator: "))
    p = ator.buscar_ator(cod_ator)
    if (p == None):
        print ("Ator não encontrado")
    else:
        imprimir_ator(p)
  
def menu_remover():
    print ("\nRemover ator \n")
    cod_ator = int(input("Código ator: "))
    p = ator.remover_ator(cod_ator)
    if (p == False):
        print ("Ator não encontrado")
    else:
        print ("Ator removido")
    

def mostrar_menu():
    run_ator = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo Ator \n" +
             "(2) Listar Ator \n" +
             "(3) Buscar Ator pelo Codigo \n" +
             "(4) Remover ator \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_ator):
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
            run_ator = False
    
