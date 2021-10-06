import unittest
from models.country import Country 

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country1 = Country("Spain", 3)

    def test_country_has_name(self):
        self.assertEqual("Spain", self.country1.country_name)

    def test_country_has_id(self):
        self.assertEqual(3, self.country1.id)

