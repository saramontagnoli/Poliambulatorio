from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from Attivita.Medico import Medico


class VistaMedico(QWidget):

    def __init__(self, medico, elimina_callback):
        super(VistaMedico, self).__init__()
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()
        nome = ""
        info = {}

        if isinstance(medico, Medico):
            nome = f"Medico {medico.id}"
            info = medico.getInfoMedico()

        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Si scrivono i vari dati del medico selezionato
        v_layout.addWidget(QLabel(f"Nome: {info['nome']}"))
        v_layout.addWidget(QLabel(f"Cognome: {info['cognome']}"))
        v_layout.addWidget(QLabel(f"Data nascita: {info['data_nascita'].strftime('%Y-%m-%d')}"))
        v_layout.addWidget(QLabel(f"CF: {info['CF']}"))
        v_layout.addWidget(QLabel(f"Telefono: {info['telefono']}"))
        v_layout.addWidget(QLabel(f"Genere: {info['genere']}"))
        v_layout.addWidget(QLabel(f"Email: {info['mail']}"))
        v_layout.addWidget(QLabel(f"Indirizzo: {info['indirizzo']}"))
        v_layout.addWidget(QLabel(f"Abilitazione: {info['abilitazione']}"))

        # Se la nota è presente si stampa
        if "nota" in info:
            v_layout.addWidget(QLabel(f"Nota: {info['nota']}"))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Creazione del bottone per eliminare il medico che si sta visualizzando
        btn_elimina = QPushButton('Elimina')
        btn_elimina.clicked.connect(lambda: self.elimina_medico_click(medico))
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle("Medico")

    # Funzione per l'eliminazione del medico selezionato quando si preme il bottone
    def elimina_medico_click(self, medico):
        if isinstance(medico, Medico):
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Eliminato")
            messaggio.setText("Il medico e' stato eliminato con successo. ")
            messaggio.exec_()
            medico.rimuoviMedico()
        self.elimina_callback()
        self.close()
