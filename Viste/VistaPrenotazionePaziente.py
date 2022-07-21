"""
    Interfaccia grafica per la visualizzazione delle informazioni della prenotazione e gli eventuali button
    per la disdetta della prenotazione, visualizzazione di referto, ricevuta e mora LATO PAZIENTE
    La classe figlia eredita i metodi e attributi dalla classe padre VistaPrenotazione
    (ereditarietà)
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from Attivita.Prenotazione import Prenotazione
from Gestione.GestoreFile import caricaFile
from Viste.VistaPrenotazione import VistaPrenotazione


class VistaPrenotazionePaziente(VistaPrenotazione):
    """
        Costruttore della classe figlia
        Set della finestra della visualizzazione della prenotazione lato medico
        Inserimento di tutte le informazioni della prenotazione con delle label
        Se le variabili boolean sono True stampa il campo: SI, altrimenti non stampa il campo
        Inserimento dei button di visualizzazione referto, mora e ricevuta (in base ai controlli effettuati)
        Inserimento del button di disdetta della prenotazione (in base ai controlli effettuati)
    """
    def __init__(self, prenotazione, elimina_callback):
        super(VistaPrenotazione, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.elimina_callback = elimina_callback
        self.utente = "paziente"
        v_layout = QVBoxLayout()
        nome = ""
        info = {}

        # caricamento informazioni della prenotazione e inserimento dei dati tramite labels
        if isinstance(prenotazione, Prenotazione):
            nome = f"Prenotazione {prenotazione.id}"
            info = prenotazione.getInfoPrenotazione()

        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(QLabel(f"Id: {info['id']}"))
        v_layout.addWidget(QLabel(f"Data: {info['data'].strftime('%Y-%m-%d')}"))
        v_layout.addWidget(QLabel(f"Ora: {info['ora'].strftime('%H:%M')}"))
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

        # se la prenotazione non è già conclusa o scaduta o già disdetta, inserisco il button di disdetta che rimanda all'evento click di disdetta
        if not prenotazione.conclusa and not prenotazione.scaduta and not prenotazione.disdetta:
            btn_disdici = QPushButton('Disdici')
            btn_disdici.clicked.connect(lambda: self.disdetta_prenotazione_click(prenotazione))
            v_layout.addWidget(btn_disdici)

        # se la prenotazione è già conclusa controllo se esistono referto, ricevuta e mora e inserisco i button che rimandano ai rispettivi eventi click
        if prenotazione.conclusa:
            # caricamento dei referti nel dizionario referti
            referti = caricaFile("Referti")

            flag = False
            for referto in referti:
                if referto.id == prenotazione.id:
                    flag = True
                    # se il referto esiste stampo il button di visualizza referto, rimanda all'avento click
                    btn_visualizza_referto = QPushButton('Visualizza referto')
                    btn_visualizza_referto.clicked.connect(lambda: self.visualizza_referto_click(referto))
                    v_layout.addWidget(btn_visualizza_referto)

        # caricamento delle more nel dizionario more
        more = caricaFile("More")

        for mora in more:
            if mora.id == prenotazione.id:
                # se la mora esiste stampo il button di visualizza mora, rimanda all'evento click
                btn_visualizza_mora = QPushButton('Visualizza mora')
                btn_visualizza_mora.clicked.connect(lambda: self.visualizza_mora_click(mora))
                v_layout.addWidget(btn_visualizza_mora)

        # se la prenotazione risulta conclusa inserisco il button di visualizza ricevuta, rimanda all'evento click
        if prenotazione.conclusa:
            btn_visualizza_ricevuta = QPushButton('Visualizza ricevuta')
            btn_visualizza_ricevuta.clicked.connect(lambda: self.visualizza_ricevuta_click(prenotazione))
            v_layout.addWidget(btn_visualizza_ricevuta)

        self.setLayout(v_layout)
        self.setWindowTitle("Prenotazione")
