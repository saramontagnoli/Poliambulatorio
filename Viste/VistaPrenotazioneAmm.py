"""
    Interfaccia grafica per la visualizzazione delle informazioni della prenotazione e gli eventuali button
    per la disdetta della prenotazione, visualizzazione della ricevuta, del referto e della mora LATO ADMIN
    La classe figlia eredita i metodi e attributi dalla classe padre VistaPrenotazione
    (ereditarietà)
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from Attivita.Prenotazione import Prenotazione
from Gestione.GestoreFile import caricaFile
from Viste.VistaPrenotazione import VistaPrenotazione


class VistaPrenotazioneAmm(VistaPrenotazione):
    """
        Costruttore della classe figlia
        Set della finestra della visualizzazione della prenotazione lato admin
        Inserimento di tutte le informazioni della prenotazione con delle label
        Se le variabili boolean sono True stampa il campo: SI, altrimenti non stampa il campo
        Inserimento dei button di creazione o visualizzazione ricevuta (in base ai controlli effettuati)
        Inserimento del button di una eventuale mora (se esiste nel file More)
        Inserimento del button di disdetta della prenotazione (in base ai controlli effettuati)
    """

    def __init__(self, prenotazione, elimina_callback):
        super(VistaPrenotazione, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.elimina_callback = elimina_callback
        self.utente = "admin"
        v_layout = QVBoxLayout()
        nome = ""
        info = {}

        # carico le informazioni della prenotazione
        if isinstance(prenotazione, Prenotazione):
            nome = f"Prenotazione {prenotazione.id}"
            info = prenotazione.getInfoPrenotazione()

        # inserimento delle label contenenti le informazioni della prenotazione
        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(QLabel(f"Id: {info['id']}"))
        v_layout.addWidget(QLabel(f"Data: {info['data'].strftime('%Y-%m-%d')}"))
        v_layout.addWidget(QLabel(f"Ora: {info['ora'].strftime('%H:%M')}"))
        v_layout.addWidget(QLabel(f"CF Paziente: {info['cf_paziente']}"))
        v_layout.addWidget(QLabel(f"Id medico: {info['id_medico']}"))
        v_layout.addWidget(QLabel(f"Id visita: {info['id_visita']}"))

        # controllo stampe variabili boolean
        if bool(info['scaduta']):
            v_layout.addWidget(QLabel(f"Scaduta: Si"))

        if bool(info['disdetta']):
            v_layout.addWidget(QLabel(f"Disdetta: Si"))

        if bool(info['conclusa']):
            v_layout.addWidget(QLabel(f"Conclusa: Si"))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # se la prenotazione è ancora attiva inserisco il button Crea ricevuta
        if not prenotazione.conclusa and not prenotazione.disdetta and not prenotazione.scaduta:
            btn_crea_ricevuta = QPushButton('Crea ricevuta')
            btn_crea_ricevuta.clicked.connect(lambda: self.crea_ricevuta_click(prenotazione))
            v_layout.addWidget(btn_crea_ricevuta)
        elif prenotazione.conclusa:
            # se la prenotazione è già conclusa e la visita è stata effettuata permetto di visualizzarne la ricevuta
            btn_visualizza_ricevuta = QPushButton('Visualizza ricevuta')
            btn_visualizza_ricevuta.clicked.connect(lambda: self.visualizza_ricevuta_click(prenotazione))
            v_layout.addWidget(btn_visualizza_ricevuta)

        # se la prenotazione ha collegata una mora inserisco il button Visualizza mora che rimanda al metodo di visualizzazione mora
        more = caricaFile("More")
        for mora in more:
            if mora.id == prenotazione.id:
                btn_visualizza_mora = QPushButton('Visualizza mora')
                btn_visualizza_mora.clicked.connect(lambda: self.visualizza_mora_click(mora))
                v_layout.addWidget(btn_visualizza_mora)

        # se la prenotazione non è ancora conclusa o scaduta o già disdetta, inserisco il button per la disdetta che rimanda al metodo di disdetta
        if not prenotazione.conclusa and not prenotazione.scaduta and not prenotazione.disdetta:
            btn_disdici = QPushButton('Disdici')
            btn_disdici.clicked.connect(lambda: self.disdetta_prenotazione_click(prenotazione))
            v_layout.addWidget(btn_disdici)

        self.setLayout(v_layout)
        self.setWindowTitle("Prenotazione")

    """
        Metodo che implementa l'evento click per la creazione di una ricevuta (chiamata al metodo creaRicevuta in Prenotazione).
        Se la creazione è andata a buon fine mando un pop up di successo, altrimenti un pop up di errore
    """

    def crea_ricevuta_click(self, prenotazione):
        if isinstance(prenotazione, Prenotazione):
            messaggio = QMessageBox()

            # controllo l'esito della creazione della ricevuta
            if prenotazione.crea_ricevuta():
                # pop up di successo
                messaggio.setWindowTitle("Ricevuta")
                messaggio.setText("La Ricevuta della prenotazione e' stata creata con successo. ")
                messaggio.exec_()
            else:
                # pop up di errore
                messaggio.setWindowTitle("Errore")
                messaggio.setText("Impossibile creare la ricevuta. ")
                messaggio.exec_()
        self.elimina_callback()
        self.close()
