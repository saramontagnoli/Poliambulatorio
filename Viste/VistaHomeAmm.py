from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from Viste.VistaGestisciPazienti import VistaGestisciPazienti
from Viste.VistaGestisciMedici import VistaGestisciMedici
from Viste.VistaGestisciPrenotazioni import VistaGestisciPrenotazioni


class VistaHomeAmm(QWidget):

    # Pulsante con nome e relativo ONLICK, visualizzazione della finestra home del paziente
    def __init__(self, parent=None):
        super(VistaHomeAmm, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Gestisci Prenotazioni", self.go_prenotazioni), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Gestisci Pazienti", self.go_pazienti), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Gestisci Medici", self.go_medici), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Gestisci Statistiche", self.go_statistiche), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Gestisci BackUp", self.go_backup), 2, 0, 1, 2)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("ADMIN")

    # Funzionalità del QPushButton
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    # Metodi onclick
    def go_prenotazioni(self):
        self.vista_gestisci_prenotazioni = VistaGestisciPrenotazioni()
        self.vista_gestisci_prenotazioni.show()

    def go_pazienti(self):
        self.vista_gestisci_pazienti = VistaGestisciPazienti()
        self.vista_gestisci_pazienti.show()

    def go_medici(self):
        self.vista_gestisci_medici = VistaGestisciMedici()
        self.vista_gestisci_medici.show()

    def go_statistiche(self):
        pass

    def go_backup(self):
        pass
