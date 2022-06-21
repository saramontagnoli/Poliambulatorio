import datetime
import os
import pickle


class Prenotazione:

    #costruttore di Prenotazione
    def __init__(self):
        self.id = -1
        self.data = datetime.date(1970, 1, 1)
        self.ora = datetime.time(0, 0)
        self.scaduta = False
        self.disdetta = False
        self.conclusa = False

    #metodo per l'aggiunta della prenotazione al file Prenotazioni.pickle
    def aggiungiPrenotazione(self, id, data, ora, scaduta, disdetta, conclusa):
        self.id = id
        self.data = data
        self.ora = ora
        self.scaduta = scaduta
        self.disdetta = disdetta
        self.conclusa = conclusa
        prenotazioni = {}
        #Apertura e scrittura su file della prenotazione
        if os.path.isfile('File/Prenotazioni.pickle'):
            with open('File/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
        prenotazioni[id] = self
        with open('File/Prenotazioni.pickle', 'wb') as handle:
            pickle.dump(prenotazioni, handle, pickle.HIGHEST_PROTOCOL)

    #Definizione di tutti i metodi getter degli attributi di prenotazione
    def getID(self):
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

    #Definizione di tutti i metodi setter degli attributi di prenotazione
    def setData(self, data):
        self.data = data

    def setOra(self, ora):
        self.ora = ora

    def setDisdetta(self, disdetta):
        self.disdetta = disdetta

    def setConclusa(self, conclusa):
        self.conclusa = conclusa
