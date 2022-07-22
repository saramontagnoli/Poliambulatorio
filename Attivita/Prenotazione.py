"""
    Classe di modellazione per la Prenotazione
    Rappresenta la prenotazione del Paziente registrata da parte dell'amministratore
"""

import datetime

from Attivita.Mora import Mora
from Attivita.Ricevuta import Ricevuta
from Eccezioni.MaxPrenException import MaxPrenException
from Eccezioni.MedicoOccupatoException import MedicoOccupatoException
from Eccezioni.PazienteAssenteException import PazienteAssenteException
from Eccezioni.PazienteOccupatoException import PazienteOccupatoException
from Eccezioni.RepartoMedicoException import RepartoMedicoException
from Eccezioni.WeekEndException import WeekEndException
from Gestione.GestoreFile import scriviFile, caricaFile, ricercaElemFile


"""
    Metodo per la ricerca di un determinata Prenotazione sulla base dell'ID.
    Si richiama il metodo di ricerca dal GestoreFile che permette l'apertura 
    e lo scorrimento del file contenente le Prenotazioni.
"""
def ricerca(id):
    # chiamata al metodo contenuto in GestoreFile
    return ricercaElemFile("Prenotazioni", id)


class Prenotazione:

    """
        Costruttore della classe
        Set degli attributi di Prenotazione a null
    """
    def __init__(self):
        self.id = 0
        self.data = datetime.datetime(1970, 1, 1)
        self.ora = datetime.time(0, 0, 0)
        self.cf_paziente = ""
        self.id_medico = 0
        self.id_visita = 0
        self.scaduta = False
        self.disdetta = False
        self.conclusa = False

        self.id_referto = 0
        self.id_ricevuta = 0
        self.id_mora = 0


    """
        Metodo che permette l'aggiunta delle informazioni di una nuova Prenotazione.
        Scrittura su file delle nuove informazioni.
        Si implementano inoltre i controlli:
            - no prenotazioni nel weekend (sabato e domenica la struttura è chiusa)
            - esistenza del CF del paziente inserito
            - confronto tra reparto della visita e reparto del medico (non posso prenotare una visita di un reparto con il medico di un altro)
            - controllo se il medico in quella specifica data e ora è già impegnato in un'altra visita
            - controllo che il paziente nella stessa data e ora non può avere prenotazioni in contemporanea
            - un paziente non può avere più di 5 prenotazioni attive contemporaneamente
    """
    def aggiungiPrenotazione(self, id, data, ora, id_medico, id_visita, cf_paziente):
        self.id = id
        self.ora = ora
        self.id_medico = id_medico
        self.id_visita = id_visita

        # controllo weekend
        if data.isoweekday() > 5:
            # errore, la data scelta cade durante il weekend (sabato o domenica)
            raise WeekEndException

        self.data = data

        # caricamento dei Pazienti nel dizionario mediante la chiamata al GestoreFile
        pazienti = caricaFile("Pazienti")

        # scorrimento dizionario per la verifica dell'esistenza del CF del paziente inserito
        for paziente in pazienti:
            if paziente.CF == cf_paziente:
                self.cf_paziente = cf_paziente

        # se trovo il CF del paziente inserito continuo i controlli, altrimenti restituisco l'errore del CF
        if self.cf_paziente != "":

            # caricamento delle visite in dizionario visite, mediante la chiamata al GestoreFile
            visite = caricaFile("Visite")

            # scorro il dizionario salvando l'id del reparto della visita scelta in fase di registrazione della prenotazione
            id_reparto_visita = 0
            for visita in visite:
                if visita.id == self.id_visita:
                    id_reparto_visita = visita.id_reparto

            # caricamento dei medici in dizionario medici, mediante la chiamata al GestoreFile
            medici = caricaFile("Medici")

            # scorro il dizionario salvando l'id del reparto del medico scelto in fase di registrazione della prenotazione
            id_reparto_medico = -1
            for medico in medici:
                if medico.id == self.id_medico:
                    id_reparto_medico = medico.id_reparto

            # se gli id del reparto di medico e visita corrispondono continuo i controlli, altrimenti restituisco l'errore relativo
            if id_reparto_visita == id_reparto_medico:
                # scorrimento di tutti i medici fino al medico desiderato
                for medico in medici:
                    if self.id_medico == medico.id:

                        # caricamento delle prenotazioni in dizionario prenotazioni, mediante chiamata al GestoreFile
                        prenotazioni = caricaFile("Prenotazioni")

                        """
                            Scorro tutti i pazienti fino al paziente selezionato in fase di registrazione della prenotazione
                            e successivamente scorro le prenotazioni per verificare se il paziente ha altre prenotazioni attive.
                            (in particolare controllo il n° di prenotazioni attive e la data e l'ora delle prenotazioni attive)
                        """
                        c = 0
                        for paziente in pazienti:
                            if paziente.CF == self.cf_paziente:
                                for prenotazione in prenotazioni:
                                    if prenotazione.cf_paziente == self.cf_paziente:
                                        if not prenotazione.disdetta and not prenotazione.scaduta and not prenotazione.conclusa:
                                            c += 1

                                        # se conto 5 o più prenotazioni restituisco un errore (il paziente può prenotare max 5 visite contemp.)
                                        if c >= 5:
                                            # errore troppe prenotazioni a carico di un paziente
                                            raise MaxPrenException

                                        # se trovo una prenotazione con stessa data e stessa ora che non sia stata disdetta restituisco
                                        #un errore (il paziente non può fare + visite contemp.)
                                        if prenotazione.ora == self.ora and prenotazione.data == self.data and not prenotazione.disdetta:
                                            # errore più prenotazioni nello stesso momento per il paziente
                                            raise PazienteOccupatoException

                        # controllo se il medico in questione è libero nel giorno e ora specificate, altrimenti restituisco un errore
                        for prenotazione in prenotazioni:
                            if prenotazione.id_medico == self.id_medico and not prenotazione.disdetta:
                                if prenotazione.data == self.data and prenotazione.ora == self.ora:
                                    # errore medico già impegnato in altre visite nel giorno e ora desiderate
                                    raise MedicoOccupatoException

                # se non ho riscontrato alcun problema nei controlli posso salvare la prenotazione nel file con GestoreFile
                scriviFile("Prenotazioni", self)

            else:
                # errore della non corrispondenza tra id reparto del medico e id reparto della visita
                raise RepartoMedicoException
        else:
            # errore CF del paziente non trovato nell'archivio
            raise PazienteAssenteException


    """
        Metodo che ritorna tutte le informazioni registrate di Prenotazione.
        Si ritorna il dizionario seguente con dentro le informazioni complete di Prenotazione.
    """
    def getInfoPrenotazione(self):
        return {
            "id": self.id,
            "data": self.data,
            "ora": self.ora,
            "scaduta": self.scaduta,
            "disdetta": self.disdetta,
            "conclusa": self.conclusa,
            "id_medico": self.id_medico,
            "id_visita": self.id_visita,
            "cf_paziente": self.cf_paziente
        }


    """
        Metodo per la disdetta di una particolare Prenotazione.
        Controllo se sono già passati i 5 giorni limite per la disdetta.
        Controllo chi sta richiedendo la disdetta:
            - se il paziente chiede la disdetta e i 5 giorni sono passati, allora avrà a suo carico la mora
            - se il paziente chiede la disdetta e i 5 giorni non sono ancora passati, non avrà alcuna mora
            - se è il medico o l'amministratore a disdire per problemi interni, il paziente non anvrà alcuna mora
        Set del flag di disdetta della prenotazione a prescindere dai controlli della mora.
    """
    def disdiciPrenotazione(self, num):
        costo = 0

        # se la prenotazione non è ancora disdetta o conclusa posso procedere con i controlli della mora, altrimenti invio un errore
        if not self.disdetta and not self.conclusa:
            sottrazione_data = self.data - datetime.datetime.today()

            # se i 5 giorni per la disdetta sono scaduti procedo con l'inserimento della mora
            if sottrazione_data.days < 5:

                # caricamente del file visite in dizionario visite, mediante la chiamata a GestoreFile
                visite = caricaFile("Visite")

                # scorro il dizionario delle visite e salvo il costo della visita scelta nella prenotazione
                for visita in visite:
                    if self.id_visita == visita.id:
                        costo = visita.costo

                # se è il paziente a disdire creo la mora con un costo, se è l'amm/medico creo una mora con motivazione a costo zero
                if num == 1:
                    Mora(self.id, costo, "Non disdetta in tempo. ")
                else:
                    Mora(self.id, 0, "Prenotazione disdetta dal medico o dall'amministratore. ")


            # set flag di disdetta e salvataggio delle informazioni della prenotazione su file (GestoreFile)
            self.disdetta = True
            scriviFile("Prenotazioni", self)
            return True
        else:
            # errore, non posso disdire la prenotazione perché è già stata disdetta oppure è già conclusa
            return False


    """
        Metodo di controllo per la scadenzaa di Prenotazione.
        Controllo se la Prenotazione è già scaduta o conclusa
        Se la prenotazione è scaduta vuol dire che il paziente non si è presentato alla visita e non ha disdetto la prenotazione
        quindi dovrà pagare una mora.
        Set del flag scaduta della prenotazione e salvataggio delle informazioni di Prenotazione su file
    """
    def scadenzaPrenotazione(self):
        costo = 0
        if not self.scaduta and not self.conclusa:
            # controlli sulla data di scadenza
            scadenza = datetime.datetime.today()
            scadenza = scadenza.replace(day=scadenza.day - 1)

            # se la prenotazione risulta scaaduta eseguo il set del flag
            if self.data < scadenza:
                self.scaduta = True

                # caricamento delle visite sul dizionario visite, trovo la visita in questione e salvo il costo
                visite = caricaFile("Visite")
                for visita in visite:
                    if self.id_visita == visita.id:
                        costo = visita.costo

                # creazione della Mora relativa alla prenotazione scaduta e scrittura su file dei dati aggiornati della Prenotazione
                Mora(self.id, costo, "Prenotazione scaduta. ")
                scriviFile("Prenotazioni", self)
                return True
        else:
            return False


    """
        Metodo che permette la creazione di una nuova Ricevuta, set del flag prenotazione conclusa.
        Scrittura su file delle nuove informazioni.
    """
    def crea_ricevuta(self):
        costo = 0

        # se la prenotazione ancora non è né disdetta né scaduta né conclusa posso crearne la ricevuta (quando il paziente effettua la visita)
        if not self.disdetta and not self.scaduta and not self.conclusa:

            # caricamento del file visite e ricerca della visita scritta in prenotazione, salvataggio del costo
            visite = caricaFile("Visite")
            for visita in visite:
                if self.id_visita == visita.id:
                    costo = visita.costo

            # creazione ricevuta e set flag prenotazione conclusa
            Ricevuta(self.id, costo)
            self.conclusa = True

            # scrittura fu file delle nuove informazioni di prenotazione
            scriviFile("Prenotazioni", self)
            return True
        else:
            # ritorno un valore che indica che non ho potuto creare la ricevuta
            return False
