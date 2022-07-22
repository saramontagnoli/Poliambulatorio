"""
    Interfaccia grafica per la visualizzazione delle informazioni della prenotazione e gli eventuali button
    per la disdetta della prenotazione, visualizzazione e inserimento del referto LATO MEDICO
    La classe figlia eredita i metodi e attributi dalla classe padre VistaPrenotazione
    (ereditarietà)
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from Attivita.Prenotazione import Prenotazione
from Gestione.GestoreFile import caricaFile
from Viste.VistaInserisciReferto import VistaInserisciReferto
from Viste.VistaPrenotazione import VistaPrenotazione


class VistaPrenotazioneMedico(VistaPrenotazione):
    """
        Costruttore della classe figlia
        Set della finestra della visualizzazione della prenotazione lato medico
        Inserimento di tutte le informazioni della prenotazione con delle label
        Se le variabili boolean sono True stampa il campo: SI, altrimenti non stampa il campo
        Inserimento dei button di creazione o visualizzazione referto (in base ai controlli effettuati)
        Inserimento del button di disdetta della prenotazione (in base ai controlli effettuati)
    """

    def __init__(self, prenotazione, elimina_callback):
        super(VistaPrenotazione, self).__init__()
        self.inserisci_referto = None
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.elimina_callback = elimina_callback
        self.utente = "medico"
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
        v_layout.addWidget(QLabel(f"CF Paziente: {info['cf_paziente']}"))
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

        """
            Se la prenotazione è conclusa cerco se esiste il referto, se lo trovo inserisco il button per visualizza referto.
            Se non trovo il referto inserisco il button di Inserisci referto, rimanda all'evento click di inserimento referto
        """
        if prenotazione.conclusa:
            referti = caricaFile("Referti")

            flag = False
            for referto in referti:
                if referto.id == prenotazione.id:
                    flag = True
                    btn_visualizza_referto = QPushButton('Visualizza referti')
                    btn_visualizza_referto.clicked.connect(lambda: self.visualizza_referto_click(referto))
                    v_layout.addWidget(btn_visualizza_referto)
            if not flag:
                btn_inserisci_referto = QPushButton('Inserisci referto')
                btn_inserisci_referto.clicked.connect(lambda: self.inserisci_referto_click(prenotazione))
                v_layout.addWidget(btn_inserisci_referto)

        self.setLayout(v_layout)
        self.setWindowTitle("Prenotazione")

    """
        Metodo che implementa l'evento click per la creazione di un referto (chiamata alla vista di inserimento nuovo referto).
        Si richiama la vista dove si possono inserire le informazioni di un nuovo referto
    """

    def inserisci_referto_click(self, prenotazione):
        if isinstance(prenotazione, Prenotazione):
            # chiamata alla vista di inserimento di un nuovo referto
            self.inserisci_referto = VistaInserisciReferto(prenotazione, self.elimina_callback)
            self.inserisci_referto.show()
            self.elimina_callback()
            self.close()
