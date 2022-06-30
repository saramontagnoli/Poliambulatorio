import os.path
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox

from Attivita.Paziente import Paziente
from Viste.VistaPaziente import VistaPaziente
from Viste.VistaInserisciPazienti import VistaInserisciPazienti

#Interfaccia grafica per la gestione dei Pazienti (da parte dell'admin)
class VistaGestisciPazienti(QWidget):

    def __init__(self, parent=None):
        #stampa lista dei pazienti
        super(VistaGestisciPazienti, self).__init__(parent)
        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.h_layout.addWidget(self.list_view)
        self.qlines = {}

        #QPushButton per un nuovo Paziente o visualizzazione dati
        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton('Nuovo')
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

#Casella di testo per la ricerca
        self.add_info_text("ricerca", "ricerca")


#Pulsanti per la ricerca CF o ID
        ricerca_CF = QPushButton('Ricerca CF')
        ricerca_CF.clicked.connect(self.ricerca_paziente_CF)
        buttons_layout.addWidget(ricerca_CF)
        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        ricerca_ID = QPushButton('Ricerca ID')
        ricerca_ID.clicked.connect(self.ricerca_paziente_ID)
        buttons_layout.addWidget(ricerca_ID)
        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        self.qlines["ricerca_CF"] = ricerca_CF
        self.h_layout.addWidget(ricerca_CF)
        self.qlines["ricerca_ID"] = ricerca_ID
        self.h_layout.addWidget(ricerca_ID)


        self.setLayout(self.h_layout)
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

    def add_info_text(self, nome, label):
        self.h_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.h_layout.addWidget(current_text)

    def ricerca_paziente_CF(self):
        f = 0
        CF = self.qlines["ricerca"].text()
        for paziente in pazienti:
            if paziente.CF == CF:
                f = 1
                self.vista_paziente = VistaPaziente(paziente, elimina_callback=self.update_ui)
                self.vista_paziente.show()

        if f == 0 :
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Non trovato")
            messaggio.setText("Non è stato trovato nessun paziente con questo codice fiscale. ")
            messaggio.exec_()



    def ricerca_paziente_ID(self):
        f = 0
        ID = int(self.qlines["ricerca"].text())
        for paziente in pazienti:
            if paziente.id == ID:
                f = 1
                self.vista_paziente = VistaPaziente(paziente, elimina_callback=self.update_ui)
                self.vista_paziente.show()

        if f == 0 :
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Non trovato")
            messaggio.setText("Non è stato trovato nessun paziente con questo ID. ")
            messaggio.exec_()
