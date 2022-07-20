from Gestione.GestoreFile import caricaFile
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

        medici = caricaFile("Medici")
        for medico in medici:
            if medico.CF == username and medico.password == password:
                # trovato = 1
                self.vista_home = VistaHomeMedico(medico)
                self.vista_home.show()
                return True

        pazienti = caricaFile("Pazienti")
        for paziente in pazienti:
            if paziente.CF == username and paziente.password == password:
                self.vista_home = VistaHomePaziente(paziente)
                VistaHomePaziente.paziente = paziente
                self.vista_home.show()
                return True

        return False
