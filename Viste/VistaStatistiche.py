"""
    Interfaccia grafica per la gestione delle richieste delle statistiche su ricevute e more
    La vista permette di vedere due button Statistiche Ricevute e Statistiche More
    Al click si aprirà un pop up contenente tutte le informazioni delle statistiche richieste
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox

from Gestione.GestoreStatistiche import richiediStatisticheMore, richiediStatisticheRicevute

"""
     Evento del click al button Richiedi Statistiche Ricevute
     Mostra un pop up che contiene tutte le informazioni delle statistiche
 """


def stat_ricevute_click():
    # pop up che contiene le statistiche sulle ricevute, tramite chiamata a GestoreStatistiche
    messaggio = QMessageBox()
    messaggio.setWindowIcon(QIcon('CroceVerde.png'))
    messaggio.setWindowTitle("Statistiche Ricevute")
    messaggio.setText(richiediStatisticheRicevute())
    messaggio.exec_()
    return


"""
    Evento del click al button Richiedi Statistiche More
    Mostra un pop up che contiene tutte le informazioni delle statistiche
"""


def stat_more_click():
    # pop up che contiene le statistiche sulle more, tramite chiamata a GestoreStatistiche
    messaggio = QMessageBox()
    messaggio.setWindowIcon(QIcon('CroceVerde.png'))
    messaggio.setWindowTitle("Statistiche More")
    messaggio.setText(richiediStatisticheMore())
    messaggio.exec_()


class VistaStatistiche(QWidget):
    """
        Costruttore della classe
        Si effettuano tutti i set di icone, size, titolo della finestra e visualizzazione
        Inserimento di due button che rimandano a:
            -statistiche sulle more (button Statistiche more)
            -statistiche sulle ricevute (button Statistiche ricevute)
        Entrambi i button richiamo due funzioni tramite lambda al click
    """

    def __init__(self):
        super(VistaStatistiche, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.setGeometry(0, 0, 300, 300)
        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignCenter)

        # button per richiedere statistiche sulle ricevute e relativo evento click
        btn_stat_ricevute = QPushButton('Statistiche ricevute')
        btn_stat_ricevute.clicked.connect(lambda: stat_ricevute_click())
        btn_stat_ricevute.setFixedSize(300, 100)
        v_layout.addWidget(btn_stat_ricevute)

        # button per richiedere statistiche sulle more e relativo evento click
        btn_stat_more = QPushButton('Statistiche more')
        btn_stat_more.setFixedSize(300, 100)
        btn_stat_more.clicked.connect(lambda: stat_more_click())
        v_layout.addWidget(btn_stat_more)

        self.setLayout(v_layout)
        self.setWindowTitle("Statistiche")
