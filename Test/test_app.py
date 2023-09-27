import unittest
from App.multi import *

class testmulti(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(multiplicacion(2,3),6)
    def test_suma(self):
        self.assertEqual(suma(2,2),4)

if __name__ == "__main__":
    unittest.main()

