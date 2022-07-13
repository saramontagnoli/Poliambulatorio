import os
import pickle

from Viste.VistaHomeAmm import VistaHomeAmm
from Viste.VistaHomeMedico import VistaHomeMedico
from Viste.VistaHomePaziente import VistaHomePaziente


class GestoreAccesso:
    def __init__(self):
        self.vista_home = None

    #Gestione dei livelli di accesso degli utenti della piattaforma
    def login(self, username, password):
        trovato = 0
        #Controllo se l'utente che vuole accedere è l'admin (superutente)
        if username == "admin" and password == "admin":
            trovato = 1
            self.vista_home = VistaHomeAmm()
            self.vista_home.show()
        else:
            self.medici = []
            if os.path.isfile('File/Medici.pickle'):
                with open('File/Medici.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    self.medici.extend(current.values())
            for medico in self.medici:
                if(medico.CF == username and medico.password == password):
                    trovato = 1
                    self.vista_home = VistaHomeMedico(medico)
                    self.vista_home.show()
        if trovato == 0:
            self.pazienti = []
            if os.path.isfile('File/Pazienti.pickle'):
                with open('File/Pazienti.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    self.pazienti.extend(current.values())
            for paziente in self.pazienti:
                trovato = 1
                #print(paziente.CF)
                if(paziente.CF == username and paziente.password == password):
                    self.vista_home = VistaHomePaziente(paziente)
                    VistaHomePaziente.paziente = paziente
                    self.vista_home.show()



    def logout(self):
        return
