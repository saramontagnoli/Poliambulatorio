from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from Attivita.Paziente import Paziente

class VistaPaziente(QWidget):

    def __init__(self, paziente, elimina_callback):
        super(VistaPaziente, self).__init__()
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()
        nome = ""
        info = {}

        if isinstance(paziente, Paziente):
             nome = f"Paziente { paziente.id }"
             info = paziente.getInfoPaziente()

        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(QLabel(f"Nome: {info['nome']}"))
        v_layout.addWidget(QLabel(f"Cognome: {info['cognome']}"))
        v_layout.addWidget(QLabel(f"Data nascita: {info['data_nascita']}"))
        v_layout.addWidget(QLabel(f"CF: {info['CF']}"))
        v_layout.addWidget(QLabel(f"Telefono: {info['telefono']}"))
        v_layout.addWidget(QLabel(f"Genere: {info['genere']}"))
        v_layout.addWidget(QLabel(f"Email: {info['mail']}"))
        v_layout.addWidget(QLabel(f"Indirizzo: {info['indirizzo']}"))

        if "nota" in info:
            v_layout.addWidget(QLabel(f"Nota: {info['nota']}"))

        if bool(info['allergia']) == 1:
            v_layout.addWidget(QLabel(f"Allergia: {info['allergia']}"))

        if bool(info['malattia_pregressa']) == 1:
            v_layout.addWidget(QLabel(f"Malattia_pregressa: {info['malattia_pregressa']}"))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton(v_layout)
        btn_elimina.clicked.connect(lambda: self.elimina_paziente_click(paziente))
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle("Paziente")

        def elimina_paziente_click(self, paziente):
            if isinstance(paziente, Paziente):
                paziente.rimuoviPaziente()
            self.elimina_callback()
            self.close()

