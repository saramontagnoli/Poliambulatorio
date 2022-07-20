import datetime
from Gestione.GestoreFile import scriviFile


class Referto:

    def __init__(self, id, nota):
        self.id = id
        self.nota = nota
        self.data_emissione = datetime.datetime.today()

        scriviFile("Referti", self)

    def getId(self):
        return self.id

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return self.nota
