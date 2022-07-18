from PyQt5.QtGui import QIcon

from Attivita.Medico import Medico
import os
import pickle
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox

class VistaModificaMedico (QWidget):

    def __init__(self, medico, callback):

        super(VistaModificaMedico, self).__init__()
        self.medico = medico
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qlines = {}

        #Caselle di testo per inserimento informazioni del medico
        self.add_info_text("password", "Password")
        self.add_info_text("mail", "Email")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("indirizzo", "Indirizzo")
        self.add_info_text("nota", "Nota")
        self.add_info_text("abilitazione", "Abilitazione")

        btn_ok = QPushButton("Modifica")
        btn_ok.clicked.connect(self.modifica_medico)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica medico")

    #Prelevo le informazioni scritte nelle caselle di testo
    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    #Aggiunta di un nuovo medico
    def modifica_medico(self):

        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return

        #Controllo delle caselle di testo (devono essere tutte riempite)
        try:
            password = self.qlines["password"].text()
            mail = self.qlines["mail"].text()
            telefono = self.qlines["telefono"].text()
            indirizzo = self.qlines["indirizzo"].text()
            nota = self.qlines["nota"].text()
            abilitazione = self.qlines["abilitazione"].text()


            medico.setInfoMedico(self.medico.id, password, self.medico.cognome, self.medico.nome, self.medico.data_nascita, self.medico.CF, telefono, self.medico.genere, mail, indirizzo, nota, abilitazione, self.medico.id_reparto)

        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        self.callback()
        self.close()
