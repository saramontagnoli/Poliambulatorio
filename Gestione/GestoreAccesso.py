from Viste.VistaHomeAmm import VistaHomeAmm

class GestoreAccesso:
    def __init__(self):
        self.vista_home = None

    #Gestione dei livelli di accesso degli utenti della piattaforma
    def login(self, username, password):
        #Controllo se l'utente che vuole accedere è l'admin (superutente)
        if username == "admin" and password == "admin":
            self.vista_home = VistaHomeAmm()
            self.vista_home.show()


    def logout(self):
        return
