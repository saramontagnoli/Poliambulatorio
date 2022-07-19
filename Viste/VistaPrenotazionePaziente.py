import os
import pickle

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from Attivita.Prenotazione import Prenotazione
from Attivita.Referto import Referto
from Attivita.Mora import Mora

class VistaPrenotazionePaziente(QWidget):

    def __init__(self, prenotazione, elimina_callback):
        super(VistaPrenotazionePaziente, self).__init__()
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
        #v_layout.addWidget(QLabel(f"CF Paziente: {info['cf_paziente']}"))
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

        # disdetta della prenotazione da parte del paziente
        if not prenotazione.conclusa and not prenotazione.scaduta and not prenotazione.disdetta:
            btn_disdici = QPushButton('Disdici')
            btn_disdici.clicked.connect(lambda: self.disdetta_prenotazione_click(prenotazione))
            v_layout.addWidget(btn_disdici)

        if prenotazione.conclusa:
            referti = []
            # Apertura e scrittura su file delle more
            if os.path.isfile('File/Referti.pickle'):
                with open('File/Referti.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    referti.extend(current.values())

            flag = False
            for referto in referti:
                if referto.id == prenotazione.id:
                    flag = True
                    btn_visualizza_referto = QPushButton('Visualizza referto')
                    btn_visualizza_referto.clicked.connect(lambda: self.visualizza_referto_click(referto))
                    v_layout.addWidget(btn_visualizza_referto)

        more = []
        # Apertura e scrittura su file delle more
        if os.path.isfile('File/More.pickle'):
            with open('File/More.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                more.extend(current.values())

        for mora in more:
            if mora.id == prenotazione.id:
                btn_visualizza_mora = QPushButton('Visualizza mora')
                btn_visualizza_mora.clicked.connect(lambda: self.visualizza_mora_click(mora))
                v_layout.addWidget(btn_visualizza_mora)

        if prenotazione.conclusa:
            btn_visualizza_ricevuta = QPushButton('Visualizza ricevuta')
            btn_visualizza_ricevuta.clicked.connect(lambda: self.visualizza_ricevuta_click(prenotazione))
            v_layout.addWidget(btn_visualizza_ricevuta)


        self.setLayout(v_layout)
        self.setWindowTitle("Prenotazione")

    # Funzione per l'eliminazione della prenotazione selezionato quando si preme il bottone
    def disdetta_prenotazione_click(self, prenotazione):
        if isinstance(prenotazione, Prenotazione):
            messaggio = QMessageBox()
            if (prenotazione.disdiciPrenotazione(1)):
                messaggio.setWindowTitle("Disdetta")
                messaggio.setText("La prenotazione e' stato disdetta con successo. ")
                messaggio.exec_()
            else:
                messaggio.setWindowTitle("Errore")
                messaggio.setText("La prenotazione e' gia' stata disdetta. ")
                messaggio.exec_()
        self.elimina_callback()
        self.close()

    def visualizza_ricevuta_click(self, prenotazione):
        if isinstance(prenotazione,Prenotazione):
            ricevute = []
            # Apertura e scrittura su file delle ricevute
            if os.path.isfile('File/Ricevute.pickle'):
                with open('File/Ricevute.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    ricevute.extend(current.values())

            for ricevuta in ricevute:
                if ricevuta.id == prenotazione.id:
                    messaggio = QMessageBox()
                    messaggio.setWindowIcon(QIcon('CroceVerde.png'))
                    messaggio.setWindowTitle("Ricevuta")
                    messaggio.setText(f"Id: {ricevuta.id} \nImporto: {ricevuta.importo}€ \nData e ora: {ricevuta.data_ora.strftime('%Y-%m-%d %H:%M')}" )
                    messaggio.exec_()

    def visualizza_mora_click(self, mora):
        if isinstance(mora, Mora):
            messaggio = QMessageBox()
            messaggio.setWindowIcon(QIcon('CroceVerde.png'))
            messaggio.setWindowTitle("Mora")
            messaggio.setText(f"Id: {mora.id} \nImporto: {round(mora.importo, 2)}€ \nNota: {mora.nota} \nData e ora: {mora.data_emissione.strftime('%Y-%m-%d %H:%M')}" )
            messaggio.exec_()

    # Funzione per la visualizzazione della mora quando si preme il pulsante
    def visualizza_referto_click(self, referto):
        if isinstance(referto, Referto):
            messaggio = QMessageBox()
            messaggio.setWindowIcon(QIcon('CroceVerde.png'))
            messaggio.setWindowTitle("Referto")
            messaggio.setText(
                f"Id: {referto.id} \nNota: {referto.nota} \nData e ora: {referto.data_emissione.strftime('%Y-%m-%d %H:%M')}")
            messaggio.exec_()
