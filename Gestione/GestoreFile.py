"""
    Classe che implementa la gestione dei caricamenti e scritture su File
    Si occupa anche delle ricerche effettuate sui File
    Per rendere più generale il gestore si passa come parametro il nome del file, creando il path
"""

import os
import pickle
import shutil


"""
    La cartella Appoggio contiene tutti i file vuoti e i file di Reparti e Visite precompilati
    Nel momento in cui dovessero essere cancellati i file dal package File si provvede al caricamento dei file "base"
    direttamente copiandoli da Appoggio a File
    Metodo, dunque, che permette il caricamento dei file di default nel momento in cui non dovessero essere presenti, dovessero
    essere stati cancellati o corrotti e quindi avessero bisogno di un ripristino.
"""
def creazioneFile(filename):
    empty_list = []
    path1 = f"Appoggio/{filename}.pickle"
    path2 = f"File/{filename}.pickle"
    print(path1)
    # se il file passato come parametro non esiste lo carica da Appoggio, se esiste lo mantiene
    if not os.path.exists(path2):
        shutil.copy(path1, 'File/')


"""
    Metodo che permette la ricerca di un determinato elemento a partire dall'id, in un file passato come parametro
"""
def ricercaElemFile(filename, id):
    path = f"File/{filename}.pickle"
    # apertura del file e caricamento dei dati nel dizionario
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            dizionario = dict(pickle.load(f))
            return dizionario[id]
    else:
        return None

"""
    Metodo che permette di eseguire il caricamento di un file passato come parametro in un dizionario
    Return di tutto il dizionario riempito
"""
def caricaFile(filename):
    dizionario = []
    path = f"File/{filename}.pickle"
    # apertura del file e caricamento dei dati nel dizionario
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            current = dict(pickle.load(f))
            dizionario.extend(current.values())
        return dizionario

"""
    Metodo che permette di eseguire la scrittura di un elemento nel file passato come parametro
    Return True se ho portato a termine l'inserimento in modo corretto 
"""
def scriviFile(filename, elemento):
    dizionario = {}
    path = f"File/{filename}.pickle"

    # apertura file per il caricamento delle informazioni
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            dizionario = pickle.load(f)
    dizionario[elemento.id] = elemento
    # apertura del file in scrittura e aggiunta delle nuove informazioni nel file
    with open(path, 'wb') as f:
        pickle.dump(dizionario, f, pickle.HIGHEST_PROTOCOL)
        return True

"""
    Metodo che permette di eseguire la rimozione di un elemento da un file passato come parametro
"""
def rimuoviElemFile(filename, elemento):
    path = f"File/{filename}.pickle"
    # apertura del file per il caricamento dei dati e rimozione dell'elemento
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            dizionario = dict(pickle.load(f))
            del dizionario[elemento.id]
        # apertura in scrittura del file e caricamento del dizionario modificato nel file
        with open(path, 'wb') as f:
            pickle.dump(dizionario, f, pickle.HIGHEST_PROTOCOL)


class GestoreFile:
    pass
