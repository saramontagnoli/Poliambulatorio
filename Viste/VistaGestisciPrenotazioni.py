"""
    Interfaccia grafica per la visualizzazione della lista delle prenotazioni
    La classe padre raggruppa al suo interno i metodi e attributi in comune tra VistaGestisciPrenmedico, VistaGestisciPrenPaziente
    e VistaGestisciPrenAmm
    (ereditarietà)
"""

from abc import abstractmethod

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QLineEdit, QLabel, QMessageBox

from Attivita.Prenotazione import ricerca
from Gestione.GestoreFile import caricaFile
from Viste.VistaPrenotazioneAmm import VistaPrenotazioneAmm
from Viste.VistaPrenotazioneMedico import VistaPrenotazioneMedico
from Viste.VistaPrenotazionePaziente import VistaPrenotazionePaziente


class VistaGestisciPrenotazioni(QWidget):

    """
        Costruttore della classe padre
        Set della finestra della visualizzazione della lista di prenotazioni
    """
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

    """
        Metodo che permette il caricamento del file prenotazioni nel dizionario prenotazioni
    """
    def load_prenotazioni(self):
        self.prenotazioni = caricaFile("Prenotazioni")

    """
        Metodo astratto che implementa l'aggiornamento della vista della lista delle prenotazioni
    """
    @abstractmethod
    def update_ui(self):
        pass

    """
        Metodo che permette la visualizzazione delle informazioni della prenotazione che si vuole aprire
        Controlla l'utente attuale e per ognuno apre la vista della prenotazione relativa
            - se sei l'addmin apre VistaPrenotazioneAmm
            - se sei un medico apre VistaPrenotazioneMedico
            - se sei un paziente apre VistaPrenotazionePaziente
    """
    def show_selected_info(self):
        try:
            selected = self.list_view.selectedIndexes()[0].data()
            tipo = selected.split(" ")[0].strip()
            id = int(selected.split(" ")[1].strip())
            prenotazione = None

            # ricerco la prenotazione che voglio aprire e poi controllo l'utente per vedere quale vista aprire
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

    """
        Metodo che permette di inserire caselle di testo e prelevare il valore all'interno aggiungedolo al dizionario qlines[]
    """
    def add_info_text(self, nome, label):
        self.h_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.h_layout.addWidget(current_text)

    """
        Metodo per la ricerca di un determinata Prenotazione sulla base dell'ID.
        Controllo che l'ID inserito sia valido
        Se trovo la prenotazione del dizionario prenotazioni controllo l'utente connesso e apro la vista della prenotazione relativa:
            - se sei l'addmin apre VistaPrenotazioneAmm
            - se sei un medico apre VistaPrenotazioneMedico
            - se sei un paziente apre VistaPrenotazionePaziente
        Se non trovo la prenotazione apro un pop up di errore
    """
    def ricerca_prenotazione_ID(self):
        # controllo validità dell'ID
        try:
            ID = int(self.qlines["ricerca"].text())
        except:
            QMessageBox.critical(self, 'Errore', 'L id non sembra un numero valido.', QMessageBox.Ok, QMessageBox.Ok)
            return

        f = 0
        # sccorro le prenotazioni, se la trovo controllo l'utente collegato, aprendo per ognuno la vista relativa
        for prenotazione in self.prenotazioni:
            if prenotazione.id == ID:
                if self.utente == "admin":
                    f = 1
                    print("SEI ADMIN")
                    self.vista_prenotazione = VistaPrenotazioneAmm(prenotazione, elimina_callback=self.update_ui)
                    self.vista_prenotazione.show()
                elif self.utente == "medico":
                    if prenotazione.id_medico == self.medico.id:
                        f = 1
                        self.vista_prenotazione = VistaPrenotazioneMedico(prenotazione, elimina_callback=self.update_ui)
                        self.vista_prenotazione.show()
                elif self.utente == "paziente":
                    if prenotazione.cf_paziente == self.paziente.CF:
                        f = 1
                        self.vista_prenotazione = VistaPrenotazionePaziente(prenotazione, elimina_callback=self.update_ui)
                        self.vista_prenotazione.show()

        # se non ho trovato la prenotazione apro un pop up di errore
        if f == 0:
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Non trovato")
            messaggio.setText("Non è stato trovato nessun prenotazione con questo ID. ")
            messaggio.exec_()
