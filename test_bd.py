#from bd.py import buscar
import dataBase
buscaID = dataBase.buscar("1");

print( dataBase.buscarTabela("user") )
print( dataBase.buscarTabela("ativos") )
print( dataBase.buscarTabela("privilegios") )
print(dataBase.buscarTabela("tipos_ativos"))
campos=["idtipo_ativos,nome"]
valores=["","Ebook"]
dataBase.gravar("tipos_ativos","idtipo_ativos,nome","","Ebook")
print( dataBase.buscarTabela("ativos") )
