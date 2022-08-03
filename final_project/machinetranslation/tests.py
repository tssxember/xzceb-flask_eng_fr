import unittest
from translator import english_to_french
from translator import french_to_english

class TestModule(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_f2e2(self):
        self.assertEqual(french_to_english('None'),'')

class TestModule2(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_f2e2(self):
        self.assertEqual(english_to_french('None'),'') 


unittest.main()     