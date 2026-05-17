from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, p_jaratszam, p_celallomas, p_jegyar):
        self.jaratszam = p_jaratszam
        self.celallomas = p_celallomas
        self.jegyar = p_jegyar

    def getJaratszam(self):
        return self.jaratszam

    def getCelallomas(self):
        return self.celallomas

    def getJegyar(self):
        return self.jegyar

    @abstractmethod
    def jaratTipus(self):
        pass