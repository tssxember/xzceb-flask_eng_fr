import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class TestModule(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    def test_f2e2(self):
        self.assertEqual(frenchToEnglish('None'),'')

  class TestModule(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
    def test_f2e2(self):
        self.assertEqual(englishToFrench('None'),'') 


unittest.main()     

