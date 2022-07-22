"""
    Classe di modellazione per il Referto
    Rappresenta il documento rilasciato dal Medico dopo aver effettuato la visita al Paziente
"""

import datetime
from Gestione.GestoreFile import scriviFile


class Referto:

    """
        Costruttore della classe
        Set degli attributi di Referto secondo i parametri passati
        La data di emissione della mora è la data attuale (ovvero il momento in cui viene caricata)
        Scrittura su file delle informazioni del Referto creato
    """
    def __init__(self, id, nota):
        self.id = id
        self.nota = nota
        self.data_emissione = datetime.datetime.today()

        # scrittura su file del Referto, chiamata a GestoreFile
        scriviFile("Referti", self)
