import pickle
import sys

from PyQt5.QtWidgets import QApplication

from Viste.VistaHomeAmm import VistaHomeAmm
from Viste.VistaHomePaziente import VistaHomePaziente
from Viste.VistaHomeMedico import VistaHomeMedico
from Viste.VistaLogin import VistaLogin
from Viste.VistaInserisciPazienti import VistaInserisciPazienti

# main con vista login degli utenti
if __name__ == '__main__':
    empty_list = []

    # interfaccia grafica per il login
    app = QApplication(sys.argv)
    form = VistaLogin()
    form.show()
    sys.exit(app.exec())
