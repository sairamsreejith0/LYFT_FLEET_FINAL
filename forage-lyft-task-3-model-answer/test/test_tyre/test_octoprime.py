import unittest
from tyres.octoprime_tyre import Octoprime


class TestOctoprimeTyre(unittest.TestCase):
    def test_needs_service_true(self):
        arr = [1,2,3,4]
        tyre = Octoprime(arr)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        arr=[0.2,0.2,0.4,0.4]
        tyre = Octoprime(arr)
        self.assertFalse(tyre.needs_service())
