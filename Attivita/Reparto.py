import datetime
import os
import pickle

class Reparto:

    #costruttore
    def __init__(self, id, nome, nota):
        self.id = id
        self.nome = nome
        self.nota = nota

        reparti ={}
        if os.path.isfile('File/Reparti.pickle'):
            with open('File/Reparti.pickle', 'rb') as f:
                reparti = pickle.load(f)
        reparti[self.id] = self
        with open('File/Reparti.pickle', 'wb') as f:
            pickle.dump(reparti, f, pickle.HIGHEST_PROTOCOL)


    #metodi set e get dei vari attributi
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return self.nota
