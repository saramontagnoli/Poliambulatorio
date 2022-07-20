import datetime
from Gestione.GestoreFile import scriviFile


class Ricevuta:

    def __init__(self, id, importo):
        self.id = id
        self.importo = importo
        self.data_ora = datetime.datetime.today()

        scriviFile("Ricevute", self)

    # Metodi Setter per gli attributi
    def setImporto(self, importo):
        self.importo = importo

    def setData_ora(self, data_ora):
        self.data_ora = data_ora

    # Metodi getter degli attributi
    def getId(self):
        return self.id

    def getImporto(self):
        return self.importo

    def getData_ora(self):
        return self.data_ora

    def visualizza(self):
        return
