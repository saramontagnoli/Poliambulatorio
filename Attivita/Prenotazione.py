import os
import pickle
import datetime


class Prenotazione:

    # costruttore di Prenotazione
    def __init__(self):
        self.id = 0
        # self.data = datetime.datetime(1970, 1, 1)
        self.data = ""
        self.ora = ""
        self.id_paziente = ""
        self.id_medico = ""
        self.id_visita = ""
        self.scaduta = False
        self.disdetta = False
        self.conclusa = False
        # aggiungere il referto, mora e ricevuta

    def aggiungiPrenotazione(self, id, data, ora):
        self.id = id
        self.data = data
        self.ora = ora
        prenotazioni = {}
        # Apertura e scrittura su file della prenotazione
        if os.path.isfile('File/Prenotazioni.pickle'):
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
        if os.path.isfile('File/Prenotazioni.pickle'):
            with open('File/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
                return prenotazioni[id]
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

    def disdiciPrenotazione(self):
        """self.id = id
        print(id)
        self.data = data
        print(data)
        self.ora = ora
        print(ora) """
        if not self.disdetta:
            self.disdetta = True
            prenotazioni = {}
            # Apertura e scrittura su file della prenotazione
            if os.path.isfile('File/Prenotazioni.pickle'):
                print("File aperto")
                with open('File/Prenotazioni.pickle', 'rb') as f:
                    prenotazioni = pickle.load(f)
            prenotazioni[self.id] = self
            with open('File/Prenotazioni.pickle', 'wb') as f:
                pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
            return True
        else:
            return False

    def scadenzaPrenotazione(self):
        if not self.scaduta:
            print("PROVA PRE FUNZIONE")
            # data1 = datetime.strptime(self.data, '%d/%m/%y')
            print("PROVA")
            print(self.data)
            print(datetime.datetime.today())
            if self.data <= datetime.datetime.today():
                # and self.conclusa == False and self.disdetta == False
                self.scaduta = True
                print(self.scaduta)
                prenotazioni = {}
                # Apertura e scrittura su file della prenotazione
                if os.path.isfile('File/Prenotazioni.pickle'):
                    print("File aperto")
                    with open('File/Prenotazioni.pickle', 'rb') as f:
                        prenotazioni = pickle.load(f)
                prenotazioni[self.id] = self
                with open('File/Prenotazioni.pickle', 'wb') as f:
                    pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
                    return True
        else:
            return False
