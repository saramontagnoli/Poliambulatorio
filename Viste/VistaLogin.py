from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout)


class VistaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.resize(350, 200)
        layout = QGridLayout()
        label1 = QLabel('<font size="8"> UserId </font>')
        self.user_obj = QLineEdit()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.user_obj, 0, 1)
        label2 = QLabel('<font size="8"> Password </font>')
        self.user_pwd = QLineEdit()
        # impostazioni della visibilita password
        self.user_pwd.setEchoMode(QLineEdit.Password)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.user_pwd, 1, 1)
        button_login = QPushButton('Login')
        layout.addWidget(button_login, 2, 0, 2, 2)
        self.setLayout(layout)
