from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from Attivita.Referto import Referto


class VistaInserisciReferto(QWidget):

    def __init__(self, prenotazione, callback):
        super(VistaInserisciReferto, self).__init__()
        self.prenotazione = prenotazione
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qlines = {}
        # Casella di testo per inserimento nota referto
        self.add_info_text("nota", "Nota")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.inserisci_referto)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Referto")

    # Prelevo le informazioni scritte nelle caselle di testo
    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    # Aggiunta di un nuovo paziente
    def inserisci_referto(self):

        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return

        # Controllo delle caselle di testo (devono essere tutte riempite)
        try:
            nota = self.qlines["nota"].text()

            Referto(self.prenotazione.id, nota)
            messaggio = QMessageBox()
            messaggio.setWindowIcon(QIcon('CroceVerde.png'))
            messaggio.setWindowTitle("Referto caricato")
            messaggio.setText("Il referto è stato caricato correttamente.")
            messaggio.exec_()

        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()
