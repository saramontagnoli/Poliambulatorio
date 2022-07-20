import os.path
import pickle

from Attivita.Utilizzatore import Utilizzatore
from Gestione.GestoreFile import scriviFile, ricercaElemFile, rimuoviElemFile


class Paziente(Utilizzatore):

    # Costruttore della classe Paziente
    def __init__(self):
        super().__init__()
        self.allergia = False
        self.malattia_pregressa = False

    # Set delle informazioni del paziente (richiamo la superclasse che è Utilizzatore)
    def setInfoPaziente(self, id, nome, cognome, password, data_nascita, CF, telefono, genere, mail, indirizzo, nota,
                        allergia, malattia_pregressa):

        self.setInfoUtilizzatore(id, password, cognome, nome, data_nascita, CF, telefono, genere, mail, indirizzo,
                                 nota)
        self.allergia = allergia
        self.malattia_pregressa = malattia_pregressa

        scriviFile("Pazienti", self)

    # Ritorna un dizionario con le informazioni di Paziente
    def getInfoPaziente(self):
        info = self.getInfoUtilizzatore()
        info["allergia"] = self.allergia
        info["malattia_pregressa"] = self.malattia_pregressa
        return info

    # Ricerca paziente per codice fiscale
    def ricercaUtilizzatoreCF(self, CF):
        return ricercaElemFile("Pazienti", CF)

    # Ricerca paziente per id
    def ricercaUtilizzatoreId(self, id):
        return ricercaElemFile("Pazienti", id)

    # Rimozione di un paziente mediante il suo id
    def rimuoviPaziente(self):
        rimuoviElemFile("Pazienti", self)
        self.rimuoviUtilizzatore()
        self.allergia = False
        self.malattia_pregressa = False
        del self

    # Metodi getter degli attributi contenuti in Paziente (non ereditati da Utilizzatore)
    def isAllergia(self):
        return self.allergia

    def isMalattia_pregressa(self):
        return self.malattia_pregressa

    # Metodi setter degli attributi contenuti in Paziente (non ereditati da Utilizzatore)
    def setMalattia_pregressa(self, malattia_pregressa):
        self.malattia_pregressa = malattia_pregressa

    def setAllergia(self, allergia):
        self.allergia = allergia
