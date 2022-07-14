import os.path
import pickle

from Attivita.Utilizzatore import Utilizzatore


class Paziente(Utilizzatore):

    # Costruttore della classe Paziente
    def __init__(self):
        super().__init__()
        self.prenotazioni = []
        self.allergia = False
        self.malattia_pregressa = False

    # Set delle informazioni del paziente (richiamo la superclasse che è Utilizzatore)
    def setInfoPaziente(self, id, nome, cognome, password, data_nascita, CF, telefono, genere, mail, indirizzo, nota,
                        allergia, malattia_pregressa):

        self.setInfoUtilizzatore(id, password, cognome, nome, data_nascita, CF, telefono, genere, mail, indirizzo,
                                 nota)
        self.allergia = allergia
        self.malattia_pregressa = malattia_pregressa
        pazienti = {}

        # Load del file Pazienti sul dizionario pazienti
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)
        pazienti[id] = self
        with open('File/Pazienti.pickle', 'wb') as f:
            pickle.dump(pazienti, f, pickle.HIGHEST_PROTOCOL)

    # Ritorna un dizionario con le informazioni di Paziente
    def getInfoPaziente(self):
        info = self.getInfoUtilizzatore()
        info["prenotazioni"] = self.prenotazioni
        info["allergia"] = self.allergia
        info["malattia_pregressa"] = self.malattia_pregressa
        return info

    # Ricerca paziente per codice fiscale
    def ricercaUtilizzatoreCF(self, CF):
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = dict(pickle.load(f))
                return pazienti.get(CF, None)
        else:
            return None

    # Ricerca paziente per id
    def ricercaUtilizzatoreId(self, id):
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = dict(pickle.load(f))
                return pazienti.get(id, None)

        else:
            return None

    # Rimozione di un paziente mediante il suo id
    def rimuoviPaziente(self):
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = dict(pickle.load(f))
                del pazienti[self.id]
            with open('File/Pazienti.pickle', 'wb') as f:
                pickle.dump(pazienti, f, pickle.HIGHEST_PROTOCOL)
        self.rimuoviUtilizzatore()
        self.prenotazioni = []
        self.allergia = False
        self.malattia_pregressa = False
        del self

    # Metodi getter degli attributi contenuti in Paziente (non ereditati da Utilizzatore)
    def isAllergia(self):
        return self.allergia

    def isMalattia_pregressa(self):
        return self.malattia_pregressa

    # Metodi setter degli attributi contenuti in Paziente (non ereditati da Utilizzatore)
    def setMalattia_pregressa(self, malattia_pregressa):
        self.malattia_pregressa = malattia_pregressa

    def setAllergia(self, allergia):
        self.allergia = allergia

    # Modifica di un paziente
    def modificaPaziente(self, password, telefono, mail, indirizzo, nota, malattia_pregressa, allergia):
        self.modificaUtilizzatore(password, telefono, mail, indirizzo, nota)
        self.malattia_pregressa = malattia_pregressa
        self.allergia = allergia
