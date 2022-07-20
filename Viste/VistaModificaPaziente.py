from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox


class VistaModificaPaziente(QWidget):

    def __init__(self, paziente):

        super(VistaModificaPaziente, self).__init__()
        self.paziente = paziente
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.v_layout = QVBoxLayout()
        self.qlines = {}

        # Caselle di testo per inserimento informazioni del medico
        self.add_info_text("password", "Password")
        self.add_info_text("mail", "Email")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("indirizzo", "Indirizzo")
        self.add_info_text("nota", "Nota")
        self.add_checkbox("allergia", "Allergia")
        self.add_checkbox("malattia_pregressa", "Malattia pregressa")

        btn_ok = QPushButton("Modifica")
        btn_ok.clicked.connect(self.modifica_paziente)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica paziente")

    # Prelevo le informazioni scritte nelle caselle di testo
    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def add_checkbox(self, nome, label):
        self.checkbox = QCheckBox(label, self)
        self.checkbox.resize(320, 40)
        self.qlines[nome] = self.checkbox
        self.v_layout.addWidget(self.checkbox)
        self.checkbox.stateChanged.connect(self.clickBox)

    def clickBox(self, state):
        if state == QtCore.Qt.Checked:
            return True
        else:
            return False

    # Aggiunta di un nuovo medico
    def modifica_paziente(self):

        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return

        # Controllo delle caselle di testo (devono essere tutte riempite)
        try:
            password = self.qlines["password"].text()
            mail = self.qlines["mail"].text()
            telefono = self.qlines["telefono"].text()
            indirizzo = self.qlines["indirizzo"].text()
            nota = self.qlines["nota"].text()
            allergia = self.qlines["allergia"].text()
            malattia_pregressa = self.qlines["malattia_pregressa"].text()

            self.paziente.setInfoPaziente(self.paziente.id, self.paziente.nome, self.paziente.cognome, password,
                                          self.paziente.data_nascita, self.paziente.CF, telefono, self.paziente.genere,
                                          mail, indirizzo, nota, allergia, malattia_pregressa)
            messaggio = QMessageBox()
            messaggio.setWindowIcon(QIcon('CroceVerde.png'))
            messaggio.setWindowTitle("Modifica informazioni")
            messaggio.setText("Modifica effettuata")
            messaggio.exec_()

        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        self.close()
