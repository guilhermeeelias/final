from logica import ingresso

def imprimir_ingresso(ingresso):
    print("Codigo do ingresso: "ingresso[0])

def menu_listar():
    print("\nListar ingressos \n")
    ingressos=ingresso.listar_ingresso()
    for i in ingressos:
        imprimir_ingresso(i)

def menu_buscar():
    print("\nBuscar ingresso por código ")
    cod_ingresso=int(input("Codigo do ingresso"))
    if (i==None):
        print("Ingresso nao encontrado ")
    else:
        imprimir_ingresso(i)

def menu_remover():
    print ("\nRemover ingresso \n")
    cod_ingresso=int(input("Codigo de ingresso: "))
    i=ingresso.remover_ingresso(cod_ingresso)
    if(i==False):
        print("Ingresso nao encontrado")
    else:
        print("Ingresso removido")


def menu_remover_todos():
    ingresso.remover_todos_ingresos()
        print("Ingressos removidos ")


def mostrar_menu():
    run_ingresso=True
    menu=("\n---------------------\n"+
    "(1)Buscar\n"+
    "(2)Listar\n"+
    "(3)Remover\n"+
    "(4)Remover todos\n"+
    "-------------------")

    while(run_ingresso):
        print(menu)
        op=int(input("Digite sua escolha: "))

        if(op==1):
            menu_buscar()
        elif(op==2):
            menu_listar()
        elif(op==3):
            menu_remover()
        elif(op==4):
            menu_remover_todos()