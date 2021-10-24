import unittest
from django.test import TestCase

class TesteBasico(TestCase):
    def test_testado(self):
        self.assertEqual(1+1,2)