import os.path
import pickle

from Attivita.Utilizzatore import Utilizzatore

class Paziente(Utilizzatore):

    def __init__(self):
        super().__init__()
        self.prenotazioni = []
        self.allergia = False
        self.malattia_pregressa = False

    def setInfoPaziente(self, nome, cognome, password, data_nascita, CF, telefono, genere, mail, indirizzo, nota, allergia, malattia_pregressa):
        self.setInfoUtilizzatore(nome, cognome, password, data_nascita, CF, telefono, genere, mail, indirizzo, nota)
        self.allergia = allergia
        self.malattia_pregressa = malattia_pregressa
        pazienti = {}
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)
        pazienti[id] = self
        with open('File/Pazienti.pickle', 'wb') as f:
            pickle.dump(pazienti, f, pickle.HIGHEST_PROTOCOL)
