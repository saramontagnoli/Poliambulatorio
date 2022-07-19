from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from Viste.VistaGestisciPrenPaziente import VistaGestisciPrenPaziente
from Viste.VistaModificaPaziente import VistaModificaPaziente


class VistaHomePaziente(QWidget):

    #Vista che rappresenta la home del paziente con i relativi pulsanti
    def __init__(self, paziente, parent = None):
        super(VistaHomePaziente, self).__init__(parent)
        self.paziente = paziente
        self.setWindowIcon(QIcon('CroceVerde.png'))
        grid_layout = QGridLayout()
        print(self.paziente.CF)
        grid_layout.addWidget(self.get_generic_button("Vedi Prenotazioni",self.go_prenotazioni), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Modifica Informazioni", self.go_modifica), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Visualizza Informazioni", self.go_vis_info), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Logout", self.go), 1, 1)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle(f"{self.paziente.nome} {self.paziente.cognome} - {self.paziente.id}")

    #Funzione che crea i ulsanti presenti nella home
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_prenotazioni(self):
        self.vista_gestisci_pren_paziente = VistaGestisciPrenPaziente(self.paziente)
        self.vista_gestisci_pren_paziente.show()

    def go_modifica(self):
        self.vista_modifica_paziente = VistaModificaPaziente(self.paziente)
        self.vista_modifica_paziente.show()

    def go(self):
        pass

    def go_vis_info(self):
        messaggio = QMessageBox()
        messaggio.setWindowIcon(QIcon('CroceVerde.png'))
        messaggio.setWindowTitle("Profilo")
        messaggio.setText(f"Id: {self.paziente.id} \nNome: {self.paziente.nome} \nCognome: {self.paziente.cognome} \nCF: {self.paziente.CF} \nData nascita: {self.paziente.data_nascita.strftime('%Y-%m-%d')} \nGenere: {self.paziente.genere} \nIndirizzo: {self.paziente.indirizzo}\nMail: {self.paziente.mail} \nTelefono: {self.paziente.telefono} \nNota: {self.medico.nota} \nAllergia: {self.paziente.allergia} \nMalattia pregressa: {self.paziente.malattia_pregressa}" )
        messaggio.exec_()
        return




