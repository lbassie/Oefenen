"""Tests voor gokspel.py: checkt de vergelijkingslogica los van user input."""

import unittest


def vergelijk(gok, geheim_getal):
    if gok < geheim_getal:
        return "Hoger!"
    elif gok > geheim_getal:
        return "Lager!"
    return "Goed geraden!"


class TestGokspel(unittest.TestCase):
    def test_gok_te_laag(self):
        self.assertEqual(vergelijk(10, 50), "Hoger!")

    def test_gok_te_hoog(self):
        self.assertEqual(vergelijk(90, 50), "Lager!")

    def test_gok_juist(self):
        self.assertEqual(vergelijk(50, 50), "Goed geraden!")


if __name__ == "__main__":
    unittest.main()
