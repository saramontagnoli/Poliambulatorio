"""
    Interfaccia grafica per la visualizzazione della home del medico
    Sono presenti 5 button che permettono di svolgere diverse funzioni:
        - controllare le prenotazioni a carico di questo medico
        - visualizzare il file dei turni di lavoro
        - modificare le informazioni del proprio profilo
        - visualizzare le informazioni del proprio profilo
        - eseguire il logout
"""

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QMessageBox
from Viste.VistaGestisciPrenMedico import VistaGestisciPrenMedico
from Viste.VistaModificaMedico import VistaModificaMedico
import cv2


class VistaHomeMedico(QWidget):
    """
        Costruttore della classe
        Si effettuano tutti i set di icone, size, titolo della finestra e visualizzazione
        Inserimento di 5 button che rimandano a:
            - vedi prenotazioni
            - vedi turni
            - modifica informazioni
            - visualizza informazioni
            - logout
        Ogni button ha l'evento click relativo che apre la vista per poter effettuare quella richiesta
    """
    def __init__(self, medico, parent=None):
        super(VistaHomeMedico, self).__init__(parent)
        self.medico = medico
        self.setWindowIcon(QIcon('CroceVerde.png'))
        grid_layout = QGridLayout()

        # button nella home del medico, ognuno con il suo evento click
        grid_layout.addWidget(self.get_generic_button("Vedi Prenotazioni", self.go_prenotazioni), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Vedi Turni", self.go_turni), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Modifica Informazioni", self.go_informazioni), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Visualizza Informazioni", self.go_vis_info), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Logout", self.go_logout), 2, 0, 1, 2)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle(f"Dot. {self.medico.nome} {self.medico.cognome} - {self.medico.id}")


    """
        Metodo che inserisce il button e collega l'evento on_click
    """
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button


    """
        Metodi per eventi del click ai button visualizzati nella home del medico
    """
    def go_prenotazioni(self):
        # apertura della vista di gestione delle prenotazioni del medico
        self.vista_gestisci_pren_medico = VistaGestisciPrenMedico(self.medico)
        self.vista_gestisci_pren_medico.show()

    def go_turni(self):
        # apertura dell'immagine dei turni di lavoro del medico
        img = cv2.imread('Turni.png')
        cv2.imshow('Turni.png', img)

    def go_informazioni(self):
        # apertura della vista di modifica delle informazioni del medico
        self.vista_modifica_medico = VistaModificaMedico(self.medico)
        self.vista_modifica_medico.show()

    def go_vis_info(self):
        # apertura pop up contenente le informazioni del medico
        messaggio = QMessageBox()
        messaggio.setWindowIcon(QIcon('CroceVerde.png'))
        messaggio.setWindowTitle("Profilo")
        messaggio.setText(
            f"Id: {self.medico.id} \nNome: {self.medico.nome} \nCognome: {self.medico.cognome} \nCF: {self.medico.CF} \nData nascita: {self.medico.data_nascita.strftime('%Y-%m-%d')} \nGenere: {self.medico.genere} \nIndirizzo: {self.medico.indirizzo}\nMail: {self.medico.mail} \nTelefono: {self.medico.telefono} \nReparto: {self.medico.id_reparto} \nAbilitazione: {self.medico.abilitazione} \nNota: {self.medico.nota}")
        messaggio.exec_()
        return

    """
        Metodo che permette di eseguire il logout chiudendo l'applicazione
    """
    def go_logout(self):
        QCoreApplication.quit()


