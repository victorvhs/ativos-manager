#from bd.py import buscar
import dataBase
buscaID = dataBase.buscar("1");

print( dataBase.buscarTabela("user") )
print( dataBase.buscarTabela("ativos") )
print( dataBase.buscarTabela("privilegios") )
print(dataBase.buscarTabela("tipos_ativos"))
campos=["nome,tipo,local,posicao,data"]
dataBase.gravar("ativo",campos,["coelho",1,"pais das maravilhas","ok","12/09/1945"])
print( dataBase.buscarTabela("ativos") )
