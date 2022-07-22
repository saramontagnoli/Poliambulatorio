from Eccezioni import Error


class PazienteOccupatoException(Exception):
    # Lanciata se il paziente è già occupato nell'orario scelto
    pass
