import unittest
from car_factory import CarFactory
from datetime import datetime

today = datetime.today().date()
capuletEngineMileage = 30000
willoughbyEngineMileage = 60000
spindlerBatteryLife = 2
nubbinBatteryLife = 4


class test_car_factory_calliope(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage-1
        last_service_mileage = 0
        self.assertFalse(CarFactory.create_Calliope(today,last_service_date,current_mileage,last_service_mileage).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage + 1
        last_service_mileage = 0
        self.assertTrue(CarFactory.create_Calliope(today, last_service_date, current_mileage, last_service_mileage).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - spindlerBatteryLife - 1)
        current_mileage = capuletEngineMileage - 1
        last_service_mileage = 0
        self.assertTrue(CarFactory.create_Calliope(today, last_service_date, current_mileage, last_service_mileage).needs_service())

    def test_should_service(self):
        last_service_date = today.replace(year=today.year - spindlerBatteryLife - 1)
        current_mileage = capuletEngineMileage + 1
        last_service_mileage = 0
        self.assertTrue(CarFactory.create_Calliope(today, last_service_date, current_mileage, last_service_mileage).needs_service())

class test_car_factory_glissade(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        self.assertFalse(CarFactory.create_Glissade(today,last_service_date,current_mileage,last_service_mileage).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage + 1
        last_service_mileage = 0
        self.assertTrue(CarFactory.create_Glissade(today, last_service_date, current_mileage, last_service_mileage).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - spindlerBatteryLife - 1)
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        self.assertTrue(CarFactory.create_Glissade(today, last_service_date, current_mileage, last_service_mileage).needs_service())

    def test_should_service(self):
        last_service_date = today.replace(year=today.year - spindlerBatteryLife - 1)
        current_mileage = willoughbyEngineMileage + 1
        last_service_mileage = 0
        self.assertTrue(CarFactory.create_Glissade(today, last_service_date, current_mileage, last_service_mileage).needs_service())

class test_car_factory_palindrome(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        warning_light = False
        self.assertFalse(CarFactory.create_Palindrome(today,last_service_date,warning_light).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        warning_light = True
        self.assertTrue(CarFactory.create_Palindrome(today, last_service_date, warning_light).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - spindlerBatteryLife - 1)
        warning_light = False
        self.assertTrue(CarFactory.create_Palindrome(today, last_service_date, warning_light).needs_service())

    def test_should_service(self):
        last_service_date = today.replace(year=today.year - spindlerBatteryLife - 1)
        warning_light = True
        self.assertTrue(CarFactory.create_Palindrome(today, last_service_date, warning_light).needs_service())

class test_car_factory_rorschach(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        self.assertFalse(CarFactory.create_Rorschach(today,last_service_date,current_mileage,last_service_mileage).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage + 1
        last_service_mileage = 0
        self.assertTrue(CarFactory.create_Rorschach(today, last_service_date, current_mileage, last_service_mileage).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - nubbinBatteryLife - 1)
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        self.assertTrue(CarFactory.create_Rorschach(today, last_service_date, current_mileage, last_service_mileage).needs_service())

    def test_should_service(self):
        last_service_date = today.replace(year=today.year - nubbinBatteryLife - 1)
        current_mileage = willoughbyEngineMileage + 1
        last_service_mileage = 0
        self.assertTrue(CarFactory.create_Rorschach(today, last_service_date, current_mileage, last_service_mileage).needs_service())

class test_car_factory_thovex(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage-1
        last_service_mileage = 0
        self.assertFalse(CarFactory.create_Thovex(today,last_service_date,current_mileage,last_service_mileage).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage + 1
        last_service_mileage = 0
        self.assertTrue(CarFactory.create_Thovex(today, last_service_date, current_mileage, last_service_mileage).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - nubbinBatteryLife - 1)
        current_mileage = capuletEngineMileage - 1
        last_service_mileage = 0
        self.assertTrue(CarFactory.create_Thovex(today, last_service_date, current_mileage, last_service_mileage).needs_service())

    def test_should_service(self):
        last_service_date = today.replace(year=today.year - nubbinBatteryLife - 1)
        current_mileage = capuletEngineMileage + 1
        last_service_mileage = 0
        self.assertTrue(CarFactory.create_Thovex(today, last_service_date, current_mileage, last_service_mileage).needs_service())