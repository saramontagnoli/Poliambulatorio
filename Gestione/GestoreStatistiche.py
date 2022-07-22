"""
    Classe che implementa la gestione delle statistiche sui guadagni della struttura
    Si possono richiedere statistiche su:
        - numero ricevute e totale ricevute anno corrente
        - numero more e relativo importo anno corrente
"""

import datetime
import os
import pickle

from Gestione.GestoreFile import caricaFile

"""
    Metodo che permette di richiedere le statistiche sulle more emesse (n° di more e importo totale more)
    Ritorno una stringa formattata che contiene l'anno corrente, il totale delle more e il numero di more emesse
"""
def richiediStatisticheMore():
    # caricamento delle more nel dizionario more
    more = caricaFile("More")
    somma = 0
    num = 0
    anno_attuale = int(datetime.datetime.today().year)

    # scorro tutto il dizionario more per controllare le more all'anno attuale, incrementare un contatore e una variabile somma
    for mora in more:
        anno_mora = int(mora.data_emissione.year)
        if anno_mora == anno_attuale:
            num += 1
            somma += mora.importo

    # return della stringa contenente le statistiche richieste
    return f"Somma totale anno {anno_attuale}: {round(somma, 2)}€ \nNumero more: {num}"


"""
    Metodo che permette di richiedere le statistiche sulle ricevute (n° di ricevute e importo totale ricevute)
    Ritorno una stringa formattata che contiene l'anno corrente, il totale delle ricevute e il numero di ricevute
"""
def richiediStatisticheRicevute():
    # caricamento delle ricevute nel dizionario ricevute
    ricevute = caricaFile("Ricevute")
    somma = 0
    num = 0
    anno_attuale = int(datetime.datetime.today().year)

    # scorro tutto il dizionario ricevute per controllare le ricevute all'anno attuale, incrementare un contatore e una variabile somma
    for ricevuta in ricevute:
        anno_ricevuta = int(ricevuta.data_ora.year)

        if anno_ricevuta == anno_attuale:
            num += 1
            somma += ricevuta.importo

    # return della stringa contenente le statistiche richieste
    return f"Somma totale anno {anno_attuale}: {round(somma, 2)}€ \nNumero ricevute: {num}"


class GestoreStatistiche:
    pass
