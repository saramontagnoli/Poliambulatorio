"""
    Interfaccia grafica per la visualizzazione della home dell'Amministratore
    Sono presenti 6 button che permettono di svolgere diverse funzioni:
        - gestire le prenotazioni della struttura
        - gestire i pazienti
        - gestire i medici
        - gestire le statistiche
        - gestire il backup dei dati
        - eseguire il logout
"""

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from Viste.VistaGestisciPazienti import VistaGestisciPazienti
from Viste.VistaGestisciMedici import VistaGestisciMedici
from Viste.VistaGestisciPrenAmm import VistaGestisciPrenAmm
from Viste.VistaStatistiche import VistaStatistiche
from Viste.VistaBackUp import VistaBackUp


class VistaHomeAmm(QWidget):
    """
        Costruttore della classe
        Si effettuano tutti i set di icone, size, titolo della finestra e visualizzazione
        Inserimento di 6 button che rimandano a:
            - gestisci prenotazioni
            - gestisci pazienti
            - gestisci medici
            - gestisci statistiche
            - gestisci backup
            - logout
        Ogni button ha l'evento click relativo che apre la vista per poter effettuare quella richiesta
    """
    def __init__(self, parent=None):
        super(VistaHomeAmm, self).__init__(parent)
        self.setWindowIcon(QIcon('CroceVerde.png'))
        grid_layout = QGridLayout()

        # button nella home dell'amministratore, ognuno con il suo evento click
        grid_layout.addWidget(self.get_generic_button("Gestisci Prenotazioni", self.go_prenotazioni), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Gestisci Pazienti", self.go_pazienti), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Gestisci Medici", self.go_medici), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Gestisci Statistiche", self.go_statistiche), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Gestisci BackUp", self.go_backup), 2, 0, 1, 2)
        grid_layout.addWidget(self.get_generic_button("Log-out", self.go_logout), 3, 0, 1, 2)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("ADMIN")


    """
        Metodo che inserisce il button e linka l'evento on_click
    """
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    """
        Metodi per eventi del click ai button visualizzati nella home dell'admin
    """
    def go_prenotazioni(self):
        # apertura della vista di gestione delle prenotazioni
        self.vista_gestisci_prenotazioni = VistaGestisciPrenAmm()
        self.vista_gestisci_prenotazioni.show()

    def go_pazienti(self):
        # apertura della vista di gestione dei pazienti
        self.vista_gestisci_pazienti = VistaGestisciPazienti()
        self.vista_gestisci_pazienti.show()

    def go_medici(self):
        # apertura della vista di gestione dei medici
        self.vista_gestisci_medici = VistaGestisciMedici()
        self.vista_gestisci_medici.show()

    def go_statistiche(self):
        # apertura della vista di gestione delle statistiche
        self.vista_statistiche = VistaStatistiche()
        self.vista_statistiche.show()

    def go_backup(self):
        # apertura della vista di gestione del backup
        self.vista_backup = VistaBackUp()
        self.vista_backup.show()


    """
        Metodo che permette di eseguire il logout chiudendo l'applicazione
    """
    def go_logout(self):
        QCoreApplication.quit()

