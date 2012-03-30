"""Module de tests pour le module operator"""
import sys
sys.path[:0]=["../"]

from unittest import TestCase
from operators import *


class OperatorsTests (TestCase):
    """Classe de tests pour le module operator"""
    def test_add(self):
        """Test de la fonction Add"""
        self.assertEquals(add(2,3),5)
        
    def test_mul(self):
        """Test de la fonction Mul"""
        self.assertEquals(mul(2,3),6)
