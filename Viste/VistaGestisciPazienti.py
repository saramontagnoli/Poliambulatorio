"""
    Interfaccia grafica per la visualizzazione della lista dei pazienti LATO ADMIN
"""

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox

from Attivita.Paziente import Paziente
from Gestione.GestoreFile import caricaFile
from Viste.VistaInserisciPazienti import VistaInserisciPazienti
from Viste.VistaPaziente import VistaPaziente


class VistaGestisciPazienti(QWidget):
    """
        Costruttore della classe
        Set della finestra della visualizzazione della lista di pazienti
        Inserimenti di due button per apertura paziente e nuovo paziente
        Inserimento casella di testo per ricerca dei pazienti per ID o CF a seconda del button premuto
    """

    def __init__(self, parent=None):
        super(VistaGestisciPazienti, self).__init__(parent)
        self.inserisci_paziente = None
        self.vista_paziente = None
        self.pazienti = None
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.h_layout.addWidget(self.list_view)
        self.qlines = {}

        # inserimento button per apertura del paziente, rimanda all'evento click show_selected_info che visualizza il paziente
        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        # inserimento button per inserimento nuovo paziente, rimanda all'evento click show_new che visualizza la vista di inserimento
        new_button = QPushButton('Nuovo')
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        # inserimento caselle di testo mediante metodo add_info_text per inserire l'id o il cf del paziente da ricercare
        self.add_info_text("ricerca", "ricerca")

        # inserimento button per ricerca del paziente secondo l'ID o il CF, rimanda all'evento click ricerca_paziente_ID e CF
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

    """
        Metodo che permette il caricamento del file pazienti nel dizionario pazienti
    """

    def load_pazienti(self):
        self.pazienti = caricaFile("Pazienti")

    """
        Metodo che permette l'aggiornamento della lista dei pazienti nella vista
        Carico le informazioni dei pazienti nel dizionario pazienti
        Carico anche tutti gli elementi Qt mediante QStandardItemModel
        Scorro tutti i pazienti, per ogni paziente creo un Item e stampo ID e nome e cognome
        Aggiungo l'elemento paziente alla vista lista degli elementi
        Ho quindi una lista di item contenente tutti i pazienti
    """

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

    """
        Metodo che permette la visualizzazione delle informazioni del paziente che si vuole aprire
        Cerco il paziente selezionato che voglio aprire e richiamo la vista di visualizzazione delle informazioni
    """

    def show_selected_info(self):
        try:
            selected = self.list_view.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            id = int(selected.split("-")[1].strip().split(" ")[1])
            paziente = None

            # cerco il paziente che sto cercando di aprire
            if tipo == "Paziente":
                paziente = Paziente().ricercaUtilizzatoreId(id)

            # apro la vista di visualizzazione delle informazioni del paziente
            self.vista_paziente = VistaPaziente(paziente, elimina_callback=self.update_ui)
            self.vista_paziente.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Nessun elemento selezionato', QMessageBox.Ok, QMessageBox.Ok)
            return

    """
        Metodo che gestisce l'evento click dell'inserimento di un nuovo paziente
        Permette l'apertura della vista per l'inserimento di un nuovo paziente
    """

    def show_new(self):
        self.inserisci_paziente = VistaInserisciPazienti(callback=self.update_ui)
        self.inserisci_paziente.show()

    """
        Metodo che permette di inserire caselle di testo e prelevare il valore all'interno aggiungendolo al dizionario qlines[]
    """

    def add_info_text(self, nome, label):
        self.h_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.h_layout.addWidget(current_text)

    """
        Metodo per la ricerca di un determinato Paziente sulla base del CF.
        Controllo che il CF inserito sia valido
        Se trovo il paziente che sto cercando richiamo la vista per la visualizzazione delle informazioni del paziente
        Se non trovo il paziente apro un pop up di errore
    """

    def ricerca_paziente_CF(self):
        f = 0

        # prelevo il CF dal campo
        CF = self.qlines["ricerca"].text()

        # scorro i pazienti cercando quello con il CF specificato, se lo trovo richiamo la vista di visualizzazione delle info
        for paziente in self.pazienti:
            if paziente.CF == CF:
                f = 1
                self.vista_paziente = VistaPaziente(paziente, elimina_callback=self.update_ui)
                self.vista_paziente.show()

        # se non trovo il paziente apro un pop up di errore
        if f == 0:
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Non trovato")
            messaggio.setText("Non è stato trovato nessun paziente con questo codice fiscale. ")
            messaggio.exec_()

    """
        Metodo per la ricerca di un determinato Paziente sulla base dell'ID.
        Controllo che l'ID inserito sia valido
        Se trovo il paziente che sto cercando richiamo la vista per la visualizzazione delle informazioni del paziente
        Se non trovo il paziente apro un pop up di errore
    """

    def ricerca_paziente_ID(self):
        # prelevo l'ID dal campo controllando anche che sia valido
        try:
            ID = int(self.qlines["ricerca"].text())
        except:
            QMessageBox.critical(self, 'Errore', 'L id non sembra un numero valido.', QMessageBox.Ok, QMessageBox.Ok)
            return

        f = 0
        # scorro i pazienti cercando quello con l'ID specificato, se lo trovo richiamo la vista di visualizzazione delle info
        for paziente in self.pazienti:
            if paziente.id == ID:
                f = 1
                self.vista_paziente = VistaPaziente(paziente, elimina_callback=self.update_ui)
                self.vista_paziente.show()

        # se non trovo il paziente apro un pop up di errore
        if f == 0:
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Non trovato")
            messaggio.setText("Non è stato trovato nessun paziente con questo ID. ")
            messaggio.exec_()
