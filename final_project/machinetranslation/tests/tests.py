import unittest
import sys
sys.path.insert(0, '/home/project/xzceb-flask_eng_fr/final_project/machinetranslation')

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Oui')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hi')
        self.assertNotEqual(french_to_english('Bonjour'), 'Yes')


unittest.main()