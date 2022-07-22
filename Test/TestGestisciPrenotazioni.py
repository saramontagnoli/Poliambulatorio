import datetime
import os.path
import pickle
import unittest
from unittest import TestCase

from Attivita.Prenotazione import Prenotazione
from Eccezioni.PazienteAssenteException import PazienteAssenteException
from Eccezioni.RepartoMedicoException import RepartoMedicoException
from Eccezioni.WeekEndException import WeekEndException


class TestGestisciPrenotazioni(TestCase):

    def test_add_prenotazione(self):
        self.prenotazione = Prenotazione()

        prenotazioni = []

        # WeekEndException

        with self.assertRaises(WeekEndException):
            print("\nIl sabato e la domenica l'ambulatorio è chiuso")
            prenotazioni[1] = self.prenotazione.aggiungiPrenotazione(1, datetime.datetime(2022, 7, 23),
                                                                     datetime.time(8, 0, 0), 1, 1,
                                                                     "CF")

        # PazienteAssenteException

        with self.assertRaises(PazienteAssenteException):
            print("\nCodice fiscale non valido")
            prenotazioni[1] = self.prenotazione.aggiungiPrenotazione(1, datetime.datetime(2022, 7, 22),
                                                                     datetime.time(8, 0, 0), 1, 1,
                                                                     "CF_non_esistente")
        # RepartoMedicoException

        with self.assertRaises(RepartoMedicoException):
            print("\nIl reparto del medico e della visita non corrispondono")
            prenotazioni[1] = self.prenotazione.aggiungiPrenotazione(1, datetime.datetime(2022, 7, 22),
                                                                     datetime.time(8, 0, 0), 1, 6,
                                                                     "CF")

        self.prenotazione.aggiungiPrenotazione(1, datetime.datetime(2022, 7, 22),
                                               datetime.time(8, 0, 0), 1, 1,
                                               "CF")

        prenotazioni = None
        if os.path.isfile('File/Prenotazioni.pickle'):
            with open('File/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)

        self.assertIsNotNone(prenotazioni)

        self.assertIn(1, prenotazioni)


if __name__ == '__main__':
    unittest.main()