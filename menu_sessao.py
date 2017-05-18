from logica import sessao

def imprimir_sessao(sessao):
    print("Codigo da sessao: ", sessao[0])
    print("Codigo do filme: ", sessao[1])
    print("Codigo da sala: ", sessao[2])
    print("Horario: ", sessao[3])

def menu_criar():
    print("\nCriar sessão: ")
    cod_sessao=int(input("Codigo do ator: "))
    cod_filme=int(input("Codigo do filme: "))
    cod_sala=int(input("Codigo da sala: "))
    horario=int(input("Horario: "))
    sessao.criar_seesao(cod_sessao, sessao_filme, cod_sala, horario)


def menu_listar():
    print("\nListar Sessoes: ")
        sessoes=sessao.listar_sessoes()
        for j in sessoes
            imprimir_sessao(j)

def menu_buscar():
    print("\nBuscar sessao por codigo: \n")
    cod_sessao= int(input("Codigo da sessão: "))
    j=sessao.buscar_sessao(cod_sessao)
    if(j==None):
        print("Sessão nao encontrada")
    else:
        imprimir_sessao(j)

def menu_remover():
    print ("\nRemover sessao\n ")
    cod_sessao=int(int("Codigo da sessão: "))
    j=sessao.remover_sessoes(cod_sessao)
    if (j==False):
        print("Sessão não encontrada ")
    else:
            print("Sessão removida")

def monstrar_menu():
    run_sessao=True
    menu=("\n------------------------\n"+
                    "(1)Criar sessão \n"+
                    "(2)Listar sessões \n"+
                    "(3)Buscar sessão \n"+
                    "(4)Remover sessão \n"+
                    "(5)"+
                    "(0) Voltar\n"+
                    "-------------------")

while(run_sessao):
    print(menu)
    op=int(int("Digite sua escolha: "))
    if(op==1):
        menu_criar()
    elif (op==2):
        menu_listar()
    elif(op==3)
        menu_buscar()
    elif(op==4)
        menu_remover()

    elif (op==0):
        run_sessao=False
