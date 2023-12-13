from kps import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self, muistin_koko):
        self._parempi_tekoaly = TekoalyParannettu(muistin_koko)

    def _tokan_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._parempi_tekoaly.anna_siirto()
        self._parempi_tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto