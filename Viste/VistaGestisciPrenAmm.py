from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHBoxLayout, QListView, QVBoxLayout, QPushButton

from Viste.VistaGestisciPrenotazioni import VistaGestisciPrenotazioni
from Viste.VistaInserisciPrenotazioni import VistaInserisciPrenotazioni


# Interfaccia grafica per la gestione delle Prenotazioni (da parte dell'admin)
class VistaGestisciPrenAmm(VistaGestisciPrenotazioni):

    def __init__(self):
        # stampa lista delle prenotazioni
        super(VistaGestisciPrenotazioni, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.h_layout.addWidget(self.list_view)
        self.qlines = {}
        self.utente = "admin"

        # QPushButton per una nuova Prenotazionee o Visualizzazione dati
        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton('Nuova')
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        # Casella di testo per la ricerca
        self.add_info_text("ricerca", "ricerca")

        ricerca_ID = QPushButton('Ricerca ID')
        ricerca_ID.clicked.connect(self.ricerca_prenotazione_ID)
        buttons_layout.addWidget(ricerca_ID)
        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        self.qlines["ricerca_ID"] = ricerca_ID
        self.h_layout.addWidget(ricerca_ID)

        self.setLayout(self.h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Gestisci Prenotazioni")

    # Richiama la vista per l'inserimento di una nuova prenotazione
    def show_new(self):
        self.inserisci_prenotazione = VistaInserisciPrenotazioni(callback=self.update_ui)
        self.inserisci_prenotazione.show()

    # Dati contenuti dentro la casella di testo della ricerca

    def update_ui(self):
        self.prenotazioni = []
        self.load_prenotazioni()
        listview_model = QStandardItemModel(self.list_view)
        for prenotazione in self.prenotazioni:

            prenotazione.scadenzaPrenotazione()
            item = QStandardItem()
            if not prenotazione.scaduta and not prenotazione.disdetta and not prenotazione.conclusa:
                nome = f"P. {prenotazione.id}"
            else:
                nome = f"P. {prenotazione.id} (Non attiva)"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.list_view.setModel(listview_model)
