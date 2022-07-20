from Gestione.GestoreFile import scriviFile


class Visita:

    def __init__(self, id, nome, nota, id_reparto, costo):
        self.id = id
        self.nome = nome
        self.nota = nota
        self.id_reparto = id_reparto
        self.costo = costo

        scriviFile("Visite", self)

    # metodi set e get dei vari attributi
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return self.nota

    def setCosto(self, costo):
        self.costo = costo

    def getCosto(self):
        return self.costo

    # metodo per stampare i dati di una visita
    def visualizza(self):
        return
