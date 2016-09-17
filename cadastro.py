import dataBase as db

# Funções para o cadastro


def geraSenha():
    from random import random
    return str(random())[2:8]


def cadUsuario():
    nome = input("Insira o nome: ")
    senha = geraSenha()
    privilegio = 0
    while privilegio != 1 and privilegio != 2:
        privilegio = input("""Insira o privilegio \n\\\
        1 para Administrador\n2 para Usuário comum\n:""")
        try:
            privilegio = int(privilegio)
        except:
            print("Opção errada")
    campos = "'"+nome+"'"+','+"'"+str(senha)+"'"+','+"'"+str(privilegio)+"'"
    db.gravar_user(campos)
    print("Usuário {} cadastrado\nSenha: {}".format(nome, str(senha)))


def cadAtivos():
    nome = input("Nome do Ativo: ")
    tipo = 0
    while not tipo:
        tipo = input("Insira o Tipo do ativo: ")
        try:
            tipo = int(tipo)
        except:
            print("Opção errada")
    local = input('Local do Ativo: ')
    posi = input('Insira o estado de conservação do ativo: ')
    d = input('Insira a data de entrada do ativo: ')
    campos = "'{}','{}','{}','{}','{}'".format(nome, str(tipo), local, posi, d)
    db.gravar_ativo(campos)
    db.buscar('ativos')


def cadTipo():
    nome = input("Insira o nome do Tipo de Ativo: ")
    db.gravar_tipoAtivos(nome)
