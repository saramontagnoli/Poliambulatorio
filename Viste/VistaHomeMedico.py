from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from Viste.VistaGestisciPrenMedico import VistaGestisciPrenMedico
from Viste.VistaModificaMedico import VistaModificaMedico
import cv2

class VistaHomeMedico(QWidget):

    def __init__(self, medico, parent=None):
        super(VistaHomeMedico, self).__init__(parent)
        self.medico = medico
        self.setWindowIcon(QIcon('CroceVerde.png'))
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Vedi Prenotazioni", self.go_prenotazioni), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Vedi Turni", self.go_turni), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Modifica Informazioni", self.go_informazioni), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Visualizza Informazioni", self.go_vis_info), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Logout", self.go_logout), 2, 0, 1, 2)
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
        img = cv2.imread('Turni.png')
        cv2.imshow('Turni.png', img)

    def go_informazioni(self):
        self.vista_modifica_medico = VistaModificaMedico(self.medico)
        self.vista_modifica_medico.show()

    def go_logout(self):
        pass

    def go_vis_info(self):
        messaggio = QMessageBox()
        messaggio.setWindowIcon(QIcon('CroceVerde.png'))
        messaggio.setWindowTitle("Profilo")
        messaggio.setText(f"Id: {self.medico.id} \nNome: {self.medico.nome}€ \nCognome: {self.medico.cognome} \nCF: {self.medico.CF} \nData nascita: {self.medico.data_nascita} \nGenere: {self.medico.genere} \nIndirizzo: {self.medico.indirizzo}\nMail: {self.medico.mail} \nTelefono: {self.medico.telefono} \nReparto: {self.medico.id_reparto} \nAbilitazione: {self.medico.abilitazione} \nNota: {self.medico.nota}" )
        messaggio.setText()
        messaggio.exec_()
        return
