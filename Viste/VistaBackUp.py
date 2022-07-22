"""
    Interfaccia grafica per la gestione del backup da parte dell'admin della piattaforma
    La vista permette di vedere una casella di testo e una combo box per la modifica delle impostazioni del backup
    La vista, inoltre, ha un button che permette di eseguire il backup in maniera immediata
"""

from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox, QLabel, QLineEdit, QComboBox
from Gestione.GestoreBackUp import GestoreBackUp, effettuaBackUp


"""
    Evento del click al button Esegui Backup Adesso
    Effettua il backup richiamante il metodo effettua backup
    Mostra un pop up che segnala il completamento del backup
"""
def backup_click():
    effettuaBackUp()

    messaggio = QMessageBox()
    messaggio.setWindowIcon(QIcon('CroceVerde.png'))
    messaggio.setWindowTitle("Completato")
    messaggio.setText('Back-up completato.')
    messaggio.exec_()
    return


class VistaBackUp(QWidget):
    """
        Costruttore della classe
        Si effettuano tutti i set di icone, size, titolo della finestra e visualizzazione
        Inserimento di una casella di testo per l'inserimento dell'ora, una combobox per la periodicità del backup e il button di conferma
        Inserimento di un button per il backup immediato
        Ad ogni button corrisponde un evento click definito nella lambda:
            - se clicco invio e ho inserito i dati correttamente avrò l'aggiornamento del file contenente le impostazioni del backup
            - se clicco Esegui Backup Adesso avrò l'avvio del backup e un package con la copia di tutti i file dei dati
    """
    def __init__(self):
        super(VistaBackUp, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.setGeometry(0, 0, 300, 300)

        self.v_layout = QVBoxLayout()
        self.v_layout.setAlignment(Qt.AlignCenter)
        self.qlines = {}

        self.gb = GestoreBackUp()

        # casella di testo e combo box per modificare le impostazioni del backup
        self.add_info_text("ora", "Nuovo orario (HH:MM)")
        self.combo_frequenza = QComboBox()
        options = ["1", "2", "3", "4", "5", "6", "7"]

        for option in options:
            self.combo_frequenza.addItem(option)

        self.combo_frequenza.currentIndexChanged.connect(self.selectionchange)
        self.qlines["frequenza"] = self.combo_frequenza
        self.v_layout.addWidget(self.combo_frequenza)

        # button della modifica delle impostazioni del backup
        btn_ok = QPushButton('Invio')
        btn_ok.clicked.connect(lambda: self.modifica_click())
        btn_ok.setFixedSize(300, 100)
        self.v_layout.addWidget(btn_ok)

        # button dell'esecuzione immediata del backup
        btn_backup = QPushButton('Esegui Back-up adesso')
        btn_backup.setFixedSize(300, 100)
        btn_backup.clicked.connect(lambda: backup_click())
        self.v_layout.addWidget(btn_backup)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Back-up")


    """
        Metodo che permette di inserire caselle di testo e prelevare il valore all'interno aggiungendolo al dizionario qlines[]
    """
    def add_info_text(self, nome, label):
        # aggiunta label e casella di testo
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        # aggiunta del valore al dizionario qlines[]
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    """
        Metodo che permette di tenere traccia dei cambiamenti di selezione nella combobox della periodicità del backup
    """
    def selectionchange(self):
        return self.combo_frequenza.currentText()


    """
        Metodo che permette di effettuare la modifica delle impostazioni del backup dei dati
        Controllo dell'esattezza dei parametri inseriti tramite la vista
        Se sono corretti richiamo il metodo di modificaBackup, portando a termine la modifica
        Altrimenti il try-except bloccherà gli input errati mostrando un pop up di errore
        Se la modifica è stata portata a termine invece apparirà un pop up di successo
    """
    def modifica_click(self):
        # try-except per il controllo di ora e frequenza
        try:
            ora = datetime.strptime(self.qlines["ora"].text(), '%H:%M')
            frequenza = int(self.qlines["frequenza"].currentIndex() + 1)

            # richiamo al metodo di modifica dati backup
            self.gb.modificaBackUp(ora, frequenza)
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        # pop up di avvenuta modifica delle impostazioni di backup
        messaggio = QMessageBox()
        messaggio.setWindowIcon(QIcon('CroceVerde.png'))
        messaggio.setWindowTitle("Modifica")
        messaggio.setText('Orario e frequenza di back-up modificati con successo')
        messaggio.exec_()
        return
