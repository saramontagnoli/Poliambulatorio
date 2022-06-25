import pickle
import sys

from PyQt5.QtWidgets import QApplication

from Viste.VistaHomeAmm import VistaHomeAmm
from Viste.VistaHomePaziente import VistaHomePaziente
from Viste.VistaHomeMedico import VistaHomeMedico
from Viste.VistaLogin import VistaLogin
from Viste.VistaInserisciPazienti import VistaInserisciPazienti
#main con viste
if __name__ == '__main__':
    empty_list = []
    # Open the pickle file in 'wb' so that you can write and dump the empty variable
    # openfile = open('File/Pazienti.pickle', 'wb')
    # pickle.dump(empty_list, openfile)
    # openfile.close()

    app = QApplication(sys.argv)
    form = VistaLogin()
    form.show()
    # vista_home = VistaHomeAmm()
    # vista_home.show()
    vista_home2 = VistaHomeMedico()
    vista_home2.show()
    vista_home3 = VistaHomePaziente()
    vista_home3.show()
    #vista_home4 = VistaInserisciPazienti()
    #vista_home4.show()
    sys.exit(app.exec())

