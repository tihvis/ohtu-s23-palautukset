from komentotehdas import KomentoTehdas


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        if vastaus.endswith("a"):
            kaksinpeli = KomentoTehdas.pelaaja_vs_pelaaja()
            kaksinpeli.pelaa()

        elif vastaus.endswith("b"):
            tekoaly = KomentoTehdas.tekoaly()
            tekoaly.pelaa()

        elif vastaus.endswith("c"):
            parempi_tekoaly =  KomentoTehdas.parempi_tekoaly()
            parempi_tekoaly.pelaa()

        else:
            break

if __name__ == "__main__":
    main()
