import unittest
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

class CapuletEngineTest(unittest.TestCase):

    def test_capulet_engine_expect_false(self):
        currentMileage = CapuletEngine(0,0).mileage
        lastServiceMileage = 0
        self.assertFalse(CapuletEngine(currentMileage,lastServiceMileage).needs_service())

    def test_capulet_engine_expect_true(self):
        currentMileage = CapuletEngine(0,0).mileage+1
        lastServiceMileage = 0
        self.assertTrue(CapuletEngine(currentMileage,lastServiceMileage).needs_service())

class WilloughbyEngineTest(unittest.TestCase):

    def test_willoughby_engine_expect_false(self):
        currentMileage = WilloughbyEngine(0,0).mileage
        lastServiceMileage = 0
        self.assertFalse(WilloughbyEngine(currentMileage,lastServiceMileage).needs_service())

    def test_willoughby_engine_expect_true(self):
        currentMileage = WilloughbyEngine(0,0).mileage+1
        lastServiceMileage = 0
        self.assertTrue(WilloughbyEngine(currentMileage,lastServiceMileage).needs_service())

class SternmanEngineTest(unittest.TestCase):

    def test_sternman_engine_expect_false(self):
        warning_light = False
        self.assertFalse(SternmanEngine(warning_light).needs_service())

    def test_sternman_engine_expect_true(self):
        warning_light = True
        self.assertTrue(SternmanEngine(warning_light).needs_service())

if __name__ == '__main__':
    unittest.main()