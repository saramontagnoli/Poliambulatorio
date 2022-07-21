"""
    Interfaccia grafica per la visualizzazione della lista delle prenotazioni LATO PAZIENTE
    Si stampa una lista, cliccando sulla prenotazione desiderata e cliccando APRI si può visualizzare le informazioni
    della prenotazione.
    E' presente una casella di testa che permette la ricerca secondo ID grazie al button corrispondente
    La classe figlia eredita i metodi e attributi dalla classe padre VistaGestisciPrenotazioni
    (ereditarietà)
"""

from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHBoxLayout, QListView, QVBoxLayout, QPushButton

from Viste.VistaGestisciPrenotazioni import VistaGestisciPrenotazioni


class VistaGestisciPrenPaziente(VistaGestisciPrenotazioni):
    """
        Costruttore della classe figlia
        Set della finestra della visualizzazione della lista di prenotazioni
        Inserimento dei button per apertura prenotazione
        Inserimento casella di testo e due button per la ricerca secondo ID
    """
    def __init__(self, paziente, parent=None):
        super(VistaGestisciPrenotazioni, self).__init__(parent)
        self.paziente = paziente
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.h_layout.addWidget(self.list_view)
        self.qlines = {}
        self.utente = "paziente"

        # inserimento button per apertura della prenotazione, rimanda all'evento click show_selecteed_info che visualizza la prenotazione
        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        # inserimento caselle di testo mediante metodo add_info_text per inserire l'id da ricercare
        self.add_info_text("ricerca", "ricerca")

        # inserimento button per ricerca della prenotazione secondo l'ID, rimanda all'evento click ricerca_prenotazione_ID
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

    """
        Metodo che permette l'aggiornamento della lista delle prenotazioni nella vista
        Carico le informazioni delle prenotazioni nel dizionario prenotazioni
        Carico anche tutti gli elementi Qt mediante QStandardItemModel
        Scorro tutte le prenotazioni controllando se quella appena inserita sia scadute o no, per la prenotazione creo un Item e stampo
        P. e l'ID della prenotazione
        Se la prenotazione è disdetta o scaduta o conclusa vicino aggiungo (NON ATTIVA)
        Aggiungo l'elemento prenotazione alla vista lista degli elementi
        Nella vista prendo solo le prenotazioni corrispondenti al paziente attuale
    """
    def update_ui(self):
        # caricamento del dizionario
        self.prenotazioni = []
        self.load_prenotazioni()
        listview_model = QStandardItemModel(self.list_view)
        for prenotazione in self.prenotazioni:
            if prenotazione.cf_paziente == self.paziente.CF:
                # cotnrollo la scadenza della prenotazione
                prenotazione.scadenzaPrenotazione()
                item = QStandardItem()

                # esecuzione controlli per stampare se una prenotazione è attiva o no
                if not prenotazione.scaduta and not prenotazione.disdetta and not prenotazione.conclusa:
                    nome = f"P. {prenotazione.id}"
                else:
                    nome = f"P. {prenotazione.id} (Non attiva)"
                item.setText(nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)

                # aggiunta dell'elemento nella lista degli elementi in cui sono contenute le prenotazioni
                listview_model.appendRow(item)
        self.list_view.setModel(listview_model)


