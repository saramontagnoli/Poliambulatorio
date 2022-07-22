"""
    Interfaccia grafica per l'inserimento di un nuovo referto
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from Attivita.Referto import Referto


class VistaInserisciReferto(QWidget):
    """
        Costruttore della classe
        Set della finestra dell'inserimento di un nuovo referto
        Inserimento caselle di testo per l'inserimento della nota del referto
        Inserimento button per conferma inserimento referto
    """
    def __init__(self, prenotazione, callback):
        super(VistaInserisciReferto, self).__init__()
        self.prenotazione = prenotazione
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qlines = {}

        # inserimento caselle di testo mediante metodo add_info_text
        self.add_info_text("nota", "Nota")

        # inserimento del button di conferma, rimanda all'evento click per l'aggiunta del nuovo referto
        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.inserisci_referto)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Referto")

    """
        Metodo che permette di inserire caselle di testo e prelevare il valore all'interno aggiungendolo al dizionario qlines[]
    """
    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    """
        Metodo che permette di effettuare l'aggiunta di un nuovo referto per una visita da parte del medico
        Controllo che tutte le caselle siano state riempite
        Controllo che i dati inseriti siano corretti
        Se non c'è nulla di errato il referto viene aggiunto ed è visualizzabile nella finestra della prenotazione corrispondente, altrimenti
        stampo dei pop up di errore con la descrizione dettagliata dell'errore.
    """
    def inserisci_referto(self):

        # controllo che tutte le caselle siano riempite
        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return

        # try-except per il controllo dell'esattezza dei dati
        try:
            nota = self.qlines["nota"].text()

            # chiamata al costruttore Referto per l'inserimento di un nuovo referto
            Referto(self.prenotazione.id, nota)
            messaggio = QMessageBox()
            messaggio.setWindowIcon(QIcon('CroceVerde.png'))
            messaggio.setWindowTitle("Referto caricato")
            # pop up di avvenuta creazione del referto
            messaggio.setText("Il referto è stato caricato correttamente.")
            messaggio.exec_()

        except:
            # pop up errore se i dati inseriti non sono corretti
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()
