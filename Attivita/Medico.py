from Attivita.Utilizzatore import Utilizzatore
from Gestione.GestoreFile import scriviFile, ricercaElemFile, rimuoviElemFile


class Medico(Utilizzatore):

    def __init__(self):
        super().__init__()
        self.abilitazione = ""
        self.id_reparto = 0

    def setInfoMedico(self, id, password, cognome, nome, data_nascita, CF, telefono, genere, mail, indirizzo, nota,
                      abilitazione, id_reparto):
        self.setInfoUtilizzatore(id, password, cognome, nome, data_nascita, CF,
                                 telefono, genere, mail, indirizzo, nota)
        self.abilitazione = abilitazione
        self.id_reparto = id_reparto

        scriviFile("Medici", self)

    def getInfoMedico(self):
        info = self.getInfoUtilizzatore()
        info["abilitazione"] = self.abilitazione
        info["reparto"] = self.id_reparto
        return info

    def ricercaUtilizzatoreCF(self, CF):
        return ricercaElemFile("Medici", CF)

    def ricercaUtilizzatoreId(self, id):
        return ricercaElemFile("Medici", id)

    # Rimozione di un medico mediante il suo id
    def rimuoviMedico(self):
        rimuoviElemFile("Medici", self)
        self.rimuoviUtilizzatore()
        self.abilitazione = ""
        # self.allergia = False
        # self.malattia_pregressa = False
        del self

    def getAbilitazione(self):
        return self.abilitazione

    def setAbilitazione(self, abilitazione):
        self.abilitazione = abilitazione
