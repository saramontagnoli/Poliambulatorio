from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox

from Attivita.Medico import Medico
from Gestione.GestoreFile import caricaFile
from Viste.VistaInserisciMedici import VistaInserisciMedici
from Viste.VistaMedico import VistaMedico


# Interfaccia grafica per la gestione dei medici (da parte dell'admin)
class VistaGestisciMedici(QWidget):

    def __init__(self, parent=None):
        # stampa lista dei medici
        super(VistaGestisciMedici, self).__init__(parent)
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.h_layout.addWidget(self.list_view)
        self.qlines = {}

        # QPushButton per un nuovo Medico o visualizzazione dati
        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton('Nuovo')
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        # Casella di testo per la ricerca
        self.add_info_text("ricerca", "ricerca")

        # Pulsanti per la ricerca CF o ID
        ricerca_CF = QPushButton('Ricerca CF')
        ricerca_CF.clicked.connect(self.ricerca_medico_CF)
        buttons_layout.addWidget(ricerca_CF)
        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        ricerca_ID = QPushButton('Ricerca ID')
        ricerca_ID.clicked.connect(self.ricerca_medico_ID)
        buttons_layout.addWidget(ricerca_ID)
        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        self.qlines["ricerca_CF"] = ricerca_CF
        self.h_layout.addWidget(ricerca_CF)
        self.qlines["ricerca_ID"] = ricerca_ID
        self.h_layout.addWidget(ricerca_ID)

        self.setLayout(self.h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Gestisci Medici")

    # Load file Medici nel dizionario
    def load_medici(self):
        self.medici = caricaFile("Medici")

    # Stampa della lista aggiornata nella finestra dei medici
    def update_ui(self):
        self.medici = []
        self.load_medici()
        listview_model = QStandardItemModel(self.list_view)
        for medico in self.medici:
            item = QStandardItem()
            nome = f"{medico.nome} {medico.cognome} - {type(medico).__name__} {medico.id}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.list_view.setModel(listview_model)

    # Permette la visualizzazione delle informazioni di un particolare medico
    def show_selected_info(self):
        try:
            selected = self.list_view.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            id = int(selected.split("-")[1].strip().split(" ")[1])
            medico = None
            if tipo == "Medico":
                medico = Medico().ricercaUtilizzatoreId(id)
            self.vista_medico = VistaMedico(medico, elimina_callback=self.update_ui)
            self.vista_medico.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Nessun elemento selezionato', QMessageBox.Ok, QMessageBox.Ok)
            return

    # Richiama la vista per l'inserimento di un nuovo medico
    def show_new(self):
        self.inserisci_medico = VistaInserisciMedici(callback=self.update_ui)
        self.inserisci_medico.show()

    # Dati contenuti dentro la casella di testo della ricerca
    def add_info_text(self, nome, label):
        self.h_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.h_layout.addWidget(current_text)

    # Ricerca di un particolare medico mediante il codice fiscale
    def ricerca_medico_CF(self):
        f = 0
        CF = self.qlines["ricerca"].text()

        # controllo il codice fiscale dei medici inseriti
        for medico in self.medici:
            if medico.CF == CF:
                f = 1
                self.vista_medico = VistaMedico(medico, elimina_callback=self.update_ui)
                self.vista_medico.show()

        # Se non trovo nessun medico con quel CF stampo un pop-up di errore
        if f == 0:
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Non trovato")
            messaggio.setText("Non è stato trovato nessun medico con questo codice fiscale. ")
            messaggio.exec_()

    # Ricerca di un particolare paziente mediante l'ID
    def ricerca_medico_ID(self):
        f = 0
        # Controllo sull'ID (deve contenere solo numeri)
        try:
            ID = int(self.qlines["ricerca"].text())
        except:
            QMessageBox.critical(self, 'Errore', 'L id non sembra un numero valido.', QMessageBox.Ok, QMessageBox.Ok)
            return

        # controllo l'ID dei medici inseriti
        for medico in self.medici:
            if medico.id == ID:
                f = 1
                self.vista_medico = VistaMedico(medico, elimina_callback=self.update_ui)
                self.vista_medico.show()

        # Se non trovo nessun medico con quell'ID stampo un pop-up errore
        if f == 0:
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Non trovato")
            messaggio.setText("Non è stato trovato nessun medico con questo ID. ")
            messaggio.exec_()
