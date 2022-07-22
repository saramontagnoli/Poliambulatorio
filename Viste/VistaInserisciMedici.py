"""
    Interfaccia grafica per l'inserimento di un nuovo medico
"""

from datetime import datetime

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox

from Attivita.Medico import Medico
from Gestione.GestoreFile import caricaFile


class VistaInserisciMedici(QWidget):
    """
        Costruttore della classe
        Set della finestra dell'inserimento di un nuovo medico
        Inserimento caselle di testo per l'inserimento di un medico nuovo
        Inserimento della combobox per scelta di genere e reparto
        Inserimento button per conferma inserimento nuovo medico
    """
    def __init__(self, callback):
        super(VistaInserisciMedici, self).__init__()
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

        # Inserimento di una combobox per selezionare il genere del medico (M, F, A) e salvataggio nel diz. qlines[] della scelta
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
        self.add_info_text("abilitazione", "Abilitazione")

        self.reparti = caricaFile("Reparti")

        # Creazione e riempimento con le visite della combobox
        self.combo_reparti = QComboBox()

        for reparto in self.reparti:
            id_reparto_nome = f"{reparto.id} {reparto.nome}"
            self.combo_reparti.addItem(id_reparto_nome)

        self.combo_reparti.currentIndexChanged.connect(self.selectionchange)
        self.topLabel = QLabel('Reparto', self)
        self.v_layout.addWidget(self.topLabel)
        self.qlines["reparto"] = self.combo_reparti
        self.v_layout.addWidget(self.combo_reparti)
        self.setLayout(self.v_layout)

        # inserimento del button di conferma, rimanda all'evento click per l'aggiunta del nuovo medico
        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_medico)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo medico")

    """
        Metodo che permette di monitorare i cambiamenti alle selezioni sulla combobox
    """
    def selectionchange(self):
        return self.combo_reparti.currentText()

    """
        Metodo che permette di inserire caselle di testo e prelevare il valore all'interno aggiungendolo al dizionario qlines[]
    """
    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    """
        Metodo che permette di effettuare l'aggiunta di un nuovo medico da parte dell'amministratore
        Controllo la validità dell'ID
        Controllo che tutte le caselle siano state riempite
        Controllo che i dati inseriti siano corretti
        Controllo se il CF del medico è già stato registrato
        Controllo se l'ID del medico è già stato registrato
        Se non c'è nulla di errato il medico viene aggiunto ed è visualizzabile nella lista dei medici, altrimenti
        stampo dei pop up di errore con la descrizione dettagliata dell'errore.
    """
    def aggiungi_medico(self):
        # controllo che l'ID sia un numero, except blocca gli errori mostrando un pop up
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
        medico = Medico()

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
            abilitazione = self.qlines["abilitazione"].text()
            id_reparto = int(self.qlines["reparto"].currentText().split(" ")[0].strip())

            # caricamento dei medici in dizionario medici, controllo se l'ID e il CF inseriti sono già utilizzati (se si pop up errore)
            medici = caricaFile("Medici")

            for medico in medici:
                if CF == medico.CF:
                    QMessageBox.critical(self, 'Errore', 'CF già utilizzato', QMessageBox.Ok,
                                         QMessageBox.Ok)
                    return
                if id == medico.id:
                    QMessageBox.critical(self, 'Errore', 'ID già utilizzato', QMessageBox.Ok,
                                         QMessageBox.Ok)
                    return

            # chiamata al metodo setInfoMedico con passaggio parametri per l'aggiunta del medico
            medico.setInfoMedico(id, password, cognome, nome, data_nascita, CF, telefono, genere, mail, indirizzo, nota,
                                 abilitazione, id_reparto)

        except:
            # pop up errore se i dati inseriti non sono corretti
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()
