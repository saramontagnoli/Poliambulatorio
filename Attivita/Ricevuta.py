import datetime
import os
import pickle

class Ricevuta:

    def __init__(self):
        self.id = 0
        self.importo = 0.0
        self.data = datetime.date(1970, 1, 1)
        self.ora = datetime.time(0, 0)

    #Metodi Setter per gli attributi
    def setImporto(self, importo):
        self.importo = importo

    def setData(self, date):
        self.data = date

    def setOra(self, ora):
        self.ora = ora

    #Metodi getter degli attributi
    def getId(self):
        return self.id

    def getImporto(self):
        return self.importo

    def getData(self):
        return self.date

    def getOra(self):
        return self.ora

    def visualizza(self):
        return
