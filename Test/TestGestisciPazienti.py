"""
    Classe per i test sull'inserimento e la rimozione di un determinato Paziente
"""

import datetime
import os.path
import pickle
import unittest
from unittest import TestCase

from Attivita.Paziente import Paziente


class TestGestisciPazienti(TestCase):
    """
        Metodo che permette l'inserimento di un nuovo Paziente tramite la chiamata al metodo setInfoPaziente
        Carico il dizionario dei pazienti, controllo che non sia None
        Controllo che il paziente appena inserito sia presente
    """

    def test_add_paziente(self):
        # inserimento di un nuovo Paziente
        self.paziente = Paziente()
        self.paziente.setInfoPaziente(1, "Nome", "Cognome", "Password", datetime.datetime(2001, 1, 1), "CF",
                                      "Telefono", "M", "mail", "Indirizzo", "Nota", True, True)

        # caricamento dizionario dei pazienti e controllo non sia None
        pazienti = None
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)

        self.assertIsNotNone(pazienti)

        # verifico che sia presente il paziente appena inserito
        self.assertIn(1, pazienti)

    """
        Metodo che permette la rimozione di un Paziente tramite la chiamata al metodo rimuoviPaziente
        Carico il dizionario dei pazienti, controllo che non sia None
        Controllo che il paziente sia presente
        Richiamo il metodo di rimozione e aggiorno il file dei pazienti controllando che il paziente non sia più presente
    """

    def test_rimuovi_paziente(self):
        # caricamento del file dei pazienti e controllo che non sia None
        pazienti = None
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)
        self.assertIsNotNone(pazienti)

        # controllo che il paziente sia presente e chiamo la rimozione del paziente + rimozione effettiva
        self.assertIn(1, pazienti)
        self.paziente = Paziente().ricercaUtilizzatoreId(1)
        self.paziente.rimuoviPaziente()

        # carico il file pazienti controllando che il paziente sia stato rimosso
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)
        self.assertIsNotNone(pazienti)
        self.assertNotIn(1, pazienti)


"""
    Main che permette l'esecuzione del test
"""
if __name__ == '__main__':
    unittest.main()
