import datetime
import os
import pickle

class Ricevuta:

    def incrementaId(self):
        self.incrementaId.id += 1
        return self.incrementaId.id

    incrementaId.id = 0

    def __init__(self):
        self.id = self.incrementaId()
        self.importo = 0.0
        self.data = datetime.date(1970, 1, 1)
        self.ora = datetime.time(0, 0)

    def getId(self):
        return self.id

    def setImporto(self, importo):
        self.importo = importo

    def getImporto(self):
        return self.importo

    def setData(self, date):
        self.data = date

    def getData(self):
        return self.date

    def setOra(self, ora):
        self.ora = ora

    def getOra(self):
        return self.ora

    def visualizza(self):
        return
