from kps import KiviPaperiSakset
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _tokan_siirto(self, ekan_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        return tokan_siirto
