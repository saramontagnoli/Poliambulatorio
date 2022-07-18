from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from Gestione.GestoreStatistiche import richiediStatisticheMore, richiediStatisticheRicevute


class VistaStatistiche(QWidget):

    def __init__(self):
        super(VistaStatistiche, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))

        v_layout = QVBoxLayout()
        nome = ""
        info = {}

        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_stat_ricevute = QPushButton('Statistiche ricevute')
        btn_stat_ricevute.clicked.connect(lambda: self.stat_ricevute_click())
        v_layout.addWidget(btn_stat_ricevute)

        btn_stat_more = QPushButton('Statistiche more')
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
