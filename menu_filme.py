from logica import filme

def imprimir_filme(filme):
    print("Codigo do filme: ", filme[0])
    print("Titulo do filme: ", filme[1])
    print("Duração do filme: ", filme[2])
    print("Classificação do filme: ", filme[3])
    print("Diretor do filme: ", filme[4])
    print("Distribuidora: ", filme[5])
    print("Status: ", filme[6])
    print("Genero do filme: ", filme[7])
    print()

def menu_buscar():
    print("\nBuscar filme por codigo\n")
    cod_filme = int(input("Codigo do filme: "))
    f = filme.buscar_filme(cod_filme)
    if (f== None):
        print("Filme nao encontrado")
    else:
        imprimir_filme(f)

def menu_listar():
    print("\nListar Filmes \n")
    filmes=filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)


def menu_cadastrar():
    print("\nCadastrar filme\n")
    cod_filme=int(input("Codigo do filme: "))
    titulo=str(input("Titulo do filme: "))
    duracao=str(input("Duração do filme: "))
    classificacao=str(input("Classificação do filme: "))
    diretor=str(input("Diretor do filme: "))
    status=str(input("Status do filme: "))
    distribuidora=str(input("Distribuidora: "))
    genero=str(input("Genero do filme"))
    filme.cadastrar_filme(cod_filme, titulo, duracao, classificacao, diretor, status,distribuidora,genero)


def remover_todos():
    filme.remover_todos_filmes()
    print("FILMES REMOVIDOS")



def mostrar_menu():
    run_filme= True
    menu = ("\n----------------\n"+
             "(1) Buscar filme\n" +
             "(2) Listar filmes \n" +
             "(3) Cadastrar filme  \n" +
             "(4) Remover todos \n" +
             "(0) Voltar\n"+
            "----------------")
    while (run_filme):
        print(menu)
        op=int(input("Digite sua escolha: "))

        if(op==1):
            menu_buscar()
        elif(op==2):
            menu_listar()
        elif(op==3):
            menu_cadastrar()
        elif(op==4):
            remover_todos()
        elif(op==0):
            run_filme= False



