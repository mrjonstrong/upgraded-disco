import unittest
from clothing_recommendation import get_clothing_recommendation

class TestClothingRecommendation(unittest.TestCase):

    def test_sunny_warm(self):
        weather = "sunny"
        temperature = 80
        precipitation = 10
        expected = ("Clothing: Wear sunglasses, a hat, and sunscreen. "
                    "Shorts and a t-shirt should be fine.")
        self.assertEqual(
            get_clothing_recommendation(weather, temperature, precipitation), 
            expected
        )

    def test_rainy_cold(self):
        weather = "rainy"
        temperature = 40
        precipitation = 90
        expected = ("Clothing: Don't forget an umbrella or a raincoat. "
                    "Consider wearing a warm jacket.")
        self.assertEqual(
            get_clothing_recommendation(weather, temperature, precipitation), 
            expected
        )

    def test_snowy(self):
        weather = "snowy"
        temperature = 30
        precipitation = 60
        expected = ("Clothing: Wear a heavy jacket, gloves, and a hat. "
                    "Snow boots are also recommended.")
        self.assertEqual(
            get_clothing_recommendation(weather, temperature, precipitation), 
            expected
        )

    def test_cloudy_mild(self):
        weather = "cloudy"
        temperature = 65
        precipitation = 20
        expected = ("Clothing: A long sleeve shirt and pants should be comfortable.")
        self.assertEqual(
            get_clothing_recommendation(weather, temperature, precipitation), 
            expected
        )

if __name__ == "__main__":
    unittest.main()
