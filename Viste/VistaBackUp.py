from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox, QLabel, QLineEdit, QComboBox
from Gestione.GestoreBackUp import GestoreBackUp


class VistaBackUp(QWidget):

    def __init__(self):
        super(VistaBackUp, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.setGeometry(0, 0, 300, 300)

        self.v_layout = QVBoxLayout()
        self.v_layout.setAlignment(Qt.AlignCenter)
        self.qlines = {}

        self.add_info_text("ora", "Nuovo orario")

        # Combo box lista orari dell'ambulatorio
        # Creazione e riempimento con le visite della combobox
        self.combo_frequenza = QComboBox()
        options = ["1", "2", "3", "4", "5", "6", "7"]

        for option in options:
            self.combo_frequenza.addItem(option)

        self.combo_frequenza.currentIndexChanged.connect(self.selectionchange)
        self.qlines["frequenza"] = self.combo_frequenza
        self.v_layout.addWidget(self.combo_frequenza)

        btn_ok = QPushButton('Invio')
        btn_ok.clicked.connect(lambda: self.modifica_click())
        btn_ok.setFixedSize(300, 100)
        self.v_layout.addWidget(btn_ok)

        btn_backup = QPushButton('Esegui Back-up adesso')
        btn_backup.setFixedSize(300, 100)
        btn_backup.clicked.connect(lambda: self.backup_click())
        self.v_layout.addWidget(btn_backup)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Back-up")

        # Prelevo le informazioni scritte nelle caselle di testo

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def selectionchange(self):
        return self.combo_frequenza.currentText()

    def modifica_click(self):
        gb = GestoreBackUp()
        try:
            ora = datetime.strptime(self.qlines["ora"].text(), '%H:%M')
            frequenza = int(self.qlines["frequenza"].currentIndex() + 1)
            gb.modificaBackUp(ora, frequenza)
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        messaggio = QMessageBox()
        messaggio.setWindowIcon(QIcon('CroceVerde.png'))
        messaggio.setWindowTitle("Modifica")
        messaggio.setText('Orario e frequenza di back-up modificati con successo')
        messaggio.exec_()
        return

    def backup_click(self):
        return
