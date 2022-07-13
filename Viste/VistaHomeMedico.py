from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

class VistaHomeMedico(QWidget):

    def __init__(self, medico, parent=None):
        self.medico = medico
        super(VistaHomeMedico, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Vedi Prenotazioni", self.go_prenotazioni), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Vedi Turni", self.go_turni), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Modifica Informazioni", self.go_informazioni), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Logout", self.go_logout), 1, 1)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        # vedere come mettere il nome del medico che ha fatto l'accesso
        self.setWindowTitle(f"{self.medico.nome} {self.medico.cognome} - {self.medico.id}")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_prenotazioni(self):
        pass

    def go_turni(self):
        pass

    def go_informazioni(self):
        pass

    def go_logout(self):
        pass
