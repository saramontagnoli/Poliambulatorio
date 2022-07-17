from PyQt5.QtGui import QIcon

from Attivita.Medico import Medico
import os
import pickle
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
from Attivita.Medico import Medico

class VistaInserisciMedici(QWidget):

    def __init__(self, callback):
        super(VistaInserisciMedici, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
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

        self.reparti = []

        if os.path.isfile('File/Reparti.pickle'):
            with open('File/Reparti.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.reparti.extend(current.values())

        # Creazione e riepimento con le visite della combobox
        self.combo_reparti = QComboBox()

        for reparto in self.reparti:
            id_reparto_nome = f"{reparto.id} {reparto.nome}"
            self.combo_reparti.addItem(id_reparto_nome)

        self.combo_reparti.currentIndexChanged.connect(self.selectionchange)
        self.qlines["reparto"] = self.combo_reparti
        self.v_layout.addWidget(self.combo_reparti)
        self.setLayout(self.v_layout)

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_medico)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo medico")

    def selectionchange(self, i):
        return self.combo_reparti.currentText()

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
            id_reparto = int(self.qlines["reparto"].currentText().split(" ")[0].strip())


            medico.setInfoMedico(id, password, cognome, nome, data_nascita, CF, telefono, genere, mail, indirizzo, nota, abilitazione, id_reparto)

        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()
