import sys

from PyQt5.QtWidgets import QApplication

from Viste.VistaHomeAmm import VistaHomeAmm
from Viste.VistaHomePaziente import VistaHomePaziente
from Viste.VistaHomeMedico import VistaHomeMedico
from Viste.VistaLogin import VistaLogin
#main con viste
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = VistaLogin()
    form.show()
    vista_home = VistaHomeAmm()
    vista_home.show()
    vista_home2 = VistaHomeMedico()
    vista_home2.show()
    vista_home3 = VistaHomePaziente()
    vista_home3.show()
    sys.exit(app.exec())

