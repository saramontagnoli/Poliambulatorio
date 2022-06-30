from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QRadioButton
#from PyQt5.uic.properties import QtWidgets

from Attivita.Medico import Medico


class VistaInserisciMedici(QWidget):

    def __init__(self, callback):
        super(VistaInserisciMedici, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qlines = {}
        #Caselle di testo per inserimento informazioni del medico
        self.add_info_text("id", "Id")
        self.add_info_text("password", "Password")
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("data_nascita", "Data Nascita")
        self.add_info_text("CF", "Codice Fiscale")
        self.add_info_text("mail", "Email")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("genere", "Genere(M,F,A)")
        self.add_info_text("indirizzo", "Indirizzo")
        self.add_info_text("nota", "Nota")
        self.add_info_text("abilitazione", "Abilitazione")
        #self.add_info_text("allergia", "Allergia")
        #self.add_info_text("malattia_pregressa", "Malattia pregressa")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_medico)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo medico")

    """def add_checkbox(self, nome, label):
        self.checkbox = QCheckBox(label, self)
        self.checkbox.resize(320,40)
        self.qlines[nome] = self.checkbox
        self.v_layout.addWidget(self.checkbox)
        self.checkbox.stateChanged.connect(self.clickBox)

    def clickBox(self, state):
        if state == QtCore.Qt.Checked:
            return True
        else:
            return False """

    #Prelevo le informazioni scritte nelle caselle di testo
    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    #Aggiunta di un nuovo medico
    def aggiungi_medico(self):
        #controllo ID
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
        medico = Medico()

        #Controllo delle caselle di testo (devono essere tutte riempite)
        try:
            password = self.qlines["password"].text()
            nome = self.qlines["nome"].text()
            cognome = self.qlines["cognome"].text()
            data_nascita = datetime.strptime(self.qlines["data_nascita"].text(), '%d/%m/%Y')
            CF = self.qlines["CF"].text()
            mail = self.qlines["mail"].text()
            telefono = self.qlines["telefono"].text()
            genere = self.qlines["genere"].text()
            indirizzo = self.qlines["indirizzo"].text()
            nota = self.qlines["nota"].text()
            abilitazione = self.qlines["abilitazione"].text()

            #print(allergia)
            #print(malattia_pregressa)

            medico.setInfoMedico(id, nome, cognome, password, data_nascita, CF, telefono, genere, mail, indirizzo, nota, abilitazione)

        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()