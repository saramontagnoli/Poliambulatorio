import os
import pickle


def ricercaElemFile(filename, id):
    path = f"File/{filename}.pickle"
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            dizionario = dict(pickle.load(f))
            return dizionario[id]
    else:
        return None


def caricaFile(filename):
    dizionario = []
    path = f"File/{filename}.pickle"
    # Apertura e scrittura su file delle visite
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            current = dict(pickle.load(f))
            dizionario.extend(current.values())
        return dizionario


def scriviFile(filename, elemento):
    dizionario = {}
    path = f"File/{filename}.pickle"

    if os.path.isfile(path):
        with open(path, 'rb') as f:
            dizionario = pickle.load(f)
    dizionario[elemento.id] = elemento
    with open(path, 'wb') as f:
        pickle.dump(dizionario, f, pickle.HIGHEST_PROTOCOL)
        return True


def rimuoviElemFile(filename, elemento):
    path = f"File/{filename}.pickle"
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            dizionario = dict(pickle.load(f))
            del dizionario[elemento.id]
        with open(path, 'wb') as f:
            pickle.dump(dizionario, f, pickle.HIGHEST_PROTOCOL)


class GestoreFile:
    pass
