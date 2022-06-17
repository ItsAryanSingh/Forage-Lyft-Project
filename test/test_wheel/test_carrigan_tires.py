import unittest
from tires.carrigan_tires import CarriganTires

wearValue = CarriganTires([0,0,0,0]).wearReq

class test_octorpime_tires(unittest.TestCase):
    def test_tire_should_ret_false(self):
        tireReadings = [0,0,0,0]
        self.assertFalse(CarriganTires(tireReadings).needs_service())

    def test_tire_should_ret_True(self):
        tireReadings = [0,0,0,wearValue]
        self.assertTrue(CarriganTires(tireReadings).needs_service())