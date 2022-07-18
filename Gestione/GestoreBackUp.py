import datetime


class GestoreBackUp:

    # Impostazioni standard di Back-up
    def __init__(self):
        self.ora = datetime.time(21, 0, 0)
        self.frequenza = 1

    def copiaDatiMora(self):
        # boolean
        return

    def copiaDatiPrenotazione(self):
        # boolean
        return

    def copiaDatiReferto(self):
        # boolean
        return

    def copiaDatiRicevuta(self):
        # boolean
        return

    def copiaDatiUtilizzatore(self):
        # boolean
        return

    def effettuaBackUp(self):
        self.copiaDatiUtilizzatore()
        self.copiaDatiPrenotazione()
        self.copiaDatiReferto()
        self.copiaDatiRicevuta()
        self.copiaDatiMora()
        # void
        return

    # frequenza intesa come intervallo giornaliero (ogni n giorni)
    def modificaBackUp(self, ora, frequenza):
        print("In modifica (classe)")
        print(self.ora)
        print(self.frequenza)

        self.ora = ora
        self.frequenza = frequenza
        print(self.ora)
        print(self.frequenza)
        return
