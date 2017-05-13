filme = []


def cadastrar_filme(cod_filme,titulo,duracao,classificacao,diretor,distribuidora,status,genero):
    filmes = [cod_filme,titulo,duracao,classificacao,diretor,distribuidora,status,genero]
    filme.append(filmes)

def listar_filmes():
    return filme

def buscar_filme(cod_filme):
    for p in filme:
        if (p[0] == cod_filme):
            return cod_filme
    return None

def remover_filme(cod_filme):
    for p in filme:
        if (p[0] == cod_filme):
            filme.remove(p)
            return True
    return False

def remover_todos_atores():
    global ator
    ator = []

def iniciar_filme():
    adicionar_filme(22222222222, "Rei leao","2 horas","Livre","Guilherme","Distribuidora","Disponivel","Infantil")


