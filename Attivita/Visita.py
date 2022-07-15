import datetime
import os
import pickle

class Visita:

    def __init__(self, id, nome, nota, id_reparto):
        self.id = id
        self.nome = nome
        self.nota = nota
        self.id_reparto = id_reparto

        visite ={}
        if os.path.isfile('File/Visite.pickle'):
            with open('File/Visite.pickle', 'rb') as f:
                visite = pickle.load(f)
        visite[self.id] = self
        with open('File/Visite.pickle', 'wb') as f:
            pickle.dump(visite, f, pickle.HIGHEST_PROTOCOL)

    #metodi set e get dei vari attributi
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return self.nota

    #metodo per stampare i dati di una visita
    def visualizza(self):
        return
