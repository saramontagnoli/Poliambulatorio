import datetime
import os
import pickle


class GestoreBackUp:

    # Impostazioni standard di Back-up
    def __init__(self):
        impostazioni = []
        # Caricamento delle impostazioni di back-up salvate in precedenza
        if os.path.isfile('File/Backup.pickle'):
            with open('File/Backup.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                impostazioni.extend(current.values())

            self.ora = impostazioni[0].ora
            self.frequenza = impostazioni[0].frequenza

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
        self.ora = ora
        self.frequenza = frequenza

        impostazioni = {}
        if os.path.isfile('File/Backup.pickle'):
            with open('File/Backup.pickle', 'rb') as f:
                impostazioni = pickle.load(f)
        impostazioni[0] = self
        with open('File/Backup.pickle', 'wb') as f:
            pickle.dump(impostazioni, f, pickle.HIGHEST_PROTOCOL)

        return
