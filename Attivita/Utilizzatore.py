from datetime import datetime
from abc import abstractmethod


class Utilizzatore:

        def __init__(self):
            self.id = -1
            self.password = ""
            self.cognome = ""
            self.nome = ""
            self.data_nascita = datetime.date(1970, 1, 1)
            self.CF = ""
            self.telefono = 0
            self.genere = ""
            self.mail = ""
            self.indirizzo = ""
            self.nota = ""

        def aggiungiUtilizzatore(self, id, password, cognome, nome, data_nascita, CF, telefono, genere, mail, indirizzo,
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

        @abstractmethod
        def ricercaUtilizzatoreCF(self, CF):
            pass

        @abstractmethod
        def ricercaUtilizzatoreId(self, id):
            pass

        @abstractmethod
        def modificaUtilizzatore(self):
            pass

        def rimuoviUtilizzatore(self):
            self.id = -1
            self.password = ""
            self.cognome = ""
            self.nome = ""
            self.data_nascita = datetime.date(1970, 1, 1)
            self.CF = ""
            self.telefono = 0
            self.genere = ""
            self.mail = ""
            self.indirizzo = ""
            self.nota = ""
