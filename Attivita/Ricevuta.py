import datetime
import os
import pickle

class Ricevuta:

    def __init__(self, id, importo):
        self.id = id
        self.importo = importo
        self.data_ora = datetime.datetime.today()

        ricevute ={}
        if os.path.isfile('File/Ricevute.pickle'):
            with open('File/Ricevute.pickle', 'rb') as f:
                ricevute = pickle.load(f)
        ricevute[self.id] = self
        with open('File/Ricevute.pickle', 'wb') as f:
            pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)


    #Metodi Setter per gli attributi
    def setImporto(self, importo):
        self.importo = importo

    def setData_ora(self, data_ora):
        self.data_ora = data_ora

    #Metodi getter degli attributi
    def getId(self):
        return self.id

    def getImporto(self):
        return self.importo

    def getData_ora(self):
        return self.data_ora

    def visualizza(self):
        return
