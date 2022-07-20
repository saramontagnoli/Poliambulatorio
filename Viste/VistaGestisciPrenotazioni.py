import os.path
import pickle
from abc import abstractmethod

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QLineEdit, QLabel, QMessageBox

from Attivita.Prenotazione import ricerca
from Viste.VistaPrenotazioneAmm import VistaPrenotazioneAmm

# Interfaccia grafica per la gestione delle Prenotazioni (da parte dell'admin)
from Viste.VistaPrenotazioneMedico import VistaPrenotazioneMedico
from Viste.VistaPrenotazionePaziente import VistaPrenotazionePaziente


class VistaGestisciPrenotazioni(QWidget):

    # INIT DIVERSO PER TUTTE
    def __init__(self, parent=None):
        # stampa lista delle prenotazioni
        super(VistaGestisciPrenotazioni, self).__init__(parent)
        self.prenotazioni = []
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.h_layout.addWidget(self.list_view)
        self.qlines = {}
        self.utente = ""

    # Load file Prenotazioni nel dizionario
    def load_prenotazioni(self):
        if os.path.isfile('File/Prenotazioni.pickle'):
            with open('File/Prenotazioni.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.prenotazioni.extend(current.values())

    # Stampa della lista aggiornata nella finestra dei prenotazioni
    @abstractmethod
    def update_ui(self):
        pass

    # Permette la visualizzazione delle informazioni di una particolare prenotazione
    def show_selected_info(self):
        try:
            selected = self.list_view.selectedIndexes()[0].data()
            tipo = selected.split(" ")[0].strip()
            id = int(selected.split(" ")[1].strip())
            prenotazione = None

            if tipo == "P.":
                prenotazione = ricerca(id)

            if self.utente == "admin":
                f = 1
                print("SEI ADMIN")
                self.vista_prenotazione = VistaPrenotazioneAmm(prenotazione, elimina_callback=self.update_ui)
                self.vista_prenotazione.show()
            elif self.utente == "medico":
                f = 1
                self.vista_prenotazione = VistaPrenotazioneMedico(prenotazione, elimina_callback=self.update_ui)
                self.vista_prenotazione.show()
            elif self.utente == "paziente":
                f = 1
                self.vista_prenotazione = VistaPrenotazionePaziente(prenotazione, elimina_callback=self.update_ui)
                self.vista_prenotazione.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Nessun elemento selezionato', QMessageBox.Ok, QMessageBox.Ok)
            return

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
                if self.utente == "admin":
                    f = 1
                    print("SEI ADMIN")
                    self.vista_prenotazione = VistaPrenotazioneAmm(prenotazione, elimina_callback=self.update_ui)
                    self.vista_prenotazione.show()
                elif self.utente == "medico":
                    f = 1
                    self.vista_prenotazione = VistaPrenotazioneMedico(prenotazione, elimina_callback=self.update_ui)
                    self.vista_prenotazione.show()
                elif self.utente == "paziente":
                    f = 1
                    self.vista_prenotazione = VistaPrenotazionePaziente(prenotazione, elimina_callback=self.update_ui)
                    self.vista_prenotazione.show()

        # Se non trovo nessuna prenotazione con quell'ID stampo un pop-up di errore
        if f == 0:
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Non trovato")
            messaggio.setText("Non è stato trovato nessun prenotazione con questo ID. ")
            messaggio.exec_()
