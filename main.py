"""
    Classe contenente il main
    Run dell'applicazione e apertura della vista del login
"""

import sys

from PyQt5.QtWidgets import QApplication

from Gestione.GestoreFile import creazioneFile
from Viste.VistaLogin import VistaLogin
from Attivita.Reparto import Reparto
from Attivita.Visita import Visita


if __name__ == '__main__':

    # chiamate ai costruttori Reparto e Visita per la creazione dei file precompilati da parte dell'amministratore
    """"
    c1 = Reparto(1, "cardiologia", "cuore")
    c2 = Reparto(2, "radiologia", "ossa")
    c3 = Reparto(3, "pneumologia", "polmoni")
    c4 = Reparto(4, "oculistica", "occhi")
    c5 = Reparto(5, "otorinolaringoiatria", "otorino")

    v3 = Visita (1, "controllo pacemaker", "controllo abituale", 1, 50.00)
    v4 = Visita (2, "elettrocardiogramma", "ecg", 1, 50.00)
    v5 = Visita (3, "raggi caviglia", "controllo alla caviglia", 2, 120.00)
    v6 = Visita (4, "raggi braccio", "controllo al braccio", 2, 120.00)
    v7 = Visita (5, "visita base pneumologia", "controllo torace", 3, 80.00)
    v1 = Visita (6, "visita oculistica", "occhio dx e sx", 4, 80.00)
    v2 = Visita (7, "terapia laser occhi", "occhio dx e sx", 4, 100.00)
    v8 = Visita (8, "visita base otorino", "controllo naso", 5, 90.00)
    empty_list = []
    """

    app = QApplication(sys.argv)

    # chiamata a GestoreFile, controllo se i file esistono, in caso contrario li copio dal package Appoggio (file di default)
    creazioneFile('Prenotazioni')
    creazioneFile("Pazienti")
    creazioneFile("Medici")
    creazioneFile('Ricevute')
    creazioneFile('Referti')
    creazioneFile('More')
    creazioneFile('Visite')
    creazioneFile('Reparti')
    creazioneFile('Backup')

    # chiamata alla vista contenente la form di login
    form = VistaLogin()
    form.show()
    sys.exit(app.exec())
