filmes=[]

def cadastrar_filme(cod_filme, titulo, duracao, classificacao, diretor, distribuidora,status,genero):
    filme=[cod_filme, titulo, duracao, classificacao, diretor, distribuidora,status,genero]
    filmes.append(filme)

def buscar_filme(cod_filme):
    for p in filmes:
        if (p[0] ==cod_ator):
            return p
        return None

def listar_filmes():
    return filmes

def remover_todos_filmes():
    global filmes
    filmes=[]

def iniciar_filmes():
    cadastrar_filme(22222,'Pulp Fiction','2h30','livre','Tarantino','distribuidoraX','disponivel','terro')
