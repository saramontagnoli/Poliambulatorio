import datetime
import os
import pickle
import shutil


def effettuaBackUp():
    today = datetime.datetime.today()
    backup_folder = f"Backup_{today.year}_{today.month}_{today.day}_{today.hour}_{today.minute}_{today.second}/"
    shutil.copytree("File/", backup_folder)
    return


class GestoreBackUp:

    # Impostazioni standard di Back-up
    def __init__(self):
        impostazioni = []
        # Caricamento delle impostazioni di back-up salvate in precedenza
        if os.path.isfile('File/Backup.pickle'):
            with open('File/Backup.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                impostazioni.extend(current.values())

            self.ora = impostazioni[0].ora
            self.frequenza = impostazioni[0].frequenza

    # frequenza intesa come intervallo giornaliero (ogni n giorni)
    def modificaBackUp(self, ora, frequenza):
        self.ora = ora
        self.frequenza = frequenza

        impostazioni = {}
        if os.path.isfile('File/Backup.pickle'):
            with open('File/Backup.pickle', 'rb') as f:
                impostazioni = pickle.load(f)
        impostazioni[0] = self
        with open('File/Backup.pickle', 'wb') as f:
            pickle.dump(impostazioni, f, pickle.HIGHEST_PROTOCOL)

        return
