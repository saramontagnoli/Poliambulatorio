from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from Attivita.Prenotazione import Prenotazione
from Gestione.GestoreFile import caricaFile
from Viste.VistaPrenotazione import VistaPrenotazione


class VistaPrenotazioneAmm(VistaPrenotazione):

    def __init__(self, prenotazione, elimina_callback):
        super(VistaPrenotazione, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.elimina_callback = elimina_callback
        self.utente = "admin"

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
        if not prenotazione.conclusa and not prenotazione.disdetta and not prenotazione.scaduta:
            btn_crea_ricevuta = QPushButton('Crea ricevuta')
            btn_crea_ricevuta.clicked.connect(lambda: self.crea_ricevuta_click(prenotazione))
            v_layout.addWidget(btn_crea_ricevuta)
        elif prenotazione.conclusa:
            btn_visualizza_ricevuta = QPushButton('Visualizza ricevuta')
            btn_visualizza_ricevuta.clicked.connect(lambda: self.visualizza_ricevuta_click(prenotazione))
            v_layout.addWidget(btn_visualizza_ricevuta)

        more = caricaFile("More")

        for mora in more:
            if mora.id == prenotazione.id:
                btn_visualizza_mora = QPushButton('Visualizza mora')
                btn_visualizza_mora.clicked.connect(lambda: self.visualizza_mora_click(mora))
                v_layout.addWidget(btn_visualizza_mora)

        if not prenotazione.conclusa and not prenotazione.scaduta and not prenotazione.disdetta:
            btn_disdici = QPushButton('Disdici')
            btn_disdici.clicked.connect(lambda: self.disdetta_prenotazione_click(prenotazione))
            v_layout.addWidget(btn_disdici)

        self.setLayout(v_layout)
        self.setWindowTitle("Prenotazione")

    # Funzione per la creazione della ricevuta quando si preme il bottone
    def crea_ricevuta_click(self, prenotazione):
        if isinstance(prenotazione, Prenotazione):
            messaggio = QMessageBox()
            if prenotazione.crea_ricevuta():
                messaggio.setWindowTitle("Ricevuta")
                messaggio.setText("La Ricevuta della prenotazione e' stata creata con successo. ")
                messaggio.exec_()
            else:
                messaggio.setWindowTitle("Errore")
                messaggio.setText("Impossibile creare la ricevuta. ")
                messaggio.exec_()
        self.elimina_callback()
        self.close()
