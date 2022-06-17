import unittest
from Battery.nubbin_battery import NubbinBattery
from Battery.spindler_battery import SpindlerBattery
from datetime import datetime

today = datetime.today().date()


class SpindlerBatteryTest(unittest.TestCase):
    def test_spindler_battery_expect_false(self):
        last_service_date = today.replace(year=today.year)
        self.assertFalse(SpindlerBattery(today,last_service_date).needs_service())

    def test_spindler_battery_expect_true(self):
        last_service_date = today.replace(year=today.year-SpindlerBattery(today,today).life-1)
        self.assertTrue(SpindlerBattery(today,last_service_date).needs_service())

class NubbinBatteryTest(unittest.TestCase):
    def test_nubbin_battery_expect_false(self):
        last_service_date = today.replace(year=today.year)
        self.assertFalse(NubbinBattery(today,last_service_date).needs_service())

    def test_nubbin_battery_expect_true(self):
        last_service_date = today.replace(year=today.year - NubbinBattery(today,today).life-1)
        self.assertTrue(NubbinBattery(today,last_service_date).needs_service())

if __name__ == '__main__':
    unittest.main()