"""
    Classe di modellazione per il Reparto
    Rappresenta l'area di competenza del Medico e quindi della Visita
"""

from Gestione.GestoreFile import scriviFile


class Reparto:

    """
        Costruttore della classe
        Set degli attributi di Reparto secondo i parametri passati
        Scrittura su file delle informazioni del Reparto

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
