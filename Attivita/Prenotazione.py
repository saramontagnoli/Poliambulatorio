import datetime
import os
import pickle
import pprint


class Prenotazione:

    # costruttore di Prenotazione
    def __init__(self):
        self.id = 0
        self.data = ""
        self.ora = ""
        self.scaduta = False
        self.disdetta = False
        self.conclusa = False
        self.st1 = "AB"
        self.st2 = "BC"

    def aggiungiPrenotazione(self, id, data, ora):
        self.id = id
        print(id)
        self.data = data
        print(data)
        self.ora = ora
        print(ora)
        prenotazioni = {}
        # Apertura e scrittura su file della prenotazione
        if os.path.isfile('File/Prenotazioni.pickle'):
            print("File aperto")
            with open('File/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
        prenotazioni[id] = self
        with open('File/Prenotazioni.pickle', 'wb') as f:
            pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)

    # Ritorna un dizionario con le informazioni di Prenotazione
    def getInfoPrenotazione(self):
        return {
            "id": self.id,
            "data": self.data,
            "ora": self.ora,
            "scaduta": self.scaduta,
            "disdetta": self.disdetta,
            "conclusa": self.conclusa
        }

    # Ricerca prenotazione per id
    def ricerca(self, id):

        print("Sono in ricerca di Id. [" + id+"]")
        if os.path.isfile('File/Prenotazioni.pickle'):
            with open('File/Prenotazioni.pickle', 'rb') as f:
                print("File aperto")
                prenotazioni = dict(pickle.load(f))
                print("Dict caricato")
                # print(prenotazioni.get(self,id))
                # id2 = int(id)
                return prenotazioni.get(id, None)
        else:
            return None

    # Definizione di tutti i metodi getter degli attributi di prenotazione
    def getId(self):
        return self.id

    def getData(self):
        return self.data

    def getOra(self):
        return self.ora

    def isScaduta(self):
        return self.scaduta

    def isDisdetta(self):
        return self.disdetta

    def isConclusa(self):
        return self.conclusa

    # Definizione di tutti i metodi setter degli attributi di prenotazione
    def setData(self, data):
        self.data = data

    def setOra(self, ora):
        self.ora = ora

    def setDisdetta(self, disdetta):
        self.disdetta = disdetta

    def setConclusa(self, conclusa):
        self.conclusa = conclusa
