import unittest
from engine.capulet_engine import CapuletEngine

class CapuletEngineTest(unittest.TestCase):

    def test_capulet_engine_expect_false(self):
        currentMileage = CapuletEngine(0,0).mileage
        lastServiceMileage = 0
        self.assertFalse(CapuletEngine(currentMileage,lastServiceMileage).needs_service())

    def test_capulet_engine_expect_true(self):
        currentMileage = CapuletEngine(0,0).mileage+1
        lastServiceMileage = 0
        self.assertTrue(CapuletEngine(currentMileage,lastServiceMileage).needs_service())
