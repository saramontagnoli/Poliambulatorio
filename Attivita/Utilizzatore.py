"""
    Classe di modellazione per l'Utilizzatore (classe padre di Medico e Paziente)
    La classe padre raggruppa al suo interno i metodi e attributi in comune tra Medico e Paziente
    (ereditarietà)
"""

import datetime
from abc import abstractmethod


class Utilizzatore:
    """
        Costruttore della classe
        Set degli attributi di Utilizzatore a null
    """

    def __init__(self):
        self.id = -1
        self.password = ""
        self.cognome = ""
        self.nome = ""
        self.data_nascita = datetime.datetime(1970, 1, 1)
        self.CF = ""
        self.telefono = ""
        self.genere = ""
        self.mail = ""
        self.indirizzo = ""
        self.nota = ""

    """
        Metodo che permette il set o modifica delle informazioni di un Utilizzatore.
        Una volta estesa la classe padre, le classi figlie avranno a disposizione gli attributi
    """

    def setInfoUtilizzatore(self, id, password, cognome, nome, data_nascita, CF, telefono, genere, mail, indirizzo,
                            nota):
        self.id = id
        self.password = password
        self.cognome = cognome
        self.nome = nome
        self.data_nascita = data_nascita
        self.CF = CF
        self.telefono = telefono
        self.genere = genere
        self.mail = mail
        self.indirizzo = indirizzo
        self.nota = nota

    """
        Metodo che ritorna tutte le informazioni dell'Utilizzatore.
        Si ritorna il dizionario seguente con tutte le info.
    """

    def getInfoUtilizzatore(self):
        return {
            "id": self.id,
            "cognome": self.cognome,
            "nome": self.nome,
            "data_nascita": self.data_nascita,
            "CF": self.CF,
            "telefono": self.telefono,
            "genere": self.genere,
            "mail": self.mail,
            "indirizzo": self.indirizzo,
            "nota": self.nota
        }

    """
        Metodi astratti per la ricerca degli Utilizzatori in base all'ID o al CF desiderato
    """

    @abstractmethod
    def ricercaUtilizzatoreCF(self, CF):
        pass

    @abstractmethod
    def ricercaUtilizzatoreId(self, id):
        pass

    """
        Metodo per la rimozione di un determinato Utilizzatore.
        Set di tutti i parametri di Utilizzatore a null
    """

    def rimuoviUtilizzatore(self):
        self.id = -1
        self.password = ""
        self.cognome = ""
        self.nome = ""
        self.data_nascita = datetime.datetime(1970, 1, 1)
        self.CF = ""
        self.telefono = 0
        self.genere = ""
        self.mail = ""
        self.indirizzo = ""
        self.nota = ""
