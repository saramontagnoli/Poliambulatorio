import datetime
import os.path
import pickle
import unittest
from unittest import TestCase

from Attivita.Paziente import Paziente


class TestGestisciPazienti(TestCase):

    def test_add_paziente(self):

        self.paziente = Paziente()
        self.paziente.setInfoPaziente(1, "Nome", "Cognome", "Password", datetime.datetime(2001, 1, 1), "CF",
                                      "Telefono", "M", "mail", "Indirizzo", "Nota", True, True)

        pazienti = None
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)

        self.assertIsNotNone(pazienti)

        self.assertIn(1, pazienti)

    def test_rimuovi_paziente(self):
        pazienti = None
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)
        self.assertIsNotNone(pazienti)
        self.assertIn(1, pazienti)
        self.paziente = Paziente().ricercaUtilizzatoreId(1)
        self.paziente.rimuoviPaziente()
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)
        self.assertIsNotNone(pazienti)
        self.assertNotIn(1, pazienti)


if __name__ == '__main__':
    unittest.main()
