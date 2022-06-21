import datetime
import os
import pickle

class Mora:
    def incrementaId(self):
        self.incrementaId.id += 1
        return self.incrementaId.id

    incrementaId.id = 0

    def __init__(self):
        self.id = self.incrementaId()
        self.importo = 0.0
        self.nota = ''
        self.data_emissione = datetime(1970, 0, 0, 0)

    #metodi get e set dei vari attributi
    def getId(self):
        return self.id

    def setImporto(self, importo):
        self.importo = importo

    def getImporto(self):
        return self.importo

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return self.nota

    def setData_emissione(self, data_emissione):
        self.data_emissione = data_emissione

    def getData_emissione(self):
        return self.data_emissione

    def stampa(self):
        return
