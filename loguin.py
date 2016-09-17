"""
Configuração de acesso
"""
from dataBase import buscarLoguin


def pegar_user():
    user = input("USER: ")
    while True:
        try:
            senha = int(input("SENHA: "))
            break
        except:
            print("PROBLEMAS NO PARAISO")
            print("Senha com problemas")
    cred = {'user': user, 'senha': senha}
    return cred


def verifica():
    cred = pegar_user()
    login = buscarLoguin(cred['user'])
    if not login:
        print("PROBLEMAS NO PARAISO")
    elif cred['senha'] == int(login[2]):
        print("OK")
        return True
    else:
        print("Erro")
        return False
