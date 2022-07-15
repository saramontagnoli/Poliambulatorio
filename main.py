import pickle
import sys

from PyQt5.QtWidgets import QApplication

from Viste.VistaHomeAmm import VistaHomeAmm
from Viste.VistaHomePaziente import VistaHomePaziente
from Viste.VistaHomeMedico import VistaHomeMedico
from Viste.VistaLogin import VistaLogin
from Viste.VistaInserisciPazienti import VistaInserisciPazienti
from Attivita.Reparto import Reparto
# main con vista login degli utenti
if __name__ == '__main__':
    c1 = Reparto(1, "cardiologia", "cuore")
    c2 = Reparto(2, "radiologia", "ossa")
    c3 = Reparto(3, "pneumologia", "polmoni")
    c4 = Reparto(4, "oculistica", "occhi")
    c5 = Reparto(5, "otorinolaringoiatria", "otorino")

    empty_list = []

    # interfaccia grafica per il login
    app = QApplication(sys.argv)
    form = VistaLogin()
    form.show()
    sys.exit(app.exec())
