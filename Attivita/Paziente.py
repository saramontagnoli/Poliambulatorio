"""
    Classe di modellazione per il Paziente (derivata da Utilizzatore classe padre)
    Rappresenta l'utente Paziente all'interno della piattaforma
"""

from Attivita.Utilizzatore import Utilizzatore
from Gestione.GestoreFile import scriviFile, ricercaElemFile, rimuoviElemFile


class Paziente(Utilizzatore):

    """
        Costruttore della classe
        Richiamo la classe padre con super, set degli attributi della classe figlia
    """
    def __init__(self):
        # richiamo classe padre
        super().__init__()
        self.allergia = False
        self.malattia_pregressa = False

    """
        Metodo che permette l'inserimento o modifica delle informazioni di un nuovo Paziente.
        Scrittura su file delle informazioni.
        Essendo Paziente una classe derivata, si richiama il metodo di set dalla classe padre, mentre
        le informazioni contenute solo in Paziente vengono inserite tramite il self.
    """
    def setInfoPaziente(self, id, nome, cognome, password, data_nascita, CF, telefono, genere, mail, indirizzo, nota,
                        allergia, malattia_pregressa):

        # chiamata al metodo set della classe padre (Utilizzatore)
        self.setInfoUtilizzatore(id, password, cognome, nome, data_nascita, CF, telefono, genere, mail, indirizzo,
                                 nota)
        self.allergia = allergia
        self.malattia_pregressa = malattia_pregressa

        # chiamata a GestoreFile per salvataggio su file delle informazioni del Paziente
        scriviFile("Pazienti", self)


    """
        Metodo che ritorna tutte le informazioni registrate di Paziente.
        Essendo Paziemte una classe derivata, si richiama il metodo di get dalla classe padre, mentre
        le informazioni contenute solo in Paziente vengono posizionata nel dizionario tramite il self.
        Si ritorna il dizionario "info" con dentro le informazioni complete di Paziente.
    """
    def getInfoPaziente(self):
        # chiamata al metodo get della classe padre
        info = self.getInfoUtilizzatore()

        info["allergia"] = self.allergia
        info["malattia_pregressa"] = self.malattia_pregressa
        return info


    """
        Metodo per la ricerca di un determinato Paziente sulla base del Codice Fiscale.
        Si richiama il metodo di ricerca dal GestoreFile che permette l'apertura 
        e lo scorrimento del file contennte i Pazienti.
    """
    def ricercaUtilizzatoreCF(self, CF):
        return ricercaElemFile("Pazienti", CF)


    """
        Metodo per la ricerca di un determinato Paziente sulla base dell'ID.
        Si richiama il metodo di ricerca dal GestoreFile che permette l'apertura 
        e lo scorrimento del file contennte i Pazienti.
    """
    def ricercaUtilizzatoreId(self, id):
        return ricercaElemFile("Pazienti", id)


    """
        Metodo per la rimozione di un determinato Paziente sulla base dell'ID.
        Si richiama il metodo di rimozione dal GestoreFile che permette l'apertura 
        e lo scorrimento del file rimuovendo il Paziente in questione.
        Elimino anche il Paziente dal self
    """
    def rimuoviPaziente(self):
        # chiamata a GestoreFile per la rimozione del paziente dal file
        rimuoviElemFile("Pazienti", self)

        # rimozione Paziente da self
        self.rimuoviUtilizzatore()
        self.allergia = False
        self.malattia_pregressa = False
        del self




    # CANCELLARE I SET E GET
    # CANCELLARE I SET E GET
    # CANCELLARE I SET E GET
    def isAllergia(self):
        return self.allergia

    def isMalattia_pregressa(self):
        return self.malattia_pregressa

    def setMalattia_pregressa(self, malattia_pregressa):
        self.malattia_pregressa = malattia_pregressa

    def setAllergia(self, allergia):
        self.allergia = allergia
