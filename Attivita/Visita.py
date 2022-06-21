import datetime
import os
import pickle

class Visita:

    #metodi set e get dei vari attributi
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return self.nota;

    #metodo per stampare i dati di una visita
    def visualizza(self):
        return
