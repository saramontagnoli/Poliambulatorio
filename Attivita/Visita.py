"""
    Classe di modellazione per la Visita
    Rappresenta la visita che il paziente scegliere di prenotare
"""

from Gestione.GestoreFile import scriviFile


class Visita:

    """
        Costruttore della classe
        Set degli attributi di Visita secondo i parametri passati
        Scrittura su file della informazioni della Visita

        Il costruttore è stato utilizzato solo per la creazione iniziale del file che
        nella piattaforma risulta precompilato e caricato di default dall'amministratore
        Il file è stato quindi creato una sola volta con chiamate eseguite nel main
    """
    def __init__(self, id, nome, nota, id_reparto, costo):
        self.id = id
        self.nome = nome
        self.nota = nota
        self.id_reparto = id_reparto
        self.costo = costo

        # scrittura su file delle informazioni dei reparti
        scriviFile("Visite", self)
