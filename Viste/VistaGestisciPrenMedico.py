import os.path
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox

from Attivita.Prenotazione import Prenotazione
from Viste.VistaPrenotazione import VistaPrenotazione
from Viste.VistaInserisciPrenotazioni import VistaInserisciPrenotazioni

class VistaGestisciPrenMedico:
    def __init__(self, medico, parent=None,):
        self.medico = medico
        # stampa lista delle prenotazioni
        super(VistaGestisciPrenMedico, self).__init__(parent)
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.h_layout.addWidget(self.list_view)
        self.qlines = {}

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

    # Load file Prenotazioni nel dizionario
    def load_prenotazioni(self):
        if os.path.isfile('File/Prenotazioni.pickle'):
            with open('File/Prenotazioni.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.prenotazioni.extend(current.values())

        for prenotazione in prenotazioni:
            if prenotazione.id_medico != self.medico.id:
                del prenotazioni[prenotazione.id]

    # Stampa della lista aggiornata nella finestra dei prenotazioni
    def update_ui(self):
        self.prenotazioni = []
        self.load_prenotazioni()
        listview_model = QStandardItemModel(self.list_view)
        for prenotazione in self.prenotazioni:
            prenotazione.scadenzaPrenotazione()
            item = QStandardItem()
            nome = f"{type(prenotazione).__name__} {prenotazione.id}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.list_view.setModel(listview_model)

    # Permette la visualizzazione delle informazioni di una particolare prenotazione
    def show_selected_info(self):
        try:
            selected = self.list_view.selectedIndexes()[0].data()
            tipo = selected.split(" ")[0].strip()
            id = int(selected.split(" ")[1].strip())
            prenotazione = None

            if tipo == "Prenotazione":
                prenotazione = Prenotazione().ricerca(id)
            self.vista_prenotazione = VistaPrenotazione(prenotazione, elimina_callback=self.update_ui)
            self.vista_prenotazione.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Nessun elemento selezionato', QMessageBox.Ok, QMessageBox.Ok)
            return

    # Richiama la vista per l'inserimento di una nuova prenotazione
    def show_new(self):
        self.inserisci_prenotazione = VistaInserisciPrenotazioni(callback=self.update_ui)
        self.inserisci_prenotazione.show()

    # Dati contenuti dentro la casella di testo della ricerca
    def add_info_text(self, nome, label):
        self.h_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.h_layout.addWidget(current_text)

    # Ricerca di una particolare prenotazione mediante l'ID
    def ricerca_prenotazione_ID(self):
        # Controllo sull'ID (deve contenere solo numeri)
        try:
            ID = int(self.qlines["ricerca"].text())
        except:
            QMessageBox.critical(self, 'Errore', 'L id non sembra un numero valido.', QMessageBox.Ok, QMessageBox.Ok)
            return

        f = 0
        # controllo l'ID delle prenotazioni inserite
        for prenotazione in self.prenotazioni:
            if prenotazione.id == ID:
                f = 1
                self.vista_prenotazione = VistaPrenotazione(prenotazione, elimina_callback=self.update_ui)
                self.vista_prenotazione.show()

        # Se non trovo nessuna prenotazione con quell'ID stampo un pop-up di errore
        if f == 0:
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Non trovato")
            messaggio.setText("Non è stato trovato nessun prenotazione con questo ID. ")
            messaggio.exec_()
