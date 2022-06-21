import datetime
import os
import pickle


class Prenotazione:

    def __init__(self):
        self.id = -1
        self.data = datetime.date(1970, 1, 1)
        self.time = datetime.date(0, 0)
        self.scaduta = False
        self.disdetta = False
        self.conclusa = False

