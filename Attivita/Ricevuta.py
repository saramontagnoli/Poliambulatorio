"""
    Classe di modellazione per la Ricevuta
    Rappresenta il documento di fatturazione per il Paziente che ha effettuato una visita (rilasciato da Amm.)
"""

import datetime
from Gestione.GestoreFile import scriviFile


class Ricevuta:

    """
        Costruttore della classe
        Set degli attributi di Ricevuta secondo i parametri passati
        Scrittura su file della informazioni della Ricevuta creata
    """
    def __init__(self, id, importo):
        self.id = id
        self.importo = importo
        self.data_ora = datetime.datetime.today()

        # scrittura su file delle informazioni di Ricevuta, chiamata al GestoFile
        scriviFile("Ricevute", self)




    # CANCELLARE I SET E GET
    # CANCELLARE I SET E GET
    # CANCELLARE I SET E GET
    def setImporto(self, importo):
        self.importo = importo

    def setData_ora(self, data_ora):
        self.data_ora = data_ora

    def getId(self):
        return self.id

    def getImporto(self):
        return self.importo

    def getData_ora(self):
        return self.data_ora

    def visualizza(self):
        return
