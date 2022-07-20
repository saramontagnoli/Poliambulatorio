import datetime
import os
import pickle

from Gestione.GestoreFile import caricaFile


def richiediStatisticheMore():
    more = caricaFile("More")
    somma = 0
    num = 0
    anno_attuale = int(datetime.datetime.today().year)

    for mora in more:

        anno_mora = int(mora.data_emissione.year)

        if anno_mora == anno_attuale:
            num += 1
            somma += mora.importo

    return f"Somma totale anno {anno_attuale}: {round(somma, 2)}€ \nNumero more: {num}"


def richiediStatisticheRicevute():
    ricevute = caricaFile("Ricevute")

    somma = 0
    num = 0
    anno_attuale = int(datetime.datetime.today().year)
    for ricevuta in ricevute:
        anno_ricevuta = int(ricevuta.data_ora.year)

        if anno_ricevuta == anno_attuale:
            num += 1
            somma += ricevuta.importo

    return f"Somma totale anno {anno_attuale}: {round(somma, 2)}€ \nNumero ricevute: {num}"


class GestoreStatistiche:
    pass
