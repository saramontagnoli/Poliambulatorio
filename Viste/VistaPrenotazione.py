import os
import pickle

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMessageBox

from Attivita.Mora import Mora
from Attivita.Prenotazione import Prenotazione
from Attivita.Referto import Referto


class VistaPrenotazione(QWidget):
    def __init__(self, elimina_callback):
        super(VistaPrenotazione, self).__init__()
        self.utente = ""
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.elimina_callback = elimina_callback

    # Funzione per l'eliminazione della prenotazione selezionato quando si preme il bottone
    def disdetta_prenotazione_click(self, prenotazione):
        flag = False
        if isinstance(prenotazione, Prenotazione):
            messaggio = QMessageBox()
            if self.utente == "admin" or self.utente == "medico":
                flag = prenotazione.disdiciPrenotazione(0)
            elif self.utente == "paziente":
                flag = prenotazione.disdiciPrenotazione(1)

            if flag:
                messaggio.setWindowTitle("Disdetta")
                messaggio.setText("La prenotazione e' stato disdetta con successo. ")
                messaggio.exec_()
            else:
                messaggio.setWindowTitle("Errore")
                messaggio.setText("La prenotazione e' gia' stata disdetta. ")
                messaggio.exec_()
        self.elimina_callback()
        self.close()

    # Funzione per la visualizzazione della ricevuta quando si preme il bottone
    def visualizza_ricevuta_click(self, prenotazione):
        if isinstance(prenotazione, Prenotazione):
            ricevute = []
            # Apertura e scrittura su file delle ricevute
            if os.path.isfile('File/Ricevute.pickle'):
                with open('File/Ricevute.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    ricevute.extend(current.values())

            for ricevuta in ricevute:
                if ricevuta.id == prenotazione.id:
                    messaggio = QMessageBox()
                    messaggio.setWindowIcon(QIcon('CroceVerde.png'))
                    messaggio.setWindowTitle("Ricevuta")
                    messaggio.setText(
                        f"Id: {ricevuta.id} \nImporto: {ricevuta.importo}€ \nData e ora: {ricevuta.data_ora.strftime('%Y-%m-%d %H:%M')}")
                    messaggio.exec_()

    # Funzione per la visualizzazione della mora quando si preme il bottone
    def visualizza_mora_click(self, mora):
        if isinstance(mora, Mora):
            messaggio = QMessageBox()
            messaggio.setWindowIcon(QIcon('CroceVerde.png'))
            messaggio.setWindowTitle("Mora")
            messaggio.setText(
                f"Id: {mora.id} \nImporto: {round(mora.importo, 2)}€ \nNota: {mora.nota} \nData e ora: {mora.data_emissione.strftime('%Y-%m-%d %H:%M')}")
            messaggio.exec_()

    # Funzione per la visualizzazione della mora quando si preme il pulsante
    def visualizza_referto_click(self, referto):
        if isinstance(referto, Referto):
            messaggio = QMessageBox()
            messaggio.setWindowIcon(QIcon('CroceVerde.png'))
            messaggio.setWindowTitle("Referto")
            messaggio.setText(
                f"Id: {referto.id} \nNota: {referto.nota} \nData e ora: {referto.data_emissione.strftime('%Y-%m-%d %H:%M')}")
            messaggio.exec_()
