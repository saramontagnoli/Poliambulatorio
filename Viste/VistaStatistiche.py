from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from Gestione.GestoreStatistiche import richiediStatisticheMore, richiediStatisticheRicevute


class VistaStatistiche(QWidget):

    def __init__(self):
        super(VistaStatistiche, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.setGeometry(0, 0, 300, 300)

        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignCenter)
        btn_stat_ricevute = QPushButton('Statistiche ricevute')
        btn_stat_ricevute.clicked.connect(lambda: self.stat_ricevute_click())
        btn_stat_ricevute.setFixedSize(300, 100)
        v_layout.addWidget(btn_stat_ricevute)

        btn_stat_more = QPushButton('Statistiche more')
        btn_stat_more.setFixedSize(300, 100)
        btn_stat_more.clicked.connect(lambda: self.stat_more_click())
        v_layout.addWidget(btn_stat_more)

        self.setLayout(v_layout)
        self.setWindowTitle("Prenotazione")

    def stat_ricevute_click(self):
        messaggio = QMessageBox()
        messaggio.setWindowIcon(QIcon('CroceVerde.png'))
        messaggio.setWindowTitle("Statistiche Ricevute")
        messaggio.setText(richiediStatisticheRicevute())
        messaggio.exec_()
        return

    def stat_more_click(self):
        messaggio = QMessageBox()
        messaggio.setWindowIcon(QIcon('CroceVerde.png'))
        messaggio.setWindowTitle("Statistiche More")
        messaggio.setText(richiediStatisticheMore())
        messaggio.exec_()
