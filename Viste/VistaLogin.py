from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QSizePolicy)


class VistaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.resize(350, 200)
        grid_layout = QGridLayout()
        label1 = QLabel('<font size="8"> UserId </font>')
        self.user_obj = QLineEdit()
        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(self.user_obj, 0, 1)
        label2 = QLabel('<font size="8"> Password </font>')
        self.user_pwd = QLineEdit()
        # impostazioni della visibilita password
        self.user_pwd.setEchoMode(QLineEdit.Password)
        grid_layout.addWidget(label2, 1, 0)
        grid_layout.addWidget(self.user_pwd, 1, 1)
        # salvataggio in stringa
        password = self.user_pwd.text()
        print("Password: "+password)
        grid_layout.addWidget(self.get_generic_button("Login", self.go_login, password), 2, 0, 2, 2)
        self.setLayout(grid_layout)

    # Funzionalità del bottone
    def get_generic_button(self, titolo, on_click, password):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(lambda: on_click(password))
        return button

    def go_login(self, password):
        print(str(password))
