"""
    Interfaccia grafica per la visualizzazione della lista dei medici LATO ADMIN
"""

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox

from Attivita.Medico import Medico
from Gestione.GestoreFile import caricaFile
from Viste.VistaInserisciMedici import VistaInserisciMedici
from Viste.VistaMedico import VistaMedico


class VistaGestisciMedici(QWidget):
    """
        Costruttore della classe
        Set della finestra della visualizzazione della lista di medici
        Inserimenti di due button per apertura medico e nuovo medico
        Inserimento casella di testo per ricerca dei medici per ID o CF a seconda del button premuto
    """

    def __init__(self, parent=None):
        super(VistaGestisciMedici, self).__init__(parent)
        self.inserisci_medico = None
        self.vista_medico = None
        self.medici = None
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.h_layout.addWidget(self.list_view)
        self.qlines = {}

        # inserimento button per apertura del medico, rimanda all'evento click show_selected_info che visualizza il medico
        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        # inserimento button per inserimento nuovo medico, rimanda all'evento click show_new che visualizza la vista di inserimento
        new_button = QPushButton('Nuovo')
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        # inserimento caselle di testo mediante metodo add_info_text per inserire l'id o il cf del medico da ricercare
        self.add_info_text("ricerca", "ricerca")

        # inserimento button per ricerca del medico secondo l'ID o il CF, rimanda all'evento click ricerca_medico_ID e CF
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

    """
        Metodo che permette il caricamento del file medici nel dizionario medici
    """

    def load_medici(self):
        self.medici = caricaFile("Medici")

    """
        Metodo che permette l'aggiornamento della lista dei medici nella vista
        Carico le informazioni dei medici nel dizionario pazienti
        Carico anche tutti gli elementi Qt mediante QStandardItemModel
        Scorro tutti i medici, per ogni medico creo un Item e stampo ID e nome e cognome
        Aggiungo l'elemento medico alla vista lista degli elementi
        Ho quindi una lista di item contenente tutti i medici
    """

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

    """
        Metodo che permette la visualizzazione delle informazioni del medico che si vuole aprire
        Cerco il medico selezionato che voglio aprire e richiamo la vista di visualizzazione delle informazioni
    """

    def show_selected_info(self):
        try:
            selected = self.list_view.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            id = int(selected.split("-")[1].strip().split(" ")[1])
            medico = None

            # cerco il medico che sto cercando di aprire
            if tipo == "Medico":
                medico = Medico().ricercaUtilizzatoreId(id)

            # apro la vista di visualizzazione delle informazioni del medico
            self.vista_medico = VistaMedico(medico, elimina_callback=self.update_ui)
            self.vista_medico.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Nessun elemento selezionato', QMessageBox.Ok, QMessageBox.Ok)
            return

    """
        Metodo che gestisce l'evento click dell'inserimento di un nuovo medico
        Permette l'apertura della vista per l'inserimento di un nuovo medico
    """

    def show_new(self):
        self.inserisci_medico = VistaInserisciMedici(callback=self.update_ui)
        self.inserisci_medico.show()

    """
        Metodo che permette di inserire caselle di testo e prelevare il valore all'interno aggiungendolo al dizionario qlines[]
    """

    def add_info_text(self, nome, label):
        self.h_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.h_layout.addWidget(current_text)

    """
        Metodo per la ricerca di un determinato Medico sulla base del CF.
        Controllo che il CF inserito sia valido
        Se trovo il medico che sto cercando richiamo la vista per la visualizzazione delle informazioni del medico
        Se non trovo il medico apro un pop up di errore
    """

    def ricerca_medico_CF(self):
        f = 0

        # prelevo il CF dal campo
        CF = self.qlines["ricerca"].text()

        # scorro i pazienti cercando quello con il CF specificato, se lo trovo richiamo la vista di visualizzazione delle info
        for medico in self.medici:
            if medico.CF == CF:
                f = 1
                self.vista_medico = VistaMedico(medico, elimina_callback=self.update_ui)
                self.vista_medico.show()

        # se non trovo il paziente apro un pop up di errore
        if f == 0:
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Non trovato")
            messaggio.setText("Non è stato trovato nessun medico con questo codice fiscale. ")
            messaggio.exec_()

    """
        Metodo per la ricerca di un determinato Medico sulla base dell'ID.
        Controllo che l'ID inserito sia valido
        Se trovo il medico che sto cercando richiamo la vista per la visualizzazione delle informazioni del medico
        Se non trovo il medico apro un pop up di errore
    """

    def ricerca_medico_ID(self):
        f = 0
        # prelevo l'ID dal campo controllando anche che sia valido
        try:
            ID = int(self.qlines["ricerca"].text())
        except:
            QMessageBox.critical(self, 'Errore', 'L id non sembra un numero valido.', QMessageBox.Ok, QMessageBox.Ok)
            return

        # scorro i medici cercando quello con l'ID specificato, se lo trovo richiamo la vista di visualizzazione delle info
        for medico in self.medici:
            if medico.id == ID:
                f = 1
                self.vista_medico = VistaMedico(medico, elimina_callback=self.update_ui)
                self.vista_medico.show()

        # se non trovo il medico apro un pop up di errore
        if f == 0:
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Non trovato")
            messaggio.setText("Non è stato trovato nessun medico con questo ID. ")
            messaggio.exec_()
