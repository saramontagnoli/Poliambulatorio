import datetime
import os
import pickle


class Prenotazione:

    def __init__(self):
        self.id = 0
        self.data = datetime.date(1970, 1, 1)
        self.ora = datetime.time(0, 0)
        self.scaduta = False
        self.disdetta = False
        self.conclusa = False

    def aggiungiPrenotazione(self, id, data, ora, scaduta, disdetta, conclusa):
        self.id = id
        self.data = data
        self.ora = ora
        self.scaduta = scaduta
        self.disdetta = disdetta
        self.conclusa = conclusa
        prenotazioni = {}
        if os.path.isfile('File/Prenotazioni.pickle'):
            with open('File/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
        prenotazioni[id] = self
        with open('File/Prenotazioni.pickle', 'wb') as handle:
            pickle.dump(prenotazioni, handle, pickle.HIGHEST_PROTOCOL)

    def getID(self):


    def getData(self):

    def getOra(self):

    def isScaduta(self):

    def isDisdetta(self):

    def isConclusa(self):

    def setData(self, data):
        self.data = data

    def setScaduta(self, scaduta):
        self.scaduta = scaduta

    def setOra(self, ora):
        self.ora = ora

    def setDisdetta(self, disdetta):
        self.disdetta = disdetta

    def setConclusa(self, conclusa):
        self.conclusa = conclusa
