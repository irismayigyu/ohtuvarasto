import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastoon_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_otetaan_liikaa(self):
        self.varasto.ota_varastosta(11)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_pienempi_kuin_0_ota_varastosta(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0.0)

    def test_lisaa_varastoon_alle_0(self):
        self.assertAlmostEqual(self.varasto.lisaa_varastoon(-1), None)

    def test_str(self):
        result = str(self.varasto)
        self.assertEqual(result, "saldo = 0, vielä tilaa 10")

    def test_tilavuus_alle_0(self):
        self.varasto = Varasto(tilavuus=-2.0, alku_saldo=5.0)
        self.assertEqual(self.varasto.tilavuus, 0.0)

    def test_alkusaldo_alle_0(self):
        self.varasto = Varasto(tilavuus=10, alku_saldo=-2.0)
        self.assertEqual(self.varasto.saldo, 0.0)

    def test_alkusaldo_isompi_kuin_tilavuus(self):
        self.varasto = Varasto(tilavuus=10, alku_saldo=11)
        self.assertEqual(self.varasto.saldo, 10)
