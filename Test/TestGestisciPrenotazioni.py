"""
    Classe per i test sull'inserimento di una nuova Prenotazione, gestione di 3 dei 6 except
"""

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
    """
        Metodo che permette l'inserimento di una nuova Prenotazione tramite la chiamata al metodo aggiungiPrenotazione
        Con assertRaises gestisco le eccezioni che si vanno a creare dagli errori di inserimento
        Il test è dimostrativo di 3 dei 6 except gestiti:
            -EXCEPT WeekEndException, una prenotazione non può essere aggiunta se è durante il weekend
            -EXCEPT PazienteAssenteException, il CF del paziente non esiste nell'archio dei pazienti
            -EXCEPT RepartoMedicoExceptio, il reparto di visita e di medico non corrispondono
    """
    def test_add_prenotazione(self):
        self.prenotazione = Prenotazione()

        prenotazioni = []

        # gestione WeekEndException mediante assertRaises (richiamo la classe dell'Exception generata)
        with self.assertRaises(WeekEndException):
            print("\nIl sabato e la domenica l'ambulatorio è chiuso")
            # sto provando ad inserire una prenotazione in un sabato
            prenotazioni[1] = self.prenotazione.aggiungiPrenotazione(1, datetime.datetime(2022, 7, 23),
                                                                     datetime.time(8, 0, 0), 1, 1,
                                                                     "CF")

        # gestione PazienteAssenteException mediante assertRaises (richiamo la classe dell'Exception generata)
        with self.assertRaises(PazienteAssenteException):
            print("\nCodice fiscale non valido")
            # sto provando ad inserire un cf di un paziente non esistente
            prenotazioni[1] = self.prenotazione.aggiungiPrenotazione(1, datetime.datetime(2022, 7, 22),
                                                                     datetime.time(8, 0, 0), 1, 1,
                                                                     "CF_non_esistente")

        # gestione RepartoMedicoException mediante assertRaises (richiamo la classe dell'Exception generata)
        with self.assertRaises(RepartoMedicoException):
            print("\nIl reparto del medico e della visita non corrispondono")
            # sto provando ad inserire una prenotazione con reparto di medico e visita non uguali
            prenotazioni[1] = self.prenotazione.aggiungiPrenotazione(1, datetime.datetime(2022, 7, 22),
                                                                     datetime.time(8, 0, 0), 1, 6,
                                                                     "CF")

        # caricamento di una prenotazione valida + salvataggio
        self.prenotazione.aggiungiPrenotazione(1, datetime.datetime(2022, 7, 22),
                                               datetime.time(8, 0, 0), 1, 1,
                                               "CF")
        # caricamento file prenotazioni in dizionario prenotazioni e verifica che la prenotazione sia contenuta
        prenotazioni = None
        if os.path.isfile('File/Prenotazioni.pickle'):
            with open('File/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)

        self.assertIsNotNone(prenotazioni)

        self.assertIn(1, prenotazioni)

"""
    Main che permette l'esecuzione del test
"""
if __name__ == '__main__':
    unittest.main()
