import os.path
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from Attivita.Medico import Medico
from Viste.VistaMedico import VistaMedico
from Viste.VistaInserisciMedici import VistaInserisciMedici

#Interfaccia grafica per la gestione dei medici (da parte dell'admin)
class VistaGestisciMedici(QWidget):

    def __init__(self, parent=None):
        #stampa lista dei medici
        super(VistaGestisciMedici, self).__init__(parent)
        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        #QPushButton per un nuovo Medico o visualizzazione dati
        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton('Nuovo')
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Gestisci Medici")

    #Load file Medici nel dizionario
    def load_medici(self):
        if os.path.isfile('File/Medici.pickle'):
            with open('File/Medici.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.medici.extend(current.values())

    #Stampa della lista aggiornata nella finestra dei medici
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

    #Permette la visualizzazione delle informazioni di un particolare medico
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
            print("INDEX ERROR")
            return

    #Richiama la vista per l'inserimento di un nuovo medico
    def show_new(self):
        self.inserisci_medico = VistaInserisciMedici(callback=self.update_ui)
        self.inserisci_medico.show()
