from kayttoliittyma import Komento

class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_arvo = 0
        self._edellinen_komento = None

    def miinus(self, operandi):
        self._edellinen_arvo = self._arvo
        self._edellinen_komento = Komento.EROTUS
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._edellinen_arvo = self._arvo
        self._edellinen_komento = Komento.SUMMA
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._edellinen_arvo = self._arvo
        self._edellinen_komento = Komento.NOLLAUS
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def edellinen_arvo(self):
        return self._edellinen_arvo
    
    def edellinen_komento(self):
        return self._edellinen_komento
