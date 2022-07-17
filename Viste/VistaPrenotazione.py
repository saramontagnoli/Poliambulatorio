from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox


from Attivita.Prenotazione import Prenotazione


class VistaPrenotazione(QWidget):

    def __init__(self, prenotazione, elimina_callback):
        super(VistaPrenotazione, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()
        nome = ""
        info = {}

        if isinstance(prenotazione, Prenotazione):
            nome = f"Prenotazione {prenotazione.id}"
            info = prenotazione.getInfoPrenotazione()

        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Si scrivono i vari dati della prenotazione selezionato
        v_layout.addWidget(QLabel(f"Id: {info['id']}"))
        v_layout.addWidget(QLabel(f"Data: {info['data'].strftime('%Y-%m-%d')}"))
        v_layout.addWidget(QLabel(f"Ora: {info['ora'].strftime('%H:%M')}"))
        v_layout.addWidget(QLabel(f"CF Paziente: {info['cf_paziente']}"))
        v_layout.addWidget(QLabel(f"Id medico: {info['id_medico']}"))
        v_layout.addWidget(QLabel(f"Id visita: {info['id_visita']}"))

        # Eventuali stampe degli stati della prenotazione
        if bool(info['scaduta']):
            v_layout.addWidget(QLabel(f"Scaduta: Si"))

        if bool(info['disdetta']):
            v_layout.addWidget(QLabel(f"Disdetta: Si"))

        if bool(info['conclusa']):
            v_layout.addWidget(QLabel(f"Conclusa: Si"))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Creazione del bottone per disdire la prenotazione che si sta visualizzando
        btn_ricevuta = QPushButton('Crea ricevuta')
        btn_ricevuta.clicked.connect(lambda: self.crea_ricevuta_click(prenotazione))
        btn_disdici = QPushButton('Disdici')
        btn_disdici.clicked.connect(lambda: self.disdetta_prenotazione_click(prenotazione))
        v_layout.addWidget(btn_ricevuta)
        v_layout.addWidget(btn_disdici)

        self.setLayout(v_layout)
        self.setWindowTitle("Prenotazione")

    # Funzione per l'eliminazione della prenotazione selezionato quando si preme il bottone
    def disdetta_prenotazione_click(self, prenotazione):
        if isinstance(prenotazione, Prenotazione):
            messaggio = QMessageBox()
            if(prenotazione.disdiciPrenotazione()):
                messaggio.setWindowTitle("Disdetta")
                messaggio.setText("La prenotazione e' stato disdetta con successo. ")
                messaggio.exec_()
            else:
                messaggio.setWindowTitle("Errore")
                messaggio.setText("La prenotazione e' gia' stata disdetta. ")
                messaggio.exec_()
        self.elimina_callback()
        self.close()

    def crea_ricevuta_click(self, prenotazione):
        if isinstance(prenotazione,Prenotazione):
            messaggio = QMessageBox()
            if(prenotazione.crea_ricevuta()):
                messaggio.setWindowTitle("Ricevuta")
                messaggio.setText("La Ricevuta della prenotazione e' stata creata con successo. ")
                messaggio.exec_()
            else:
                messaggio.setWindowTitle("Errore")
                messaggio.setText("Impossibile creare la ricevuta. ")
                messaggio.exec_()
        self.elimina_callback()
        self.close()

