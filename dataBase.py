# dataBase.py
"""Módulo de formatação de strings.
"""
import mysql.connector as mariadb
mariadb_connection = mariadb.connect(user='root',
                                     password='1234', database='mydb')
cursor = mariadb_connection.cursor()

campos_ativos = 'idativos,nome,tipo,local,posicao,data'
campos_tipos_ativos = 'idtipos_ativos,nome'
campos_user = 'iduser,nome,senha,privilegio'
campos_privilegios = 'idprivilegios,privilegio'


def buscar(idativo):
    cursor.execute("SELECT * FROM ativos WHERE idativos=%s" % (idativo))
    data = cursor.fetchone()
    return data


def buscarLoguin(user):
    cursor.execute("SELECT * FROM user WHERE nome='{}'".format(user.lower()))
    data = cursor.fetchone()
    return data


def buscarTabela(tabela):
    try:
        cursor.execute("SELECT * FROM %s " % (tabela.lower()))
        data = cursor.fetchall()
        return data
    except mariadb.Error as error:
        print("Problemas no paraiso")
        print("Erro {}".format(error))
    else:
        mariadb_connection.close()


def gravar_ativo(valores):
    try:
        cursor.execute("""INSERT INTO ativos (idativos,nome,tipo,local,posicao,data)
                                VALUES(null,{})""".format(valores))
    except mariadb.Error as error:
        print("PROBLEMAS NO PARAISO")
        print("Erro {}".format(error))
    else:
        mariadb_connection.commit()


def gravar_tipoAtivos(valores):
    try:
        cursor.execute("""INSERT INTO tipos_ativos({})
                    VALUES(null,'{}')""".format(campos_tipos_ativos, valores))
    except mariadb.Error as error:
        print("PROBLEMAS NO PARAISO")
        print("Erro {}".format(error))
    else:
        mariadb_connection.commit()


def gravar_user(valores):
    try:
        cursor.execute("""INSERT INTO user({})
                VALUES(null,{})""".format(campos_user, valores))
    except mariadb.Error as error:
        print("PROBLEMAS NO PARAISO")
        print("Erro {}".format(error))
    else:
        mariadb_connection.commit()
