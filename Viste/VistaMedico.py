"""
    Interfaccia grafica per la visualizzazione delle informazioni del medico LATO ADMIN
    (l'admin può cliccare un medico e all'apertura si avvia questa interfaccia grafica)
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from Attivita.Medico import Medico


class VistaMedico(QWidget):
    """
        Costruttore della classe
        Set della finestra della visualizzazione del medico lato admin
        Inserimento di tutte le informazioni del medico con delle label
        Inserimento del button di elimina del medico
    """
    def __init__(self, medico, elimina_callback):
        super(VistaMedico, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()
        nome = ""
        info = {}

        # caricamento informazioni del medico e inserimento dei dati tramite labels
        if isinstance(medico, Medico):
            nome = f"Medico {medico.id}"
            info = medico.getInfoMedico()

        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(QLabel(f"Nome: {info['nome']}"))
        v_layout.addWidget(QLabel(f"Cognome: {info['cognome']}"))
        v_layout.addWidget(QLabel(f"Data nascita: {info['data_nascita'].strftime('%Y-%m-%d')}"))
        v_layout.addWidget(QLabel(f"CF: {info['CF']}"))
        v_layout.addWidget(QLabel(f"Telefono: {info['telefono']}"))
        v_layout.addWidget(QLabel(f"Genere: {info['genere']}"))
        v_layout.addWidget(QLabel(f"Email: {info['mail']}"))
        v_layout.addWidget(QLabel(f"Indirizzo: {info['indirizzo']}"))
        v_layout.addWidget(QLabel(f"Abilitazione: {info['abilitazione']}"))
        v_layout.addWidget(QLabel(f"Reparto: {info['reparto']}"))

        # se la nota è presente la stampo, altrimenti non stampo nulla
        if "nota" in info:
            v_layout.addWidget(QLabel(f"Nota: {info['nota']}"))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # inserimento del button di elimina del medico, rimanda all'evento click di elimina medico
        btn_elimina = QPushButton('Elimina')
        btn_elimina.clicked.connect(lambda: self.elimina_medico_click(medico))
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(f"Medico {medico.id} - {medico.nome} {medico.cognome}")

    """
        Metodo che implementa l'evento click per l'eliminazione di un medico (chiamata metodo rimuoviMedico in Medico).
        Pop up di successo ad eliminazione effettuata
    """
    def elimina_medico_click(self, medico):
        if isinstance(medico, Medico):
            # chiamata metodo di rimozione del Medico
            medico.rimuoviMedico()
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Eliminato")
            # pop up di eliminazione effettuata del medico
            messaggio.setText("Il medico e' stato eliminato con successo. ")
            messaggio.exec_()
        self.elimina_callback()
        self.close()
