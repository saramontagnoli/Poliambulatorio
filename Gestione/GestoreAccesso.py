"""
    Classe che implementa la gestione degli accessi alla piattaforma
    Rappresenta la gestione della form di login, smistando i vari livelli di accesso e i diversi utenti (pazienti e medici)
    e il super utente (l'amministratore)
"""

from Gestione.GestoreFile import caricaFile
from Viste.VistaHomeAmm import VistaHomeAmm
from Viste.VistaHomeMedico import VistaHomeMedico
from Viste.VistaHomePaziente import VistaHomePaziente


class GestoreAccesso:

    """
        Costruttore della classe
        Definisco la vista home a None
    """
    def __init__(self):
        self.vista_home = None


    """
        Metodo che permette la gestione del login alla piattaforma del poliambulatorio.
        Controllo:
            - se sta accedendo l'amministratore (admin)
            - se sta accedendo un paziente (CF del paziente)
            - se sta accedendo un medico (CF del medico)
        In base all'utente che accede alla piattaforma (se i dati sono corretti) si apre la relativa vista dell'area privata 
        con tutte le funzionalità da poter svolgere
    """
    def login(self, username, password):

        # controllo se è l'admin a voler accedere (super utente)
        if username == "admin" and password == "admin":
            # apro la vista dell'admin
            self.vista_home = VistaHomeAmm()
            self.vista_home.show()
            return True

        # controllo se è un medico a voler accedere
        medici = caricaFile("Medici")
        for medico in medici:
            if medico.CF == username and medico.password == password:
                # apro la vista del medico
                self.vista_home = VistaHomeMedico(medico)
                self.vista_home.show()
                return True

        # controllo se è un paziente a voler accedere
        pazienti = caricaFile("Pazienti")
        for paziente in pazienti:
            if paziente.CF == username and paziente.password == password:
                # apro la vista del paziente
                self.vista_home = VistaHomePaziente(paziente)
                VistaHomePaziente.paziente = paziente
                self.vista_home.show()
                return True

        return False
