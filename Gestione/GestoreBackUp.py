class GestoreBackUp:
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
        # boolean
        return
