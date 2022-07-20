from Gestione.GestoreFile import scriviFile


class Reparto:

    # costruttore
    def __init__(self, id, nome, nota):
        self.id = id
        self.nome = nome
        self.nota = nota

        scriviFile("Reparti", self)

    # metodi set e get dei vari attributi
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return self.nota
