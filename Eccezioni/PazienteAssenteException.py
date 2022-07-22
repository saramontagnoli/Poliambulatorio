from Eccezioni import Error


class PazienteAssenteException(Exception):
    # Lanciata se il CF del paziente non viene trovato nel file Pazienti.pickle
    pass
