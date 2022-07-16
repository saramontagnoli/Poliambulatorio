import os
import pickle
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox

from Attivita.Prenotazione import Prenotazione
from Attivita.Visita import Visita


class VistaInserisciPrenotazioni(QWidget):

    def __init__(self, callback):
        super(VistaInserisciPrenotazioni, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qlines = {}
        # Caselle di testo per inserimento informazioni del paziente
        self.add_info_text("id", "Id")
        self.add_info_text("data", "Data")
        self.add_info_text("ora", "Ora")

        self.visite = []

        # Apertura file visite per inserimento in combobox
        if os.path.isfile('File/Visite.pickle'):
            with open('File/Visite.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.visite.extend(current.values())

        self.combo_visita = QComboBox()

        for visita in self.visite:
            self.combo_visita.addItem(visita.nome)

        self.combo_visita.currentIndexChanged.connect(self.selectionchange)
        self.qlines["visita"] = self.combo_visita
        self.v_layout.addWidget(self.combo_visita)
        self.setLayout(self.v_layout)

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_prenotazione)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuova prenotazione")

    def selectionchange(self,i):
        return self.combo_visita.currentText()

    # Prelevo le informazioni scritte nelle caselle di testo
    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    # Aggiunta di un nuovo paziente
    def aggiungi_prenotazione(self):
        # controllo ID
        try:
            id = int(self.qlines["id"].text())
        except:
            QMessageBox.critical(self, 'Errore', 'L id non sembra un numero valido.', QMessageBox.Ok, QMessageBox.Ok)
            return

        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return
        prenotazione = Prenotazione()

        # Controllo delle caselle di testo (devono essere tutte riempite)
        try:
            data = datetime.strptime(self.qlines["data"].text(), '%d/%m/%Y')
            # print(data)
            ora = datetime.strptime(self.qlines["ora"].text(), '%H:%M')
            # ora = time.strftime(self.qlines["ora"].text(), '%H:%M')
            # id_visita = (self.qlines["visita"].currentText())


            id_visita = int(self.qlines["visita"].currentIndex()) + 1
            print (id_visita)
            prenotazione.aggiungiPrenotazione(id, data, ora)
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()
