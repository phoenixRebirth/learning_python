import unittest
from unittest.mock import MagicMock
# on mock toujours un objet
# mais on peut mocker aussi une méthode seulement

class Algorithme():

    def get_key(self):
        return self.encrypt()

def get_signature_from_key(algo):
    return algo.get_key().split("#")[-1]

class Test(unittest.TestCase):
    def setUp(self):
        self.algo = Algorithme()
        self.algo.get_key = MagicMock(return_value = "fsdjflksmldsmlkfsfdlsdfldsmlq#sdfjhsdkjf")

    def testGetSignatureFromKey(self):
        self.assertEquals(get_signature_from_key(self.algo), "sdfjhsdkjf")

if __name__ == "__main__":
    unittest.main()
