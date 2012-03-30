"""Module de tests pour le module logic"""
import sys
sys.path[:0]=["../"]

from unittest import TestCase
from logic import *


class OperatorsTests (TestCase):
    """Classe de tests pour le module logic"""
    def test_and(self):
        """Test de la fonction And"""
        self.assertEquals(and_(True,False),False)
        
    def test_or(self):
        """Test de la fonction or"""
        self.assertEquals(or_(True,False),True)
