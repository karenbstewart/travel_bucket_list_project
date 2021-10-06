import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):
    
    def setUp(self):
        country1 = Country("Scotland", 2 )
        self.city1 = City("Edinburgh", False, country1, 1)

    def test_city_has_country(self):
        self.assertEqual("Scotland", self.city1.country.country_name)

    def test_city_has_name(self):
        self.assertEqual("Edinburgh", self.city1.city_name)

    def test_city_has_id(self):
        self.assertEqual(1, self.city1.id)

    def test_country_id_through_city_accessible(self):
        self.assertEqual(2, self.city1.country.id)

    def test_city_has_visited(self):
        self.assertEqual(False, self.city1.visited)


    
