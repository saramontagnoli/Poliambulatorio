import datetime
import os
import pickle


def richiediStatisticheMora():
    more = []
    # Apertura e scrittura su file delle visite
    if os.path.isfile('File/More.pickle'):
        with open('File/More.pickle', 'rb') as f:
            current = dict(pickle.load(f))
            more.extend(current.values())

    somma = 0
    num = 0
    anno_attuale = int(datetime.datetime.today().year)

    for mora in more:

        anno_mora = int(mora.data_emissione.year)

        if anno_mora == anno_attuale:
            num += 1
            somma += mora.importo

    return f"Somma totale anno {anno_attuale}: {round(somma,2)}€ \nNumero more: {num}"


def richiediStatisticheRicevuta():
    ricevute = []
    # Apertura e scrittura su file delle visite
    if os.path.isfile('File/Ricevute.pickle'):
        with open('File/Ricevute.pickle', 'rb') as f:
            current = dict(pickle.load(f))
            ricevute.extend(current.values())

    # for ricevuta in ricevute:

    return


class GestoreStatistiche:
    pass
