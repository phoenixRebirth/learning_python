import unittest
# from training_regex_and_unittest import *
from training_regex_and_unittest import is_mail

class PhoneRegexTest(unittest.TestCase):
    def setUp(self):
        pass

    def testShouldReturnTrue(self):
        self.assertTrue(is_phone("0677243511"))
        self.assertTrue(is_phone("06 77 24 35 11"))
        self.assertTrue(is_phone("+33 677243511"))
        self.assertTrue(is_phone("+33 6 77 24 35 11"))

    def testShouldReturnFalse(self):
        self.assertFalse(is_phone("0 677 243511"))
        self.assertFalse(is_phone("067724351"))
        self.assertFalse(is_phone("06772435118"))
        self.assertFalse(is_phone("0677 243511"))

class EmailRegexTest(unittest.TestCase):
    def setUp(self):
        pass

    def testShouldReturnTrue(self):
        self.assertTrue(is_mail("aaa.aaa@gmail.com"))
        self.assertTrue(is_mail("aaaaaa@gmail.com"))
        self.assertTrue(is_mail("aaRFEaaa@gmail.com"))
        self.assertTrue(is_mail("aaa.aaa@dsv.com"))
        self.assertTrue(is_mail("aaa-aaa@gmail.dsv"))
        self.assertTrue(is_mail("aaa._aaa@gmail.com"))
        self.assertTrue(is_mail("aaa245.aaa@gmail.com"))

    def testShouldReturnFalse(self):
        self.assertFalse(is_mail("aaa.aaagmail.com"))
        self.assertFalse(is_mail("aaa.aaa@gmailcom"))
        self.assertFalse(is_mail("aaa aaa@gmail.com"))


unittest.main()  # va appeler les tests de touttes les classes héritant de la classe unittest.TestCase
