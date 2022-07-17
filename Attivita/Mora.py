import datetime
import os
import pickle

class Mora:

    def __init__(self, id, importo, nota, data_emissione):
        self.id = id
        self.importo = importo / 3.0
        self.nota = nota
        self.data_emissione = data_emissione

        more ={}
        if os.path.isfile('File/More.pickle'):
            with open('File/More.pickle', 'rb') as f:
                more = pickle.load(f)
        more[self.id] = self
        with open('File/More.pickle', 'wb') as f:
            pickle.dump(more, f, pickle.HIGHEST_PROTOCOL)

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
