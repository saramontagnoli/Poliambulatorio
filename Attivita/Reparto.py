"""
    Classe di modellazione per il Reparto
    Rappresenta l'area di competenzd del Medico e quindi della Visita
"""

from Gestione.GestoreFile import scriviFile


class Reparto:

    """
        Costruttore della classe
        Set degli attributi di Reparto secondo i parametri passati
        Scrittura su file della informazioni del Reparto

        Il costruttore è stato utilizzato solo per la creazione iniziale del file che
        nella piattaforma risulta precompilato e caricato di default dall'amministratore
        Il file è stato quindi creato una sola volta con chiamate eseguite nel main
    """
    def __init__(self, id, nome, nota):
        self.id = id
        self.nome = nome
        self.nota = nota

        # scrittura su file delle informazioni dei reparti
        scriviFile("Reparti", self)






    # CANCELLARE I SET E GET
    # CANCELLARE I SET E GET
    # CANCELLARE I SET E GET
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return self.nota
