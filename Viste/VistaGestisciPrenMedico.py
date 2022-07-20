from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHBoxLayout, QListView, QVBoxLayout, QPushButton

from Viste.VistaGestisciPrenotazioni import VistaGestisciPrenotazioni


class VistaGestisciPrenMedico(VistaGestisciPrenotazioni):

    def __init__(self, medico, parent=None):
        # stampa lista delle prenotazioni
        super(VistaGestisciPrenotazioni, self).__init__(parent)
        self.medico = medico
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.h_layout.addWidget(self.list_view)
        self.qlines = {}
        self.utente = "medico"

        # QPushButton per una nuova Prenotazionee o Visualizzazione dati
        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

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

        # Stampa della lista aggiornata nella finestra dei prenotazioni

    def update_ui(self):
        self.prenotazioni = []
        self.load_prenotazioni()
        listview_model = QStandardItemModel(self.list_view)
        for prenotazione in self.prenotazioni:
            if prenotazione.id_medico == self.medico.id:
                prenotazione.scadenzaPrenotazione()
                item = QStandardItem()
                if not prenotazione.scaduta and not prenotazione.disdetta:
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
