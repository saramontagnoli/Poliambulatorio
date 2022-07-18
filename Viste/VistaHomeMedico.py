from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from Viste.VistaGestisciPrenMedico import VistaGestisciPrenMedico

class VistaHomeMedico(QWidget):

    def __init__(self, medico, parent=None):
        super(VistaHomeMedico, self).__init__(parent)
        self.medico = medico
        self.setWindowIcon(QIcon('CroceVerde.png'))
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Vedi Prenotazioni", self.go_prenotazioni), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Vedi Turni", self.go_turni), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Modifica Informazioni", self.go_informazioni), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Logout", self.go_logout), 1, 1)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle(f"Dot. {self.medico.nome} {self.medico.cognome} - {self.medico.id}")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_prenotazioni(self):
        self.vista_gestisci_pren_medico = VistaGestisciPrenMedico(self.medico)
        self.vista_gestisci_pren_medico.show()

    def go_turni(self):
        pass

    def go_informazioni(self):
        pass

    def go_logout(self):
        pass
