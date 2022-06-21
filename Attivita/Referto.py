import datetime
import os
import pickle

class Referto:
    def incrementaId(self):
        self.incrementaId.id += 1
        return self.incrementaId.id

    incrementaId.id = 0

    def __init__(self):
        self.id = self.incrementaId()
        self.nota = ""

    def getId(self):
        return self.id

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return self.nota





