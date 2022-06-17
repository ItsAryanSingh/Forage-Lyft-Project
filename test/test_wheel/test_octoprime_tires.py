import unittest
from tires.octoprime_tires import OctoprimeTires

netWearValuePerTire = OctoprimeTires([0,0,0,0]).netwearValue/4

class test_octorpime_tires(unittest.TestCase):
    def test_tire_should_ret_false(self):
        tireReadings = [0,0,0,0]
        self.assertFalse(OctoprimeTires(tireReadings).needs_service())

    def test_tire_should_ret_True(self):
        tireReadings = [netWearValuePerTire,netWearValuePerTire,netWearValuePerTire,netWearValuePerTire]
        self.assertTrue(OctoprimeTires(tireReadings).needs_service())