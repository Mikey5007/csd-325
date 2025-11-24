# test_cities.py

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Does 'santiago', 'chile' return 'Santiago, Chile'?"""
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()