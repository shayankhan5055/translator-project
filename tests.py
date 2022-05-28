from translator import french_to_english, english_to_french
import unittest



class test_french_to_english(unittest.TestCase):
    def test1(self): 
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french("tree"), "arbre")


class test_english_to_french(unittest.TestCase):
    def test1(self): 
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english("Balle"), "Ball")



unittest.main()