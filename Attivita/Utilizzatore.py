import datetime
from abc import abstractmethod


class Utilizzatore:

    # Costruttore della classe Utilizzatore
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

    # Set delle informazioni dell'utilizzatore
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

    # Metodo che restituisce un dict con le informazioni di Utilizzatore
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

    # Metodi astratti per la ricerca dell'utilizzatore (per CF o ID)
    @abstractmethod
    def ricercaUtilizzatoreCF(self, CF):
        pass

    @abstractmethod
    def ricercaUtilizzatoreId(self, id):
        pass

    # Rimozione di un utilizzatore
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


# Metodi getter degli attributi di utilizzatore (ritornano le informazioni scelte)
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


# Metodi setter per gli attributi di utilizzatore
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
