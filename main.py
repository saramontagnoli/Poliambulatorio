import pickle
import sys

from PyQt5.QtWidgets import QApplication

from Viste.VistaHomeAmm import VistaHomeAmm
from Viste.VistaHomePaziente import VistaHomePaziente
from Viste.VistaHomeMedico import VistaHomeMedico
from Viste.VistaLogin import VistaLogin
from Viste.VistaInserisciPazienti import VistaInserisciPazienti
from Attivita.Reparto import Reparto
from Attivita.Visita import Visita
# main con vista login degli utenti
if __name__ == '__main__':
    c1 = Reparto(1, "cardiologia", "cuore")
    c2 = Reparto(2, "radiologia", "ossa")
    c3 = Reparto(3, "pneumologia", "polmoni")
    c4 = Reparto(4, "oculistica", "occhi")
    c5 = Reparto(5, "otorinolaringoiatria", "otorino")

    v1 = Visita (1, "visita oculistica", "occhio dx e sx", 4)
    v2 = Visita (2, "terapia laser occhi", "occhio dx e sx", 4)
    v3 = Visita (3, "controllo pacemaker", "controllo abituale", 1)
    v4 = Visita (4, "elettrocardiogramma", "ecg", 1)
    v5 = Visita (5, "raggi caviglia", "controllo alla caviglia", 2)
    v6 = Visita (6, "raggi braccio", "controllo al braccio", 2)
    v7 = Visita (7, "visita base pneumologia", "controllo torace", 3)
    v8 = Visita (8, "visita base otorino", "controllo naso", 5)
    empty_list = []

    # interfaccia grafica per il login
    app = QApplication(sys.argv)
    form = VistaLogin()
    form.show()
    sys.exit(app.exec())
