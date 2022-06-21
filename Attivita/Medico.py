import os.path
import pickle


from Attivita.Utilizzatore import Utilizzatore


class Medico(Utilizzatore):

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
        info["abilitazione"] = self.abilitazione
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

    def modificaUtilizzatore(self):
        pass

    def rimuoviMedico(self):
        if os.path.isfile('Dati/Medici.pickle'):
            with open('Dati/Medici.pickle', 'wb+') as f:
                medici = dict(pickle.load(f))
                del medici[self.id]
                pickle.dump(medici, f, pickle.HIGHEST_PROTOCOL)
        self.rimuoviUtilizzatore()
        self.abilitazione = ""
        del self


