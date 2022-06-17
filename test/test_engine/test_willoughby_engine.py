import unittest
from engine.willoughby_engine import WilloughbyEngine


class WilloughbyEngineTest(unittest.TestCase):

    def test_willoughby_engine_expect_false(self):
        currentMileage = WilloughbyEngine(0,0).mileage
        lastServiceMileage = 0
        self.assertFalse(WilloughbyEngine(currentMileage,lastServiceMileage).needs_service())

    def test_willoughby_engine_expect_true(self):
        currentMileage = WilloughbyEngine(0,0).mileage+1
        lastServiceMileage = 0
        self.assertTrue(WilloughbyEngine(currentMileage,lastServiceMileage).needs_service())