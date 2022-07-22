"""
    Interfaccia grafica per la visualizzazione delle informazioni della prenotazione e gli eventuali button
    per la disdetta della prenotazione, visualizzazione della ricevuta, del referto e della mora
    La classe padre raggruppa al suo interno i metodi e attributi in comune tra VistaPrenotazioneAmm, VistaPrenotazionePaziente
    e VistaPrenotazioneMedico
    (ereditarietà)
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMessageBox

from Attivita.Mora import Mora
from Attivita.Prenotazione import Prenotazione
from Attivita.Referto import Referto
from Gestione.GestoreFile import caricaFile

"""
     Metodo che implementa l'evento click per la visualizzazione di una particolare Ricevuta.
     Carico il file delle ricevute e cerco la ricevuta desiderata aprendo un pop-up con le informazioni
 """


def visualizza_ricevuta_click(prenotazione):
    if isinstance(prenotazione, Prenotazione):
        # caricamento delle ricevute nel dizionario ricevute, scorro il dizionario e cerco la prenotazione desiderata, pop-up con le informazioni
        ricevute = caricaFile("Ricevute")

        for ricevuta in ricevute:
            if ricevuta.id == prenotazione.id:
                messaggio = QMessageBox()
                messaggio.setWindowIcon(QIcon('CroceVerde.png'))
                messaggio.setWindowTitle("Ricevuta")
                # pop up contenente le informazioni della ricevuta trovata
                messaggio.setText(
                    f"Id: {ricevuta.id} \nImporto: {ricevuta.importo}€ \nData e ora: {ricevuta.data_ora.strftime('%Y-%m-%d %H:%M')}")
                messaggio.exec_()


"""
        Metodo che implementa l'evento click per la visualizzazione di un particolare Referto.
        Mediante le informazioni contenute in referto, setto un pop-up contenente tutte le informazioni
"""


def visualizza_referto_click(referto):
    if isinstance(referto, Referto):
        messaggio = QMessageBox()
        messaggio.setWindowIcon(QIcon('CroceVerde.png'))
        messaggio.setWindowTitle("Referto")
        # pop up contenente le informazioni di referto
        messaggio.setText(
            f"Id: {referto.id} \nNota: {referto.nota} \nData e ora: {referto.data_emissione.strftime('%Y-%m-%d %H:%M')}")
        messaggio.exec_()


"""
        Metodo che implementa l'evento click per la visualizzazione di una particolare Mora.
        Mediante le informazioni contenute in mora, setto un pop-up contenente tutte le informazioni
"""


def visualizza_mora_click(mora):
    if isinstance(mora, Mora):
        messaggio = QMessageBox()
        messaggio.setWindowIcon(QIcon('CroceVerde.png'))
        messaggio.setWindowTitle("Mora")
        # pop up contenente le informazioni di mora
        messaggio.setText(
            f"Id: {mora.id} \nImporto: {round(mora.importo, 2)}€ \nNota: {mora.nota} \nData e ora: {mora.data_emissione.strftime('%Y-%m-%d %H:%M')}")
        messaggio.exec_()


class VistaPrenotazione(QWidget):
    """
        Costruttore della classe padre
        Set della finestra della visualizzazione della prenotazione
    """

    def __init__(self, elimina_callback):
        super(VistaPrenotazione, self).__init__()
        self.utente = ""
        self.setWindowIcon(QIcon('CroceVerde.png'))
        self.elimina_callback = elimina_callback

    """
        Metodo che implementa l'evento click per la disdetta di una particolare Prenotazione (chiamata al metodo disdiciPrenotazione in Prenotazione).
        Controllo chi sta richiedendo la disdetta:
            - se è l'admin/medico a chiedere la disdetta passo al metodo disdiciPrenotazione lo 0 per non far pagare la more al paziente 
            - se è il paziente a chiedere la disdetta passo al metodo disdiciPrenotazione 1, eventualmente il paziente pagherà la mora
        Stampa di pop-up di errore o successo in base all'esito della disdetta
    """

    def disdetta_prenotazione_click(self, prenotazione):
        flag = False
        if isinstance(prenotazione, Prenotazione):
            messaggio = QMessageBox()

            # controllo chi è che sta chiedendo la disdetta
            if self.utente == "admin" or self.utente == "medico":
                flag = prenotazione.disdiciPrenotazione(0)
            elif self.utente == "paziente":
                flag = prenotazione.disdiciPrenotazione(1)

            # se la disdetta è andata a buon fine pop up di successo, altrimenti pop up con errore
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
