

class Corrida:
    def __int__(self,nota:int,distancia:float,valor:float, passageiro:Passageiro):
        self.nota=nota
        self.distancia=distancia
        self.valor=valor
        self.passageiro=passageiro


class Motorista:
    def __int__(self,nota:int, corrida:Corrida):
        self.nota=nota
        self.corridas=corrida
        self.corridas=[]
    def InserirCorrida(self,corrida):
        self.corridas.append(corrida)

class Passageiro:
    def __int__(self,nome:str,documento:str):
        self.nome=nome
        self.documento=documento


