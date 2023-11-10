class Varasto:
    """luokka joka simuloi varastoa
    attributes:
    tilavuus: varaston tilavuus
    alku_saldo: paljonko varastossa on alunperin
    """

    def __init__(self, tilavuus, alku_saldo=0):
        """Luokan konstruktori, joka luo uuden varaston.

        Args:
            tilavuus: varaston tilavuus
            alku_saldo: paljonko varastossa on alunperin
        """
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        """kertoo paljonko varastossa on vielä tilaa vähentämällä koko tilavuudesta, 
        paljonko siellä on tällä tällä hetkelle
        args:
        tilavuus
        saldo"""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """lisää varastoon parametrina annetun määrän

        Args:
            maara
            saldo
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """simuloi ottamista varastosta. saldosta tulee saldo kun siitä on vähennetty 
        määrä mikä halutaan ottaa, joka on määritelty parametrina. 
        args:
        maara
        saldo"""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        """Muodostaa varastosta merkkijonomuotoisen esityksen.

        Returns:
            Merkkijono, joka kertoo varaston saldon sekä paljonko on vielä tilaa varastossa
        """
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
