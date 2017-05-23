import unittest
from unittest.mock import MagicMock, Mock
# on mock toujours un objet
# mais on peut mocker aussi une méthode seulement

class Algorithme():
    # def __init__(self, *args, **kwargs):
    #     while(True):
    #         self.name = 'hey'

    def get_key(self):
        return self.encrypt()

def get_signature_from_key(algo):
    return algo.get_key().split("#")[-1]

class Test(unittest.TestCase):
    # @patch('Algorithme')
    def setUp(self):
        self.algo = Mock()
        self.algo.get_key = MagicMock(return_value = "fsdjflksmldsmlkfsfdlsdfldsmlq#sdfjhsdkjf")

    def testGetSignatureFromKey(self):
        self.assertEquals(get_signature_from_key(self.algo), "sdfjhsdkjf")

if __name__ == "__main__":
    unittest.main()
