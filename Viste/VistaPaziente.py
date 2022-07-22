"""
    Interfaccia grafica per la visualizzazione delle informazioni del paziente LATO ADMIN
    (l'admin può cliccare un paziente e all'apertura si avvia questa interfaccia grafica)
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from Attivita.Paziente import Paziente


class VistaPaziente(QWidget):
    """
        Costruttore della classe
        Set della finestra della visualizzazione del paziente lato admin
        Inserimento di tutte le informazioni del paziente con delle label
        Controllo le variabili boolean, se sono True stampo la variabile, altrimenti non stampo nulla
        Inserimento del button di elimina del paziente
    """
    def __init__(self, paziente, elimina_callback):
        super(VistaPaziente, self).__init__()
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()
        nome = ""
        info = {}

        # caricamento informazioni del paziente e inserimento dei dati tramite labels
        if isinstance(paziente, Paziente):
            nome = f"Paziente {paziente.id}"
            info = paziente.getInfoPaziente()

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

        # se la nota è presente la stampo, altrimenti non stampo nulla
        if "nota" in info:
            v_layout.addWidget(QLabel(f"Nota: {info['nota']}"))

        # controllo stampe variabili boolean, se sono True le stampo, altrimenti non stampo nulla
        if bool(info['allergia']):
            v_layout.addWidget(QLabel(f"Allergia: Si"))

        if bool(info['malattia_pregressa']):
            v_layout.addWidget(QLabel(f"Malattia pregressa: Si"))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # inserimento del button di elimina del paziente, rimanda all'evento click di elimina paziente
        btn_elimina = QPushButton('Elimina')
        btn_elimina.clicked.connect(lambda: self.elimina_paziente_click(paziente))
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(f"Paziente {paziente.id} - {paziente.nome} {paziente.cognome}")


    """
        Metodo che implementa l'evento click per l'eliminazione di un paziente (chiamata metodo rimuoviPaziente in Paziente).
        Pop up di successo ad eliminazione effettuata
    """
    def elimina_paziente_click(self, paziente):
        if isinstance(paziente, Paziente):
            # chiamata al metodo di rimozione del paziente
            paziente.rimuoviPaziente()
            messaggio = QMessageBox()
            messaggio.setWindowTitle("Eliminato")
            # pop up successo avvenuta eliminazione
            messaggio.setText("Il paziente e' stato eliminato con successo. ")
            messaggio.exec_()
        self.elimina_callback()
        self.close()
