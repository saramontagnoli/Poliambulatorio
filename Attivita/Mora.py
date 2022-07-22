"""
    Classe di modellazione per la Mora
    Rappresenta la penale da pagare nei casi in cui:
        - il paziente non si è presentato alla visita (la visita è scaduta)
        - il paziente non ha disdetto nel tempo limite la visita (5 gg precedenti)
"""
import datetime

from Gestione.GestoreFile import scriviFile


class Mora:
    """
        Costruttore della classe
        Set degli attributi della Mora (la data viene salvata in base al giorno di caricamento della mora).
        Salvataggio su file dei dati.
    """

    def __init__(self, id, importo, nota):
        self.id = id
        self.importo = importo / 3.0
        self.nota = nota
        self.data_emissione = datetime.datetime.today()

        # chiamata al GestoreFile per il salvataggio della Mora
        scriviFile("More", self)
