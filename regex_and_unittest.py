import re
import unittest
# le ^ signifie le début et le $ la fin
# une chaine de taille 1 composée d'un chiffre entre 0 et 9: ^[0-9]$
# une chaine d'au moins un charactere, à choisir parmi les lettres de l'alphabet et les chiffres: ^[a-zA-Z0-9]+$
# une chaine d'au moins un charactere, à choisir parmi les lettres de l'alphabet et les chiffresn suivie obligatoirement d'un arobase: ^[a-zA-Z0-9]$
# le + signifie au moins une fois (exemple [a-z]+   signifie un caractèrede l'alphabet au moins )
# le * : pareil pour 0 fois au moins (c'est optionnel, par exemple si on veut tester ce qui est au milieu)

# plein de lettres + @ + qsdsqd + '.' + dsqdq
'''
exemples :
[a-zA-Z0-9.+-_]+ signifie : au moins un caractère parmi
    - les lettres minuscules de l'alphabet
    - les lettres majuscules de l'alphabet
    - les chiffres
    - les caractères . + - _
donc '^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+$' signifie :
les chaines de caractères commençants par au moins un caractère dans [a-zA-Z0-9.+-_]
suivie de '@' suivie de au moins un caractère dans [a-zA-Z0-9] suivi du caractère '.'
suivi de au moins un caractère dans [a-zA-Z0-9]
'''

def is_email_correct(mail):
    return bool(re.match('^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9]+[.]{1}[a-zA-Z0-9]+$', mail))

# ^[[0-9]{2}[ ]{0-1}]{4}[0-9]{1}$
# ^[[0-9]{2}[ ]?]{5}$
# {10} pour préciser qu'on veut 10 caractères exactement
def is_phone_french(number):
    return \
        bool(re.match('^(\+33 |0)6 ([0-9]{2} ){3}[0-9]{2}$', number)) or \
        bool(re.match('^(\+33 ?|0)6[0-9]{8}$', number))

class EmailRegexTest(unittest.TestCase):

    def setUp(self):
        pass

    def testShouldReturnTrue(self):
        self.assertTrue(is_email_correct("pierre.benedetti.92@gmail.com"))
        self.assertTrue(is_email_correct("benepierre_92@hotmail.com"))
        self.assertTrue(is_email_correct("benepierre-92@hotmail.com"))
        self.assertTrue(is_email_correct("benepierr.92+@hotmail.com"))

    def testShouldReturnFalse(self):
        self.assertFalse(is_email_correct("benepierr.92+hotmail.com"))
        self.assertFalse(is_email_correct("benepierr.92+@hotmail_.com"))
        self.assertFalse(is_email_correct("92@h"))
        self.assertFalse(is_email_correct("benepierr.92+@hotmail"))
        self.assertFalse(is_email_correct("@hotmail.com"))

class PhoneRegexTest(unittest.TestCase):
    # '+33' ou '+33 ' ou '0'
    # '6' ou '6 '
    # bloc de 3 x 2 chiffres: 'XX' ou 'XX '
    # 'XX'

    def setUp(self):
        pass

    def testShouldReturnFrenchNumber(self):
        self.assertTrue(is_phone_french("0680512860"))
        self.assertTrue(is_phone_french("06 80 51 28 60"))
        self.assertTrue(is_phone_french("+33680512860"))
        self.assertTrue(is_phone_french("+33 680512860"))
        self.assertTrue(is_phone_french("+33 6 80 51 28 60"))
    #
    def testShouldReturnNotFrenchNumber(self):
        self.assertFalse(is_phone_french("0880512860"))
        self.assertFalse(is_phone_french("0680 512860"))
        self.assertFalse(is_phone_french("068051286"))
        self.assertFalse(is_phone_french("06 80 51 28 60 "))
        self.assertFalse(is_phone_french("068 0512860"))
        self.assertFalse(is_phone_french("06a0512860"))
        self.assertFalse(is_phone_french("06 80512860"))

if __name__ == "__main__":
    unittest.main()
