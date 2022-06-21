import datetime
import os
import pickle

class Ricevuta:

    def __init__(self):
        self.id = 0
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
        self.data = date;

    def getData(self):
        return self.date

    def setOra(self, ora):
        self.ora = ora;

    def getOra(self):
        return self.ora


