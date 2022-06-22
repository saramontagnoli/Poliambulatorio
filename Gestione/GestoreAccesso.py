from Viste.VistaHomeAmm import VistaHomeAmm

class GestoreAccesso:
    def __init__(self):
        self.vista_home = None

    def login(self, username, password):
        if username == "admin" and password == "admin":
            print("Admin Apertura")
            self.vista_home = VistaHomeAmm()
            self.vista_home.show()



    def logout(self):
        return
