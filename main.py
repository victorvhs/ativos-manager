
"""
Arquivo Principal da aplicação,
"""
import cadastro as cd
import loguin as lc
import dataBase as db


def buscar():
    while True:
        try:
            print("Para buscar digite a opção: ")
            print("1\tAtivo")
            print("2\tUsuario")
            print("3\tTipos de Ativos")
            op = input("> ")
            op = int(op)
            print(op)
            if op < 1 or op > 3:
                raise Exception()
            break
        except KeyboardInterrupt:
            print("Bye Bye")
            break
        except:
            print("PROBLEMAS NO PARAISO")
            print("Tente novamente")
    if op == 1:
        print("Busca Ativo")
        while True:
            try:
                ativo = int(input("Insira o ID do ativo: "))
                break
            except KeyboardInterrupt:
                print("Bye Bye")
                break
            except:
                print("PROBLEMAS NO PARAISO\nIsso não parece um numero")
        ativo = db.buscar(ativo)
        print(ativo)
    elif op == 2:
        print("Não Definido")
    elif op == 3:
        print("Não Definido")


def menu():
    print("Bem Vindo ao Gestor de Ativos")
    print("Escolha uma opção")
    while True:
        print("1\tPara Cadastrar Ativos")
        print("2\tPara Buscar Ativos")
        print("3\tPara Adminstrador")
        op = 0
        while True:
            try:
                op = input("> ")
                op = int(op)
                break
            except KeyboardInterrupt:
                print("Bye Bye")
                break
            except:
                print("PROBLEMAS NO PARAISO")
                print("Tente outra vez")
        if op == 1:
            cd.cadAtivos()
        elif op == 2:
            buscar()
        elif op == 3:
            print("Não definido")
        break

menu()
