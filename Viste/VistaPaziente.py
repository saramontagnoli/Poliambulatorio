from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from Attivita.Paziente import Paziente


class VistaPaziente(QWidget):

    def __init__(self, paziente, elimina_callback):
        super(VistaPaziente, self).__init__()
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()
        nome = ""
        info = {}

        if isinstance(paziente, Paziente):
            nome = f"Paziente {paziente.id}"
            info = paziente.getInfoPaziente()

        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Si scrivono i vari dati del paziente selezionato
        v_layout.addWidget(QLabel(f"Nome: {info['nome']}"))
        v_layout.addWidget(QLabel(f"Cognome: {info['cognome']}"))
        v_layout.addWidget(QLabel(f"Data nascita: {info['data_nascita'].strftime('%Y-%m-%d')}"))
        v_layout.addWidget(QLabel(f"CF: {info['CF']}"))
        v_layout.addWidget(QLabel(f"Telefono: {info['telefono']}"))
        v_layout.addWidget(QLabel(f"Genere: {info['genere']}"))
        v_layout.addWidget(QLabel(f"Email: {info['mail']}"))
        v_layout.addWidget(QLabel(f"Indirizzo: {info['indirizzo']}"))

        # Se la nota è presente si stampa
        if "nota" in info:
            v_layout.addWidget(QLabel(f"Nota: {info['nota']}"))

        # Se il cliente è allergico o ha una malattia repressa si stampa il rispettivo dato, altrimenti no
        if bool(info['allergia']):
            v_layout.addWidget(QLabel(f"Allergia: Si"))

        if bool(info['malattia_pregressa']):
            v_layout.addWidget(QLabel(f"Malattia pregressa: Si"))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Creazione del bottone per eliminare il paziente che si sta visualizzando
        btn_elimina = QPushButton('Elimina')
        btn_elimina.clicked.connect(lambda: self.elimina_paziente_click(paziente))
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle("Paziente")

        """"def elimina_paziente_click(self, paziente):
            if isinstance(paziente, Paziente):
                paziente.rimuoviPaziente()
            self.elimina_callback()
            self.close()"""

    # Funzione per l'eliminazione del paziente selezionato quando si preme il bottone
    def elimina_paziente_click(self, paziente):
        if isinstance(paziente, Paziente):
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Eliminato")
            messaggio.setText("Il paziente e' stato eliminato con successo. ")
            messaggio.exec_()
            paziente.rimuoviPaziente()
        self.elimina_callback()
        self.close()
