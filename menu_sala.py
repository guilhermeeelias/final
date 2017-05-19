from logico import sala

def imprimir_sala(sala):
    print("Codigo da sala: ",sala[0])
    print("Definir lotação: "sala[0])
    print()

def menu_status_ocupado():
    ###


def menu_status_livre():
    ###

def menu_buscar():
    print("\nBuscar sala por codigo: ")
    cod_sala=int(int("Codigo do ator: "))
    s=sala.buscar_sala(cod_sala)
    if (s==None):
        print("Sala nao encontrada")
    else:
        imprimir_sala(s)

def menu_listar():
    print("\nListar salas: \n")
    sala=sala.listar_salas()
    for s in salas:
        imprimir_sala(s)

def menu_remover():
    print ("\nRemover sala\n")
    cod_sala=int(input("Codigo sala: "))
    s=sala.remover_filme(cod_sala)
    if (s==False):
        print("Sala não encontrado ")
    else:
        print("Sala removida")

def mostrar_menu():
    run=True
    menu = ("\n-----------------------\n"+
                "(1)Adincionar sala \n"+
                "(2)Definir status ocupado"+
                "(3)Definir stuats livre"+
                "(4)Buscar lista"+
                "(5)Listar sala \n"+
                "(6)Remover sala\n"+
                "(7)Remover todas as salas"+
                "(0)Voltar\n"+
                "------------------------")

    while(run_sala):
        print(sala)
        op=int(input("Digite sua escolha: "))

        if(op==1):
            menu_adicionar()
        #elif(op==2):
        #    menu_
        #elif(op==3):
        #   menu_
        elif(op==4):
            menu_buscar()
        elif(op==5):
            menu_listar()
        elif(op==6):
            menu_remover
        #elif(op==7):
         #   menu_
        elif(op==0):
            run_filme=False