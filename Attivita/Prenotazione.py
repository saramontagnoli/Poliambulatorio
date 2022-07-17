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

    def aggiungiPrenotazione(self, id, data, ora, id_medico, id_visita, cf_paziente):
        self.id = id
        self.ora = ora
        self.id_medico = id_medico
        self.id_visita = id_visita

        if data.isoweekday() > 5:
            return -3

        self.data = data

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

            # salvo l'id del reparto relativo alla visita
            id_reparto_visita = 0
            for visita in visite:
                if visita.id == self.id_visita:
                    id_reparto_visita = visita.id_reparto

            medici = []
            # Apertura e scrittura su file delle prenotazioni
            if os.path.isfile('File/Medici.pickle'):
                with open('File/Medici.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    medici.extend(current.values())

            # salvo l'id del reparto relativo alla visita
            id_reparto_medico = -1
            for medico in medici:
                if medico.id == self.id_medico:
                    id_reparto_medico = medico.id_reparto

            if id_reparto_visita == id_reparto_medico:
                for medico in medici:
                    if self.id_medico == medico.id:
                        prenotazioni = []

                        if os.path.isfile('File/Prenotazioni.pickle'):
                            with open('File/Prenotazioni.pickle', 'rb') as f:
                                current = dict(pickle.load(f))
                                prenotazioni.extend(current.values())

                        c=0
                        for paziente in pazienti:
                            if paziente.CF == self.cf_paziente:
                                for prenotazione in prenotazioni:
                                    if prenotazione.cf_paziente == self.cf_paziente:
                                        if not prenotazione.disdetta and not prenotazione.scaduta and not prenotazione.conclusa:
                                            c+=1
                                        if c>=5:
                                            return -5
                                        if prenotazione.ora == self.ora and prenotazione.data == self.data and not prenotazione.disdetta:
                                            return -4

                        for prenotazione in prenotazioni:
                            if prenotazione.id_medico == self.id_medico and not prenotazione.disdetta:
                                if prenotazione.data == self.data and prenotazione.ora == self.ora:
                                    return -2
                prenotazioni = {}

                # Apertura e scrittura su file delle prenotazioni
                if os.path.isfile('File/Prenotazioni.pickle'):
                    with open('File/Prenotazioni.pickle', 'rb') as f:
                        prenotazioni = pickle.load(f)

                prenotazioni[id] = self
                with open('File/Prenotazioni.pickle', 'wb') as f:
                    pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
            else:
                return -1
        else:
            return 0

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

    # Disdetta di una prenotazione effettuata in precedenza
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

    # Funzione per la gestione delle scadenze delle prenotazioni secondo la data
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
