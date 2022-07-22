import datetime
import os.path
import pickle
import unittest
from unittest import TestCase

from Attivita.Paziente import Paziente

from Gestione.GestoreFile import caricaFile, creazioneFile


class TestGestisciPazienti(TestCase):

    def test_add_paziente(self):
        creazioneFile("Pazienti")

        """"
        os.makedirs("File/")
        empty_list = []
        # Open the pickle file in 'wb' so that you can write and dump the empty variable
        openfile = open('File/Pazienti.pickle', 'wb')
        pickle.dump(empty_list, openfile)
        openfile.close()
        """
        self.paziente = Paziente()
        self.paziente.setInfoPaziente(1, "Nome", "Cognome", "Password", datetime.datetime(2001, 1, 1), "CF",
                                      "Telefono","M", "mail", "Indirizzo", "Nota", True, True)

        pazienti = caricaFile("Pazienti")

        """"
        pazienti = None
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)
                
        print(pazienti[0])
        print(pazienti[0].nome)
        """

        self.assertIsNotNone(pazienti)

        for paziente in pazienti:
            print("\n")
            print(paziente.id)
            print(paziente.nome)
            print(paziente.cognome)
            print(paziente.password)
            print(paziente.data_nascita)
            print("\n")
            # self.assertIn(paziente.id, pazienti)

        self.assertIn(1, pazienti)

    def test_rimuovi_paziente(self):
        pazienti = caricaFile("Pazienti")
        """"
        pazienti = None
        if os.path.isfile('File/Pazienti.pickle'):
            with open('File/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)
"""
        self.assertIsNotNone(pazienti)
        self.assertIn(1, pazienti)
        self.paziente = Paziente().ricercaUtilizzatoreId(1)
        self.paziente.rimuoviPaziente()

        pazienti = caricaFile("Pazienti")

        self.assertIsNotNone(pazienti)
        self.assertNotIn(1, pazienti)


if __name__ == '__main__':
    unittest.main()
