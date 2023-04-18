import database
from Classes import Corrida, Motorista, Passageiro
from database import Database
from motoristaDAO import motoristadao

co=Corrida()
co.valor=18
co.nota=10
co.distancia=1
co.passageiro="Andressa"

motorista1=Motorista()
motorista1.__int__(co)
motorista1.InserirCorrida(co)


passageiro=Passageiro()
passageiro.nome='Andressa'
passageiro.documento="13277253635"

db=Database()
motorista=motoristadao()
motorista.__int__(co)
motorista.gravarCorridasBD()


