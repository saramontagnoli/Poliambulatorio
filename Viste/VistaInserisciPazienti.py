"""
    Interfaccia grafica per l'inserimento di un nuovo paziente
"""

from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QComboBox

from Attivita.Paziente import Paziente
from Gestione.GestoreFile import caricaFile


class VistaInserisciPazienti(QWidget):
    """
        Costruttore della classe
        Set della finestra dell'inserimento di un nuovo paziente
        Inserimento caselle di testo per l'inserimento di un paziente nuovo
        Inserimento della combobox per scdelta di genere
        Inserimento button per conferma inserimento nuovo paziente
    """
    def __init__(self, callback):
        super(VistaInserisciPazienti, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qlines = {}

        # inserimento caselle di testo mediante metodo add_info_text
        self.add_info_text("id", "Id")
        self.add_info_text("password", "Password")
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("data_nascita", "Data Nascita (DD/MM/YYYY)")
        self.add_info_text("CF", "Codice Fiscale")
        self.add_info_text("mail", "Email")
        self.add_info_text("telefono", "Telefono")

        # inserimento di una combobox per selezionare il genere del paziente (M, F, A) e salvataggio nel diz. qlines[] della scelta
        self.combo_genere = QComboBox()

        options = ["M", "F", "A"]
        for option in options:
            self.combo_genere.addItem(option)

        self.combo_genere.currentIndexChanged.connect(self.selectionchange)
        self.topLabel = QLabel('Genere', self)
        self.v_layout.addWidget(self.topLabel)
        self.qlines["genere"] = self.combo_genere
        self.v_layout.addWidget(self.combo_genere)
        self.setLayout(self.v_layout)

        self.add_info_text("indirizzo", "Indirizzo")
        self.add_info_text("nota", "Nota")

        # inserimento checkbox per malattie pregresse o allergie del paziente
        self.add_checkbox("allergia", "Allergia")
        self.add_checkbox("malattia_pregressa", "Malattia pregressa")

        # inserimento del button di conferma, rimanda all'evento click per l'aggiunta del nuovo paziente
        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_paziente)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo paziente")

    def add_checkbox(self, nome, label):
        self.checkbox = QCheckBox(label, self)
        self.checkbox.resize(320, 40)
        self.qlines[nome] = self.checkbox
        self.v_layout.addWidget(self.checkbox)
        self.checkbox.stateChanged.connect(self.clickBox)

    """
        Metodo che permette di monitorare i cambiamenti alle selezioni sulla combobox
    """
    def selectionchange(self, i):
        return self.combo_genere.currentText()


    def clickBox(self, state):
        if state == QtCore.Qt.Checked:
            return True
        else:
            return False

    """
        Metodo che permette di inserire caselle di testo e prelevare il valore all'interno aggiungedolo al dizionario qlines[]
    """
    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)


    """
        Metodo che permette di effettuare l'aggiunta di un nuovo paziente da parte dell'amministratore
        Controllo la validità dell'ID
        Controllo che tutte le caselle siano state riempite
        Controllo che i dati inseriti siano corretti
        Controllo se il CF del paziente è già stato registrato
        Controllo se l'ID del paziente è già stato registrato
        Se non c'è nulla di errato il paziente viene aggiunto ed è visualizzabile nella lista dei pazienti, altrimenti
        stampo dei pop up di errore con la descrizione dettagliata dell'errore.
    """
    def aggiungi_paziente(self):
        # controllo che l'ID sia un numero, l'except blocca gli errori mostrando un pop up
        try:
            id = int(self.qlines["id"].text())
        except:
            QMessageBox.critical(self, 'Errore', 'L id non sembra un numero valido.', QMessageBox.Ok, QMessageBox.Ok)
            return

        # controllo che tutte le caselle siano riempite
        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return
        paziente = Paziente()

        # try-except per il controllo dell'esattezza dei dati
        try:
            password = self.qlines["password"].text()
            nome = self.qlines["nome"].text()
            cognome = self.qlines["cognome"].text()
            data_nascita = datetime.strptime(self.qlines["data_nascita"].text(), '%d/%m/%Y')
            CF = self.qlines["CF"].text()
            mail = self.qlines["mail"].text()
            telefono = self.qlines["telefono"].text()
            genere = self.qlines["genere"].currentText()
            indirizzo = self.qlines["indirizzo"].text()
            nota = self.qlines["nota"].text()
            allergia = self.qlines["allergia"].isChecked()
            malattia_pregressa = self.qlines["malattia_pregressa"].isChecked()

            # caricamento dei pazienti in dizionario pazienti, controllo se l'ID e il CF inseriti sono già utilizzati (se si pop up errore)
            pazienti = caricaFile("Pazienti")

            for paziente in pazienti:
                if CF == paziente.CF:
                    QMessageBox.critical(self, 'Errore', 'CF già utilizzato', QMessageBox.Ok,
                                         QMessageBox.Ok)
                    return
                if id == paziente.id:
                    QMessageBox.critical(self, 'Errore', 'ID già utilizzato', QMessageBox.Ok,
                                         QMessageBox.Ok)
                    return


            # chiamata al metodo setInfoPaziente con passaggio parametri per l'aggiunta del paziente
            paziente.setInfoPaziente(id, nome, cognome, password, data_nascita, CF, telefono, genere, mail, indirizzo,
                                     nota, allergia, malattia_pregressa)

        except:
            # pop up errore se i dati inseriti non sono corretti
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti', QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()
