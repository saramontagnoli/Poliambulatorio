"""
    Interfaccia grafica per l'inserimento di una nuova prenotazione
"""

from datetime import datetime

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox

from Attivita.Prenotazione import Prenotazione
from Eccezioni.MaxPrenException import MaxPrenException
from Eccezioni.MedicoOccupatoException import MedicoOccupatoException
from Eccezioni.PazienteAssenteException import PazienteAssenteException
from Eccezioni.PazienteOccupatoException import PazienteOccupatoException
from Eccezioni.RepartoMedicoException import RepartoMedicoException
from Eccezioni.WeekEndException import WeekEndException
from Gestione.GestoreFile import caricaFile


class VistaInserisciPrenotazioni(QWidget):
    """
        Costruttore della classe
        Set della finestra dell'inserimento di una nuova prenotazione
        Inserimento caselle di testo per l'inserimento dei dati
        Inserimento button per conferma inserimento
    """

    def __init__(self, callback):
        super(VistaInserisciPrenotazioni, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qlines = {}

        # inserimento caselle di testo mediante metodo add_info_text
        self.add_info_text("id", "Id")
        self.add_info_text("data", "Data (DD/MM/YYYY)")
        self.add_info_text("cf_paziente", "CF Paziente")

        # Inserimento di una combobox per selezionare l'orario della prenotazione e salvataggio nel diz. qlines[] della scelta
        self.combo_ora = QComboBox()

        options = ["8:00", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "14:00", "14:30", "15:00",
                   "15:30", "16:00", "16:30", "17:00", "17:30"]

        for option in options:
            self.combo_ora.addItem(option)

        self.combo_ora.currentIndexChanged.connect(self.selectionchange)
        self.topLabel = QLabel('Ora', self)
        self.v_layout.addWidget(self.topLabel)
        self.qlines["ora"] = self.combo_ora
        self.v_layout.addWidget(self.combo_ora)
        self.setLayout(self.v_layout)

        # caricamento delle visite nel dizionario
        self.visite = caricaFile("Visite")

        # Inserimento di una combobox per selezionare la visita e salvataggio nel diz. qlines[]
        self.combo_visita = QComboBox()

        for visita in self.visite:
            self.combo_visita.addItem(visita.nome)

        self.combo_visita.currentIndexChanged.connect(self.selectionchange)
        self.topLabel = QLabel('Visita', self)
        self.v_layout.addWidget(self.topLabel)
        self.qlines["visita"] = self.combo_visita
        self.v_layout.addWidget(self.combo_visita)
        self.setLayout(self.v_layout)

        # caricamento dei medici nel dizionario
        self.medici = caricaFile("Medici")

        # Inserimento di una combobox per selezionare il medico e salvataggio nel diz. qlines[]
        self.combo_medico = QComboBox()

        for medico in self.medici:
            id_cognome = f"{medico.id} {medico.cognome}"
            self.combo_medico.addItem(id_cognome)

        self.combo_medico.currentIndexChanged.connect(self.selectionchange)
        self.topLabel = QLabel('Medico', self)
        self.v_layout.addWidget(self.topLabel)
        self.qlines["medico"] = self.combo_medico
        self.v_layout.addWidget(self.combo_medico)
        self.setLayout(self.v_layout)

        # inserimento del button di conferma, rimanda all'evento click per l'aggiunta della nuova prenotazione
        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_prenotazione)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuova prenotazione")

    """
        Metodo che permette di monitorare i cambiamenti alle selezioni sulla combobox
    """

    def selectionchange(self):
        return self.combo_visita.currentText()

    """
        Metodo che permette di inserire caselle di testo e prelevare il valore all'interno aggiungendolo al dizionario qlines[]
    """

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    """
        Metodo che permette di effettuare l'aggiunta di una nuova prenotazione da parte dell'amministratore
        Controllo la validità dell'ID
        Controllo che tutte le caselle siano state riempite
        Controllo che i dati inseriti siano corretti
        Controllo se l'ID inserito è già presente nell'archivio
        Gestione degli errori derivanti dal metodo aggiungiPrenotazione
        Se non c'è nulla di errato la prenotazione viene aggiunta ed è visualizzabile nella lista delle prenotazioni, altrimenti
        stampo dei pop up di errore con la descrizione dettagliata dell'errore.
    """

    def aggiungi_prenotazione(self):
        # controllo che l'ID sia un numero, except blocca gli errori mostrando un pop up
        try:
            id = int(self.qlines["id"].text())
        except:
            QMessageBox.critical(self, 'Errore', 'L id non sembra un numero valido.', QMessageBox.Ok, QMessageBox.Ok)
            return

        # controllo che tutte le caselle siano riempite
        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return

        # try-except per il controllo dell'esattezza dei dati
        try:
            data = datetime.strptime(self.qlines["data"].text(), '%d/%m/%Y')
            ora = datetime.strptime(self.qlines["ora"].currentText(), '%H:%M')
            cf_paziente = self.qlines["cf_paziente"].text()
            id_visita = int(self.qlines["visita"].currentIndex()) + 1
            id_medico = int(self.qlines["medico"].currentText().split(" ")[0].strip())
            prenotazioni = caricaFile("Prenotazioni")

            # se l'ID inserito è già utilizzato apro un pop up di errore
            for prenotazione in prenotazioni:

                if id == prenotazione.id:
                    # pop up ID inserito già in uso
                    QMessageBox.critical(self, 'Errore', 'ID già utilizzato', QMessageBox.Ok,
                                         QMessageBox.Ok)
                    return

            # chiamata al metodo aggiungiPrenotazione in Prenotazione, con passaggio parametri
            prenotazione = Prenotazione()
            prenotazione.aggiungiPrenotazione(id, data, ora, id_medico, id_visita, cf_paziente)

            """
                Restituzione degli errori dal metodo aggiungiPrenotazione:
                    - EXCEPTION: Il codice fiscale non è nell'archivio
                    - EXCEPTION: Il reparto del medico e il reparto della visita non corrispondono
                    - EXCEPTION: Il medico ha già una visita nella data e ora scelte
                    - EXCEPTION: Non si può prenotare una visita durante il weekend (sabato, domenica)
                    - EXCEPTION: Il paziente ha già prenotato una visita in quella stessa data e ora
                    - EXCEPTION: Il paziente ha troppe prenotazioni attive al momento (non può averne 5 o +)
                Per ogni controllo di errore viene aperto un pop-up relativo con la scrittura del messaggio
            """
        except PazienteAssenteException:
            QMessageBox.critical(self, 'Errore', 'Codice fiscale non valido',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

            # sto scegliendo una visita e un medico di reparti diversi
        except RepartoMedicoException:
            QMessageBox.critical(self, 'Errore', 'Il reparto del medico e della visita non corrispondono',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

            # il medico ha già un'altra visita
        except MedicoOccupatoException:
            QMessageBox.critical(self, 'Errore', 'Il medico è già impegnato in un''altra visita',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

            # sto prenotando di sabato o domenica
        except WeekEndException:
            QMessageBox.critical(self, 'Errore', 'Il sabato e la domenica l''ambulatorio è chiuso',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        except PazienteOccupatoException:
            QMessageBox.critical(self, 'Errore',
                                 'Il paziente ha già prenotato per un''altra visita in questa data e ora',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        except MaxPrenException:
            QMessageBox.critical(self, 'Errore', 'Il paziente ha troppe prenotazioni attive al momento',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        self.callback()
        self.close()
