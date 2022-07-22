"""
    Classe di modellazione per il Medico (derivata da Utilizzatore classe padre)
    Rappresenta l'utente Medico all'interno della piattaforma
"""

from Attivita.Utilizzatore import Utilizzatore
from Gestione.GestoreFile import scriviFile, ricercaElemFile, rimuoviElemFile


class Medico(Utilizzatore):

    """
        Costruttore della classe
        Richiamo la classe padre con super, set degli attributi della classe figlia
    """
    def __init__(self):
        # richiamo classe padre
        super().__init__()
        self.abilitazione = ""
        self.id_reparto = 0


    """
        Metodo che permette l'inserimento o modifica delle informazioni di un nuovo Medico.
        Scrittura su file delle informazioni.
        Essendo Medico una classe derivata, si richiama il metodo di set dalla classe padre, mentre
        le informazioni contenute solo in Medico vengono inserite tramite il self.
    """
    def setInfoMedico(self, id, password, cognome, nome, data_nascita, CF, telefono, genere, mail, indirizzo, nota,
                      abilitazione, id_reparto):
        # chiamata al metodo set della classe padre (Utilizzatore)
        self.setInfoUtilizzatore(id, password, cognome, nome, data_nascita, CF,
                                 telefono, genere, mail, indirizzo, nota)
        self.abilitazione = abilitazione
        self.id_reparto = id_reparto

        # chiamata al GestoreFile per la scrittura delle modifiche sul file
        scriviFile("Medici", self)


    """
        Metodo che ritorna tutte le informazioni registrate di Medico.
        Essendo Medico una classe derivata, si richiama il metodo di get dalla classe padre, mentre
        le informazioni contenute solo in Medico vengono posizionata nel dizionario tramite il self.
        Si ritorna il dizionario "info" con dentro le informazioni complete.
    """
    def getInfoMedico(self):
        # chiamata al metodo get della classe padre
        info = self.getInfoUtilizzatore()

        info["abilitazione"] = self.abilitazione
        info["reparto"] = self.id_reparto
        return info


    """
        Metodo per la ricerca di un determinato Medico sulla base del Codice Fiscale.
        Si richiama il metodo di ricerca dal GestoreFile che permette l'apertura 
        e lo scorrimento del file contennte i Medici.
    """
    def ricercaUtilizzatoreCF(self, CF):
        return ricercaElemFile("Medici", CF)


    """
        Metodo per la ricerca di un determinato Medico sulla base dell'ID.
        Si richiama il metodo di ricerca dal GestoreFile che permette l'apertura 
        e lo scorrimento del file contennte i Medici.
    """
    def ricercaUtilizzatoreId(self, id):
        return ricercaElemFile("Medici", id)


    """
        Metodo per la rimozione di un determinato Medico sulla base dell'ID.
        Si richiama il metodo di rimozione dal GestoreFile che permette l'apertura 
        e lo scorrimento del file rimuovendo il Medico in questione.
        Elimino anche il Medico dal self
    """
    def rimuoviMedico(self):
        # chiamata a GestoreFile per la rimozione del medico dal file
        rimuoviElemFile("Medici", self)

        # rimozione Medico da self
        self.rimuoviUtilizzatore()
        self.abilitazione = ""
        del self
