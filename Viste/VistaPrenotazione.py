from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox


from Attivita.Prenotazione import Prenotazione


class VistaPrenotazione(QWidget):

    def __init__(self, prenotazione, elimina_callback):
        super(VistaPrenotazione, self).__init__()
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
        v_layout.addWidget(QLabel(f"Ora: {info['ora'].strftime('%H-%M-%S')}"))

        # Eventuali stampe degli stati della prenotazione
        if bool(info['scaduta']):
            v_layout.addWidget(QLabel(f"Scaduta: Si"))

        if bool(info['disdetta']):
            v_layout.addWidget(QLabel(f"Disdetta: Si"))

        if bool(info['conclusa']):
            v_layout.addWidget(QLabel(f"Conclusa: Si"))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Creazione del bottone per disdire la prenotazione che si sta visualizzando
        btn_disdici = QPushButton('Disdici')
        btn_disdici.clicked.connect(lambda: self.disdetta_prenotazione_click(prenotazione))
        v_layout.addWidget(btn_disdici)

        self.setLayout(v_layout)
        self.setWindowTitle("Prenotazione")

    # Funzione per l'eliminazione della prenotazione selezionato quando si preme il bottone
    def disdetta_prenotazione_click(self, prenotazione):
        if isinstance(prenotazione, Prenotazione):
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Eliminata")
            messaggio.setText("La prenotazione e' stato eliminata con successo. ")
            messaggio.exec_()
            prenotazione.setDisdetta(True)
        self.elimina_callback()
        self.close()
