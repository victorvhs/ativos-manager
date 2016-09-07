# dataBase.py
"""Módulo de formatação de strings.
"""
import mysql.connector as mariadb
mariadb_connection = mariadb.connect(user='root', password='1234', database='mydb')
cursor = mariadb_connection.cursor()

#SELECT
def buscar(idativo):
	cursor.execute("SELECT * FROM ativos WHERE idativos=%s" %(idativo))
	data = cursor.fetchone()
	return data

def buscarTabela(tabela):
	try:
		cursor.execute("SELECT * FROM %s " %(tabela.lower()))
		data = cursor.fetchall()
		return data
	except mariadb.Error as error:
		print("Problemas no paraiso")
		print("Erro {}".format(error))
	else:
		mariadb_connection.close()

def gravar(tabela,campos,valores):
	try:
		cursor.execute("INSERT INTO %s(%s) VALUES(%s)"%(tabela,campos,valores))
	except mariadb.Error as error:
		print("Problemas no paraiso")
		print("Erro {}".format(error))
	else:
		mariadb_connection.commit()
		mariadb_connection.close()
