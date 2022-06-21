import os.path
import pickle
from abc import ABC

from Attivita.Utilizzatore import Utilizzatore


class Medico(Utilizzatore, ABC):
    def __init__(self):
        super().__init__()
        self.abilitazione = ""

    def setInfoMedico(self, abilitazione, password, cognome, nome, data_nascita, CF, telefono, genere, mail, indirizzo,
                      nota):
        self.setInfoUtilizzatore(password=password, cognome=cognome, nome=nome, data_nascita=data_nascita, CF=CF,
                                 telefono=telefono, genere=genere, mail=mail, indirizzo=indirizzo, nota=nota)
        self.abilitazione = abilitazione

    def getInfoMedico(self):
        info = self.getInfoUtilizzatore()
        info["abilitazione"] = self.abilitazione +
        return info

