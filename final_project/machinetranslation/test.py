import unittest
import translator


class Testing(unittest.TestCase):
    def test_null(self):
        a = 'Null'
        b = translator.english_to_french(a)
        self.assertEqual(a, b)

    def test_null2(self):
        a = 'Null'
        b = translator.french_to_english(a)
        self.assertEqual(a, b)
    
    def test_en_fr(self):
        a = 'Hello'
        b = translator.english_to_french(a)
        self.assertEqual(b, 'Bonjour')

    def test_fr_en(self):
        a = 'Bonjour'
        b = translator.french_to_english(a)
        self.assertEqual(b, 'Hello')

if __name__ == '__main__':
    unittest.main()