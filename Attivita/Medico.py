import os.path
import pickle

from Attivita.Utilizzatore import Utilizzatore


class Medico(Utilizzatore):

    def __init__(self):
        super().__init__()
        self.abilitazione = ""
        self.id_reparto = 0

    def setInfoMedico(self, id, password, cognome, nome, data_nascita, CF, telefono, genere, mail, indirizzo, nota,
                      abilitazione, id_reparto):
        self.setInfoUtilizzatore(id, password, cognome, nome, data_nascita, CF,
                                 telefono, genere, mail, indirizzo, nota)
        self.abilitazione = abilitazione
        self.id_reparto = id_reparto

        medici = {}
        if os.path.isfile('File/Medici.pickle'):
            with open('File/Medici.pickle', 'rb') as f:
                medici = pickle.load(f)
        medici[id] = self
        with open('File/Medici.pickle', 'wb') as f:
            pickle.dump(medici, f, pickle.HIGHEST_PROTOCOL)

    def getInfoMedico(self):
        info = self.getInfoUtilizzatore()
        info["abilitazione"] = self.abilitazione
        info["reparto"] = self.id_reparto
        return info

    def ricercaUtilizzatoreCF(self, CF):
        if os.path.isfile('File/Medici.pickle'):
            with open('File/Medici.pickle', 'rb') as f:
                medici = dict(pickle.load(f))
                return medici.get(CF, None)
        else:
            return None

    def ricercaUtilizzatoreId(self, id):
        if os.path.isfile('File/Medici.pickle'):
            with open('File/Medici.pickle', 'rb') as f:
                medici = dict(pickle.load(f))
                return medici.get(id, None)
        else:
            return None

    def modificaMedico(self, password, telefono, mail, indirizzo, nota, abilitazione):
        self.modificaUtilizzatore(password, telefono, mail, indirizzo, nota)
        self.abilitazione = abilitazione

    # Rimozione di un medico mediante il suo id
    def rimuoviMedico(self):
        if os.path.isfile('File/Medici.pickle'):
            with open('File/Medici.pickle', 'rb') as f:
                medici = dict(pickle.load(f))
                del medici[self.id]
            with open('File/Medici.pickle', 'wb') as f:
                pickle.dump(medici, f, pickle.HIGHEST_PROTOCOL)
        self.rimuoviUtilizzatore()
        self.abilitazione = ""
        # self.allergia = False
        # self.malattia_pregressa = False
        del self

    def getAbilitazione(self):
        return self.abilitazione

    def setAbilitazione(self, abilitazione):
        self.abilitazione = abilitazione
