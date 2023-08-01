import unittest

from tyres.carrigan_tyre import Carrigan


class TestCarriganTyre(unittest.TestCase):
    def test_needs_service_true(self):
        arr = [1,0.9,0.5,0.6]
        tyre = Carrigan(arr)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        arr = [0.1,0.2,0.3,0.5]
        tyre = Carrigan(arr)
        self.assertFalse(tyre.needs_service())
