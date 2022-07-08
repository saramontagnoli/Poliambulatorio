from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from Attivita.Paziente import Paziente


class VistaHomePaziente(QWidget):

    #Vista che rappresenta la home del paziente con i relativi pulsanti
    def __init__(self, paziente, parent = None):
        self.paziente = paziente
        super(VistaHomePaziente, self).__init__(parent)
        grid_layout = QGridLayout()
        print(self.paziente.CF)
        grid_layout.addWidget(self.get_generic_button("Vedi Prenotazioni",self.go), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Modifica Informazioni", self.go), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Logout", self.go), 2, 0, 1, 2)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle(f"{self.paziente.nome} {self.paziente.cognome} - {self.paziente.id}")

    #Funzione che crea i ulsanti presenti nella home
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go(self):
        pass




