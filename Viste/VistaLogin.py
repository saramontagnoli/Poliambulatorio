from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QSizePolicy, QMessageBox

from Gestione.GestoreAccesso import GestoreAccesso


class VistaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.resize(350, 200)
        grid_layout = QGridLayout()
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
        grid_layout.addWidget(self.get_generic_button("Login", self.go_login), 2, 0, 2, 2)
        self.setLayout(grid_layout)

    # Funzionalità del pulsante di Login
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    # Rimando al controllo username e pwd per il login
    def go_login(self):
        username = self.user_obj.text()
        password = self.user_pwd.text()
        # Forse togliere self
        if not GestoreAccesso.login(self, username, password):
            QMessageBox.critical(self, 'Errore', 'Codice fiscale o password errati.', QMessageBox.Ok, QMessageBox.Ok)
            return

        self.close()
