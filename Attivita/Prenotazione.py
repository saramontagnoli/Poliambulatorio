import datetime

from Attivita.Mora import Mora
from Attivita.Ricevuta import Ricevuta
from Gestione.GestoreFile import scriviFile, caricaFile, ricercaFile


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

        pazienti = caricaFile("Pazienti")

        for paziente in pazienti:
            if paziente.CF == cf_paziente:
                self.cf_paziente = cf_paziente

        if self.cf_paziente != "":

            visite = caricaFile("Visite")

            # salvo l'id del reparto relativo alla visita
            id_reparto_visita = 0
            for visita in visite:
                if visita.id == self.id_visita:
                    id_reparto_visita = visita.id_reparto

            medici = caricaFile("Medici")

            # salvo l'id del reparto relativo alla visita
            id_reparto_medico = -1
            for medico in medici:
                if medico.id == self.id_medico:
                    id_reparto_medico = medico.id_reparto

            if id_reparto_visita == id_reparto_medico:
                for medico in medici:
                    if self.id_medico == medico.id:

                        prenotazioni = caricaFile("Prenotazioni")

                        c = 0
                        for paziente in pazienti:
                            if paziente.CF == self.cf_paziente:
                                for prenotazione in prenotazioni:
                                    if prenotazione.cf_paziente == self.cf_paziente:
                                        if not prenotazione.disdetta and not prenotazione.scaduta and not prenotazione.conclusa:
                                            c += 1
                                        if c >= 5:
                                            return -5
                                        if prenotazione.ora == self.ora and prenotazione.data == self.data and not prenotazione.disdetta:
                                            return -4

                        for prenotazione in prenotazioni:
                            if prenotazione.id_medico == self.id_medico and not prenotazione.disdetta:
                                if prenotazione.data == self.data and prenotazione.ora == self.ora:
                                    return -2

                scriviFile("Prenotazioni", self)

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
        return ricercaFile("Prenotazioni", id)

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
    def disdiciPrenotazione(self, num):
        costo = 0
        if not self.disdetta and not self.conclusa:
            sottrazione_data = self.data - datetime.datetime.today()
            if sottrazione_data.days < 5:

                visite = caricaFile("Visite")

                for visita in visite:
                    if self.id_visita == visita.id:
                        costo = visita.costo

                # Controllo sul chi disdice la prenotazione (paziente = paga, amm/med = no)
                if num == 1:
                    Mora(self.id, costo, "Non disdetta in tempo. ")
                else:
                    Mora(self.id, 0, "Prenotazione disdetta dal medico o dall'amministratore. ")

            self.disdetta = True

            scriviFile("Prenotazioni", self)
            return True
        else:
            return False

    # Funzione per la gestione delle scadenze delle prenotazioni secondo la data
    def scadenzaPrenotazione(self):
        costo = 0
        if not self.scaduta and not self.conclusa:
            scadenza = datetime.datetime.today()
            scadenza = scadenza.replace(day=scadenza.day - 1)
            if self.data < scadenza:
                self.scaduta = True

                visite = caricaFile("Visite")

                for visita in visite:
                    if self.id_visita == visita.id:
                        costo = visita.costo

                Mora(self.id, costo, "Prenotazione scaduta. ")

                scriviFile("Prenotazioni", self)
                return True
        else:
            return False

    def crea_ricevuta(self):
        costo = 0
        if not self.disdetta and not self.scaduta and not self.conclusa:
            visite = caricaFile("Visite")

            for visita in visite:
                if self.id_visita == visita.id:
                    costo = visita.costo

            Ricevuta(self.id, costo)
            self.conclusa = True

            scriviFile("Prenotazioni", self)
            return True
        else:
            return False
