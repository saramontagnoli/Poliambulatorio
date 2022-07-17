import os
import pickle
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
from Attivita.Prenotazione import Prenotazione


class VistaInserisciPrenotazioni(QWidget):

    def __init__(self, callback):
        super(VistaInserisciPrenotazioni, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qlines = {}
        # Caselle di testo per inserimento informazioni del paziente
        self.add_info_text("id", "Id")
        self.add_info_text("data", "Data")
        self.add_info_text("cf_paziente", "CF Paziente")

# Combo box lista orari dell'ambulatorio
        # Creazione e riepimento con le visite della combobox
        self.combo_ora = QComboBox()

        options = ["8:00","8:30","9:00","9:30", "10:00", "10:30", "11:00", "11:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30"]

        for option in options:
            self.combo_ora.addItem(option)

        self.combo_ora.currentIndexChanged.connect(self.selectionchange)
        self.qlines["ora"] = self.combo_ora
        self.v_layout.addWidget(self.combo_ora)
        self.setLayout(self.v_layout)

# Combo box lista visite
        self.visite = []

        if os.path.isfile('File/Visite.pickle'):
            with open('File/Visite.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.visite.extend(current.values())

        # Creazione e riepimento con le visite della combobox
        self.combo_visita = QComboBox()

        for visita in self.visite:
            self.combo_visita.addItem(visita.nome)

        self.combo_visita.currentIndexChanged.connect(self.selectionchange)
        self.qlines["visita"] = self.combo_visita
        self.v_layout.addWidget(self.combo_visita)
        self.setLayout(self.v_layout)

# Combo box per lista medici
        self.medici = []

        if os.path.isfile('File/Medici.pickle'):
            with open('File/Medici.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.medici.extend(current.values())

        # Creazione e riepimento con cognomi dei medici della combobox
        self.combo_medico = QComboBox()

        for medico in self.medici:
            id_cognome = f"{medico.id} {medico.cognome}"
            #id_cognome = medico.id + medico.cognome
            self.combo_medico.addItem(id_cognome)

        self.combo_medico.currentIndexChanged.connect(self.selectionchange)
        self.qlines["medico"] = self.combo_medico
        self.v_layout.addWidget(self.combo_medico)
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
            #ora = datetime.strptime(self.qlines["ora"].text(), '%H:%M')
            # ora = time.strftime(self.qlines["ora"].text(), '%H:%M')
            # id_visita = (self.qlines["visita"].currentText())

            ora = datetime.strptime(self.qlines["ora"].currentText(), '%H:%M')

            cf_paziente = self.qlines["cf_paziente"].text()

            id_visita = int(self.qlines["visita"].currentIndex()) + 1

            id_medico = int(self.qlines["medico"].currentText().split(" ")[0].strip())

            prova = prenotazione.aggiungiPrenotazione(id, data, ora, id_medico, id_visita, cf_paziente)

            #errore cf paziente non esistente
            if prova == 0:
                QMessageBox.critical(self, 'Errore', 'Codice fiscale non valido',
                                 QMessageBox.Ok, QMessageBox.Ok)
                return

            #sto scegliendo una visita e un medico di reparti diversi
            if prova == -1:
                QMessageBox.critical(self, 'Errore', 'Il reparto del medico e della visita non corrispondono',
                                 QMessageBox.Ok, QMessageBox.Ok)
                return

            #il medico ha già un'altra visita
            if prova == -2:
                QMessageBox.critical(self, 'Errore', 'Il medico è già impegnato in un''altra visita',
                                 QMessageBox.Ok, QMessageBox.Ok)
                return

            #sto prenotando di sabato o domenica
            if prova == -3:
                QMessageBox.critical(self, 'Errore', 'Il sabato e la domenica l''ambulatorio è chiuso',
                                 QMessageBox.Ok, QMessageBox.Ok)
                return

            if prova == -4:
                QMessageBox.critical(self, 'Errore', 'Il paziente ha già prenotato per un''altra visita in questa data e ora',
                                 QMessageBox.Ok, QMessageBox.Ok)
                return

            if prova == -5:
                QMessageBox.critical(self, 'Errore', 'Il paziente ha troppe prenotazioni attive al momento',
                                 QMessageBox.Ok, QMessageBox.Ok)
                return
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()
