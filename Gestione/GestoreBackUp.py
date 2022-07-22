"""
    Classe che implementa la gestione del backup dei dati della piattaforma
    Permette di modificare la periodicità e l'ora del backup
    Permette l'esecuzione del backup
"""

import datetime
import os
import pickle
import shutil

from Gestione.GestoreFile import caricaFile


"""
    Metodo che permette di effettuare l'esecuzione del backup in una nuova cartella
    Il nome della cartella sarà nominata con Backup + la data e l'ora attuali
"""
def effettuaBackUp():
    today = datetime.datetime.today()
    backup_folder = f"Backup_{today.year}_{today.month}_{today.day}_{today.hour}_{today.minute}_{today.second}/"
    shutil.copytree("File/", backup_folder)
    return


class GestoreBackUp:

    """
        Costruttore della classe
        Caricamento delle impostazioni sulla periodicità e ora del backup
    """
    def __init__(self):
        # caricamento del file con chiama a GestoreFile
        self.impostazioni = caricaFile("Backup")

        # salvataggio informazioni delle impostazioni lette dal file
        self.ora = self.impostazioni[0].ora
        self.frequenza = self.impostazioni[0].frequenza

        print(self.ora)
        print(self.frequenza)


    """
        Metodo che permette la modifica delle impostazioni di backup del sistema
        Caricamento delle nuove informazioni nel file Backup.pickle
    """
    def modificaBackUp(self, ora, frequenza):

        self.ora = ora
        self.frequenza = frequenza

        # scrittura su file delle nuove impostazioni prese dai parametri passati
        impostazioni = {}
        if os.path.isfile('File/Backup.pickle'):
            with open('File/Backup.pickle', 'rb') as f:
                impostazioni = pickle.load(f)
        impostazioni[0] = self
        with open('File/Backup.pickle', 'wb') as f:
            pickle.dump(impostazioni, f, pickle.HIGHEST_PROTOCOL)

        return
