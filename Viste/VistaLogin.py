"""
    Interfaccia grafica per la vista del form di login per l'accesso alla piattaforma
    Ci sono due caselle di testo per inserimento di username e password e un tasto d'invio
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QSizePolicy, QMessageBox

from Gestione.GestoreAccesso import GestoreAccesso

"""
    Metodo che inserisce il button e collega l'evento on_click
"""


def get_generic_button(titolo, on_click):
    button = QPushButton(titolo)
    button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    button.clicked.connect(on_click)
    return button


class VistaLogin(QWidget):
    """
        Costruttore della classe
        Si effettuano tutti i set di icone, size, titolo della finestra e visualizzazione
        Inserimento di due caselle di testo per l'inserimento di username e password, e di un tasto d'invio
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.resize(350, 200)
        grid_layout = QGridLayout()

        # inserimento di label e caselle di testo per username e password
        label1 = QLabel('<font size="8"> UserId </font>')
        self.user_obj = QLineEdit(self)
        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(self.user_obj, 0, 1)
        label2 = QLabel('<font size="8"> Password </font>')
        self.user_pwd = QLineEdit(self)

        # impostazioni della visibilita password
        self.user_pwd.setEchoMode(QLineEdit.Password)
        grid_layout.addWidget(label2, 1, 0)
        grid_layout.addWidget(self.user_pwd, 1, 1)

        # inserimento di un generic button e relativo evento click
        grid_layout.addWidget(get_generic_button("Login", self.go_login), 2, 0, 2, 2)
        self.setLayout(grid_layout)

    """
        Metodo per evento del click al button Login
        Questo evento salva username e password inseriti nelle caselle di testo e richiama il GestoAccesso per 
        controllare quale utente sta tentando di eseguire l'accesso
        Se username o password sono errati si apre un pop up di errore, altrimenti tramite il GestoreAccesso si aprirà
        la vista relativa all'utente che vuole accedere
    """

    def go_login(self):
        username = self.user_obj.text()
        password = self.user_pwd.text()
        # controllo se riesco ad effettuare il login mediante il metodo login
        if not GestoreAccesso.login(self, username, password):
            QMessageBox.critical(self, 'Errore', 'Codice fiscale o password errati.', QMessageBox.Ok, QMessageBox.Ok)
            return

        self.close()
