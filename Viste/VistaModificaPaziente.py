"""
    Interfaccia grafica per la modifica delle informazioni del paziente
"""

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox

"""
      Metodo che controlla lo stato della checkbox (selezionata o no)
  """


def clickBox(state):
    if state == QtCore.Qt.Checked:
        return True
    else:
        return False


class VistaModificaPaziente(QWidget):
    """
        Costruttore della classe
        Set della finestra della modifica del paziente
        Inserimento caselle di testo per la modifica dei dati
        Inserimento button per conferma modifica
    """

    def __init__(self, paziente):

        super(VistaModificaPaziente, self).__init__()
        self.checkbox = None
        self.paziente = paziente
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.v_layout = QVBoxLayout()
        self.qlines = {}

        # inserimento caselle di testo mediante metodo add_info_text
        self.add_info_text("password", "Password")
        self.add_info_text("mail", "Email")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("indirizzo", "Indirizzo")
        self.add_info_text("nota", "Nota")
        self.add_checkbox("allergia", "Allergia")
        self.add_checkbox("malattia_pregressa", "Malattia pregressa")

        # inserimento button modifica, rimando all'evento click
        btn_ok = QPushButton("Modifica")
        btn_ok.clicked.connect(self.modifica_paziente)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica paziente")

    """
        Metodo che permette di inserire caselle di testo e prelevare il valore all'interno aggiungendolo al dizionario qlines[]
    """

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    """
        Metodo che permette di inserire checkbox e prelevare il valore aggiungendolo al dizionario qlines[]
    """

    def add_checkbox(self, nome, label):
        self.checkbox = QCheckBox(label, self)
        self.checkbox.resize(320, 40)
        self.qlines[nome] = self.checkbox
        self.v_layout.addWidget(self.checkbox)
        self.checkbox.stateChanged.connect(clickBox)

    """
        Metodo che permette di effettuare la modifica delle informazioni del paziente
        Controllo che tutte le caselle siano state riempite
        Se sono corrette le informazioni richiamo il metodo di setInfoPaziente per apportare le modifiche
        Non tutti i parametri possono essere cambiati.
        Il try-except blocca gli input errati mostrando un pop up di errore
        Se la modifica è stata portata a termine correttamente apparirà un pop up di successo
    """

    def modifica_paziente(self):
        # controllo che tutte le caselle siano state riempite
        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return

        # try-except per il controllo dell'esattezza dei dati
        try:
            password = self.qlines["password"].text()
            mail = self.qlines["mail"].text()
            telefono = self.qlines["telefono"].text()
            indirizzo = self.qlines["indirizzo"].text()
            nota = self.qlines["nota"].text()
            allergia = self.qlines["allergia"].text()
            malattia_pregressa = self.qlines["malattia_pregressa"].text()

            """
                Richiamo il metodo di setInfoPaziente, le informazioni che non posso essere cambiate vengono passate uguali, mentre
                le informazioni cambiate vengono passate al costruttore
            """
            self.paziente.setInfoPaziente(self.paziente.id, self.paziente.nome, self.paziente.cognome, password,
                                          self.paziente.data_nascita, self.paziente.CF, telefono, self.paziente.genere,
                                          mail, indirizzo, nota, allergia, malattia_pregressa)

            # pop up di avvenuta modifica
            messaggio = QMessageBox()
            messaggio.setWindowIcon(QIcon('CroceVerde.png'))
            messaggio.setWindowTitle("Modifica informazioni")
            messaggio.setText("Modifica effettuata")
            messaggio.exec_()

        except:
            # pop up di errore se le informazioni inserite sono sbagliate
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        self.close()
