"""
    Interfaccia grafica per la visualizzazione della home del paziente
    Sono presenti 4 button che permettono di svolgere diverse funzioni:
        - controllare le prenotazioni a carico del paziente corrente
        - modificare le informazioni del proprio profilo
        - visualizzare le informazioni del proprio profilo
        - eseguire il logout
"""

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QMessageBox

from Viste.VistaGestisciPrenPaziente import VistaGestisciPrenPaziente
from Viste.VistaModificaPaziente import VistaModificaPaziente


class VistaHomePaziente(QWidget):
    """
        Costruttore della classe
        Si effettuano tutti i set di icone, size, titolo della finestra e visualizzazione
        Inserimento di 4 button che rimandano a:
            - vedi prenotazioni
            - modifica informazioni
            - visualizza informazioni
            - logout
        Ogni pulsante ha l'evento click relativo che apre la vista per poter effettuare quella richiesta
    """
    def __init__(self, paziente, parent=None):
        super(VistaHomePaziente, self).__init__(parent)
        self.paziente = paziente
        self.setWindowIcon(QIcon('CroceVerde.png'))
        grid_layout = QGridLayout()
        print(self.paziente.CF)

        # button nella home del paziente, ognuno con il suo evento click
        grid_layout.addWidget(self.get_generic_button("Vedi Prenotazioni", self.go_prenotazioni), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Modifica Informazioni", self.go_modifica), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Visualizza Informazioni", self.go_vis_info), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Logout", self.go_logout), 1, 1)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle(f"{self.paziente.nome} {self.paziente.cognome} - {self.paziente.id}")

    """
        Metodo che inserisce il button e linka l'evento on_click
    """
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button


    """
        Metodi per eventi del click ai button visualizzati nella home del paziente
    """
    def go_prenotazioni(self):
        # apertura della vista di gestione delle prenotazioni del paziente
        self.vista_gestisci_pren_paziente = VistaGestisciPrenPaziente(self.paziente)
        self.vista_gestisci_pren_paziente.show()

    def go_modifica(self):
        # apertura della vista di modifica delle informazioni del paziente
        self.vista_modifica_paziente = VistaModificaPaziente(self.paziente)
        self.vista_modifica_paziente.show()


    def go_vis_info(self):
        messaggio = QMessageBox()
        messaggio.setWindowIcon(QIcon('CroceVerde.png'))
        messaggio.setWindowTitle("Profilo")

        # i campi boolean li trasformo in SI e NO per la leggibilità
        allergia_str = "No"
        malattia_pregressa_str = "No"
        if self.paziente.allergia:
            allergia_str = "Si"

        if self.paziente.malattia_pregressa:
            malattia_pregressa_str = "Si"

        # apertura pop up contenente le informazioni del paziente
        messaggio.setText(
            f"Id: {self.paziente.id} \nNome: {self.paziente.nome} \nCognome: {self.paziente.cognome} \nCF: {self.paziente.CF} \nData nascita: {self.paziente.data_nascita.strftime('%Y-%m-%d')} \nGenere: {self.paziente.genere} \nIndirizzo: {self.paziente.indirizzo}\nMail: {self.paziente.mail} \nTelefono: {self.paziente.telefono} \nNota: {self.paziente.nota} \nAllergia: {allergia_str} \nMalattia pregressa: {malattia_pregressa_str}")
        messaggio.exec_()
        return


    """
        Metodo che permette di eseguire il logout chiudendo l'applicazione
    """
    def go_logout(self):
        QCoreApplication.quit()
