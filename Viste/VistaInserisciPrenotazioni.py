from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

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
        self.add_info_text("ora", "Ora")


        self.combo_visita = QComboBox(self)

        visite = {}
        if os.path.isfile('File/Visite.pickle'):
            with open('File/Visite.pickle', 'rb') as f:
                visite = dict(pickle.load(f))

        for visita in visite:
            combo_visita.addItem(visita.nome)

        self.v_layout.addWidget(QLabel("visita"))
        self.combo_visita.activated[str].connect(self.onChanged)

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_prenotazione)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuova prenotazione")


    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()

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
            prenotazione.aggiungiPrenotazione(id, data, ora)
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()
