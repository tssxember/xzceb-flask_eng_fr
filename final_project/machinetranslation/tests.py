import unittest
from  translator import english_to_french
from  translator import french_to_english

class TestModule(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_f2e2(self):
        self.assertEqual(french_to_english('None'),'')
    def test_f2e3(self):
        self.assertNotEqual(french_to_english(0),0)

class TestModule2(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_e2f2(self):
        self.assertEqual(english_to_french('None'),'')
    def test_e2f3(self):
        self.assertNotEqual(english_to_french(0),0) 


unittest.main()    
