import os
import pickle
import datetime


class Prenotazione:

    # costruttore di Prenotazione
    def __init__(self):
        self.id = 0
        self.data = datetime.datetime(1970, 1, 1)
        self.ora = datetime.time(0, 0, 0)
        self.cf_paziente = ""
        self.id_medico = 0
        self.id_visita = 0
        self.scaduta = False
        self.disdetta = False
        self.conclusa = False

        self.id_referto = 0
        self.id_ricevuta = 0
        self.id_mora = 0


#Inserimnento di una nuova prenotazione nel file Prenotazioni.pickle
    def aggiungiPrenotazione(self, id, data, ora, id_medico, id_visita, cf_paziente):
        self.id = id
        self.data = data
        self.ora = ora
        self.id_medico = id_medico
        self.id_visita = id_visita

        # controllo CF paziente
        pazienti = []
        # Apertura e scrittura su file delle prenotazioni
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                pazienti.extend(current.values())

        for paziente in pazienti:
            if paziente.CF == cf_paziente:
                self.cf_paziente = cf_paziente

        if self.cf_paziente != "":
            visite = []
            # Apertura e scrittura su file delle prenotazioni
            if os.path.isfile('File/Visite.pickle'):
                with open('File/Visite.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    visite.extend(current.values())

            #salvo l'id del reparto relativo alla visita
            for visita in visite:
                if visita.id == self.id_visita:
                    id_reparto_visita = visita.id_reparto


            prenotazioni = {}

            # Apertura e scrittura su file delle prenotazioni
            if os.path.isfile('File/Prenotazioni.pickle'):
                with open('File/Prenotazioni.pickle', 'rb') as f:
                    prenotazioni = pickle.load(f)
            prenotazioni[id] = self
            with open('File/Prenotazioni.pickle', 'wb') as f:
                pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)


        else:
            return False

    # Ritorna un dizionario con le informazioni di Prenotazione
    def getInfoPrenotazione(self):
        return {
            "id": self.id,
            "data": self.data,
            "ora": self.ora,
            "scaduta": self.scaduta,
            "disdetta": self.disdetta,
            "conclusa": self.conclusa,
            "id_medico": self.id_medico,
            "id_visita": self.id_visita,
            "cf_paziente": self.cf_paziente
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

#Disdetta di una prenotazione effettuata in precedenza
    def disdiciPrenotazione(self):
        if not self.disdetta:
            self.disdetta = True
            prenotazioni = {}
            # Apertura e scrittura su file della prenotazione
            if os.path.isfile('File/Prenotazioni.pickle'):
                with open('File/Prenotazioni.pickle', 'rb') as f:
                    prenotazioni = pickle.load(f)
            prenotazioni[self.id] = self
            with open('File/Prenotazioni.pickle', 'wb') as f:
                pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
            return True
        else:
            return False

#Funzione per la gestione delle scadenze delle prenotazioni secondo la data
    def scadenzaPrenotazione(self):
        if not self.scaduta:
            scadenza = datetime.datetime.today()
            scadenza = scadenza.replace(day=scadenza.day - 1)
            if self.data < scadenza:
                self.scaduta = True
                prenotazioni = {}
                # Apertura e scrittura su file delle prenotazioni
                if os.path.isfile('File/Prenotazioni.pickle'):
                    with open('File/Prenotazioni.pickle', 'rb') as f:
                        prenotazioni = pickle.load(f)
                prenotazioni[self.id] = self
                with open('File/Prenotazioni.pickle', 'wb') as f:
                    pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
                    return True
        else:
            return False
