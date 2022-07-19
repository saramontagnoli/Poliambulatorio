import datetime
import os
import pickle


class Referto:

    def __init__(self, id, nota):
        self.id = id
        self.nota = nota
        self.data_emissione = datetime.datetime.today()

        referti = {}
        if os.path.isfile('File/Referti.pickle'):
            with open('File/Referti.pickle', 'rb') as f:
                referti = pickle.load(f)
        referti[self.id] = self
        with open('File/Referti.pickle', 'wb') as f:
            pickle.dump(referti, f, pickle.HIGHEST_PROTOCOL)

    def getId(self):
        return self.id

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return self.nota
