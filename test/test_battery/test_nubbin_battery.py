import unittest
from Battery.nubbin_battery import NubbinBattery
from datetime import datetime

today = datetime.today().date()

class NubbinBatteryTest(unittest.TestCase):
    def test_nubbin_battery_expect_false(self):
        last_service_date = today.replace(year=today.year)
        self.assertFalse(NubbinBattery(today,last_service_date).needs_service())

    def test_nubbin_battery_expect_true(self):
        last_service_date = today.replace(year=today.year - NubbinBattery(today,today).life-1)
        self.assertTrue(NubbinBattery(today,last_service_date).needs_service())