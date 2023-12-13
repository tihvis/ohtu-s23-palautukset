from kps import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _tokan_siirto(self, ekan_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return tokan_siirto
