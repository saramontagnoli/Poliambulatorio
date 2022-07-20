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




    # CANCELLARE I SET E GET
    # CANCELLARE I SET E GET
    # CANCELLARE I SET E GET
    def getCognome(self):
        return self.cognome


    def getId(self):
        return self.id


    def getNome(self):
        return self.nome


    def getData_nascita(self):
        return self.data_nascita


    def getCF(self):
        return self.CF


    def getTelefono(self):
        return self.telefono


    def getGenere(self):
        return self.genere


    def getMail(self):
        return self.mail


    def getIndirizzo(self):
        return self.indirizzo


    def getNota(self):
        return self.nota


    def getPassword(self):
        return self.password


    def setCognome(self, cognome):
        self.cognome = cognome


    def setNome(self, nome):
        self.nome = nome


    def setData_nascita(self, data_nascita):
        self.data_nascita = data_nascita


    def setCF(self, CF):
        self.CF = CF


    def setTelefono(self, telefono):
        self.telefono = telefono


    def setGenere(self, genere):
        self.genere = genere


    def setMail(self, mail):
        self.mail = mail


    def setIndirizzo(self, indirizzo):
        self.indirizzo = indirizzo


    def setNota(self, nota):
        self.nota = nota


    def setPassword(self, password):
        self.password = password
