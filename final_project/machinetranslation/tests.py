import unittest
from  translator import english_to_french
from  translator import french_to_english

class TestModule(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english(0),0)

class TestModule2(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french(0),0) 


unittest.main()    
