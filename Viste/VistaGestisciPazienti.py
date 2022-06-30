import os.path
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from Attivita.Paziente import Paziente
from Viste.VistaPaziente import VistaPaziente
from Viste.VistaInserisciPazienti import VistaInserisciPazienti

#Interfaccia grafica per la gestione dei Pazienti (da parte dell'admin)
class VistaGestisciPazienti(QWidget):

    def __init__(self, parent=None):
        #stampa lista dei pazienti
        super(VistaGestisciPazienti, self).__init__(parent)
        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        #QPushButton per un nuovo Paziente o visualizzazione dati
        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton('Nuovo')
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

#Casella di testo per la ricerca
        self.h_layout.addWidget()
        current_text = QLineEdit(self)
        self.qlines["ricerca"] = current_text
        self.h_layout.addWidget(current_text)

#Pulsanti per la ricerca CF o ID
        ricerca_CF = QPushButton('Ricerca CF')
        ricerca_CF.clicked.connect(self.show_new)
        buttons_layout.addWidget(ricerca_CF)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        ricerca_ID = QPushButton('Ricerca ID')
        ricerca_ID.clicked.connect(self.show_new)
        buttons_layout.addWidget(ricerca_ID)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Gestisci Pazienti")

    #Load file Pazienti nel dizionario
    def load_pazienti(self):
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.pazienti.extend(current.values())

    #Stampa della lista aggiornata nella finestra dei pazienti
    def update_ui(self):
        self.pazienti = []
        self.load_pazienti()
        listview_model = QStandardItemModel(self.list_view)
        for paziente in self.pazienti:
            item = QStandardItem()
            nome = f"{paziente.nome} {paziente.cognome} - {type(paziente).__name__} {paziente.id}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.list_view.setModel(listview_model)

    #Permette la visualizzazione delle informazioni di un particolare paziente
    def show_selected_info(self):
        try:
            selected = self.list_view.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            id = int(selected.split("-")[1].strip().split(" ")[1])
            paziente = None
            if tipo == "Paziente":
                paziente = Paziente().ricercaUtilizzatoreId(id)
            self.vista_paziente = VistaPaziente(paziente, elimina_callback=self.update_ui)
            self.vista_paziente.show()
        except IndexError:
            print("INDEX ERROR")
            return

    #Richiama la vista per l'inserimento di un nuovo paziente
    def show_new(self):
        self.inserisci_paziente = VistaInserisciPazienti(callback=self.update_ui)
        self.inserisci_paziente.show()
