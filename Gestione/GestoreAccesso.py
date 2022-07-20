import os
import pickle

from Viste.VistaHomeAmm import VistaHomeAmm
from Viste.VistaHomeMedico import VistaHomeMedico
from Viste.VistaHomePaziente import VistaHomePaziente


class GestoreAccesso:
    def __init__(self):
        self.vista_home = None

    # Gestione dei livelli di accesso degli utenti della piattaforma
    def login(self, username, password):
        # Controllo se l'utente che vuole accedere è l'admin (superutente)
        if username == "admin" and password == "admin":
            self.vista_home = VistaHomeAmm()
            self.vista_home.show()
            return True

        medici = []
        if os.path.isfile('File/Medici.pickle'):
            with open('File/Medici.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                medici.extend(current.values())
        for medico in medici:
            if medico.CF == username and medico.password == password:
                # trovato = 1
                self.vista_home = VistaHomeMedico(medico)
                self.vista_home.show()
                return True

        pazienti = []
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                pazienti.extend(current.values())
        for paziente in pazienti:
            if paziente.CF == username and paziente.password == password:
                self.vista_home = VistaHomePaziente(paziente)
                VistaHomePaziente.paziente = paziente
                self.vista_home.show()
                return True

        return False

    def logout(self):
        return
