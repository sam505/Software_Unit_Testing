import unittest
import scrabble


class TestScrabble(unittest.TestCase):
    def test_main(self):
        self.assertTrue(scrabble.main())

    def test_word_is_english(self):
        self.assertTrue(scrabble.check_word("Scrabble"))

    def test_word_is_not_english(self):
        self.assertFalse(scrabble.check_word("Sckralef"))

    def test_calculate_word_score_numbers(self):
        self.assertEqual(scrabble.calculate_word_score("12345"), 0)

    def test_calculate_word_score_cabbage_upper(self):
        self.assertEqual(scrabble.calculate_word_score("CABBAGE"), 14)

    def test_calculate_word_score_cabbage_lower(self):
        self.assertEqual(scrabble.calculate_word_score("cabbage"), 14)

    def test_calculate_word_score_house(self):
        self.assertEqual(scrabble.calculate_word_score("House"), 8)

    def test_calculate_word_score_house_upper_lower(self):
        self.assertEqual(scrabble.calculate_word_score("HoUsE"), 8)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestScrabble)

    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()
