from datetime import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from Attivita.Paziente import Paziente


class VistaInserisciPazienti(QWidget):

    def __init__(self, callback):
        super(VistaInserisciPazienti, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qlines = {}
        # self.add_info_text("id", "Id")
        self.add_info_text("password", "Password")
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("data_nascita", "Data Nascita")
        self.add_info_text("CF", "Codice Fiscale")
        self.add_info_text("mail", "Email")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("genere", "Genere")
        self.add_info_text("indirizzo", "Indirizzo")
        self.add_info_text("nota", "Nota")
        self.add_info_text("allergia", "Allergia")
        self.add_info_text("malattia_pregressa", "Malattia pregressa")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_paziente)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo paziente")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def aggiungi_paziente(self):
        """try:
            id = int(self.qlines["id"].text())
        except:
            QMessageBox.critical(self, 'Errore', 'L id non sembra un numero valido.', QMessageBox.Ok, QMessageBox.Ok)
            return """
        print("Inizio di aggiungi paziente?? OK")
        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return
        print("Sto per creare il paziente? Si ma No")
        paziente = Paziente()
        print("Paziente inizializzato? NO")
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
            allergia = self.qlines["allergia"].text()
            malattia_pregressa = self.qlines["malattia_pregressa"].text()

            print("Dati inseriti?")
            paziente.setInfoPaziente(self, nome, cognome, password, data_nascita, CF, telefono, genere, mail, indirizzo, nota,
                                     allergia, malattia_pregressa)
            print(paziente)
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()
