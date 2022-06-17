import unittest
from car_factory import CarFactory
from datetime import datetime

today = datetime.today().date()
capuletEngineMileage = 30000
willoughbyEngineMileage = 60000
spindlerBatteryLife = 3
nubbinBatteryLife = 4
wearValueCarriganTire = 0.9
sumWearValueOctoprimeTires = 3
wearValueOctoprimeTire = sumWearValueOctoprimeTires /4


class test_car_factory_calliope_carrigan_tires(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage-1
        last_service_mileage = 0
        tireList = [0,0,0,0]
        self.assertFalse(CarFactory.create_Calliope_with_carrigan_tires(today,last_service_date,current_mileage,last_service_mileage,tireList).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage + 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Calliope_with_carrigan_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - spindlerBatteryLife - 1)
        current_mileage = capuletEngineMileage - 1
        last_service_mileage = 0
        tireList = [0,0,0,0]
        self.assertTrue(CarFactory.create_Calliope_with_carrigan_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

    def test_tyre_cause_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage - 1
        last_service_mileage = 0
        tireList = [0, 0, 0, wearValueCarriganTire]
        self.assertTrue(CarFactory.create_Calliope_with_carrigan_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

class test_car_factory_calliope_octoprime_tires(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage-1
        last_service_mileage = 0
        tireList = [0,0,0,0]
        self.assertFalse(CarFactory.create_Calliope_with_octoprime_tires(today,last_service_date,current_mileage,last_service_mileage,tireList).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage + 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Calliope_with_octoprime_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - spindlerBatteryLife - 1)
        current_mileage = capuletEngineMileage - 1
        last_service_mileage = 0
        tireList = [0,0,0,0]
        self.assertTrue(CarFactory.create_Calliope_with_octoprime_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

    def test_tyre_cause_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage - 1
        last_service_mileage = 0
        tireList = [wearValueOctoprimeTire,wearValueOctoprimeTire,wearValueOctoprimeTire,wearValueOctoprimeTire]
        self.assertTrue(CarFactory.create_Calliope_with_octoprime_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())



class test_car_factory_glissade_carrigan_tires(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        tireList = [0,0,0,0]
        self.assertFalse(CarFactory.create_Glissade_with_carrigan_tires(today,last_service_date,current_mileage,last_service_mileage,tireList).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage + 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Glissade_with_carrigan_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - spindlerBatteryLife - 1)
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Glissade_with_carrigan_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

    def test_tyre_cause_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        tireList = [0, 0, 0, wearValueCarriganTire]
        self.assertTrue(CarFactory.create_Glissade_with_carrigan_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

class test_car_factory_glissade_octoprime_tires(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertFalse(CarFactory.create_Glissade_with_octoprime_tires(today, last_service_date, current_mileage,last_service_mileage, tireList).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage + 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Glissade_with_octoprime_tires(today, last_service_date, current_mileage,last_service_mileage, tireList).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - spindlerBatteryLife - 1)
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Glissade_with_octoprime_tires(today, last_service_date, current_mileage,last_service_mileage, tireList).needs_service())

    def test_tyre_cause_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        tireList = [wearValueOctoprimeTire,wearValueOctoprimeTire,wearValueOctoprimeTire,wearValueOctoprimeTire]
        self.assertTrue(CarFactory.create_Glissade_with_octoprime_tires(today, last_service_date, current_mileage,last_service_mileage, tireList).needs_service())




class test_car_factory_palindrome__carrigan_tires(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        warning_light = False
        tireList = [0,0,0,0]
        self.assertFalse(CarFactory.create_Palindrome_with_carrigan_tires(today,last_service_date,warning_light,tireList).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        warning_light = True
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Palindrome_with_carrigan_tires(today, last_service_date, warning_light,tireList).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - spindlerBatteryLife - 1)
        warning_light = False
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Palindrome_with_carrigan_tires(today, last_service_date, warning_light,tireList).needs_service())

    def test_tyre_cause_service(self):
        last_service_date = today
        warning_light = False
        tireList = [0, 0, 0, wearValueCarriganTire]
        self.assertTrue(CarFactory.create_Palindrome_with_carrigan_tires(today, last_service_date, warning_light,tireList).needs_service())

class test_car_factory_palindrome__octoprime_tires(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        warning_light = False
        tireList = [0,0,0,0]
        self.assertFalse(CarFactory.create_Palindrome_with_octoprime_tires(today,last_service_date,warning_light,tireList).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        warning_light = True
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Palindrome_with_octoprime_tires(today, last_service_date, warning_light,tireList).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - spindlerBatteryLife - 1)
        warning_light = False
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Palindrome_with_octoprime_tires(today, last_service_date, warning_light,tireList).needs_service())

    def test_tyre_cause_service(self):
        last_service_date = today
        warning_light = False
        tireList = [wearValueOctoprimeTire,wearValueOctoprimeTire,wearValueOctoprimeTire,wearValueOctoprimeTire]
        self.assertTrue(CarFactory.create_Palindrome_with_octoprime_tires(today, last_service_date, warning_light,tireList).needs_service())



class test_car_factory_rorschach_carrigan_tires(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        tireList = [0,0,0,0]
        self.assertFalse(CarFactory.create_Rorschach_with_carrigan_tires(today,last_service_date,current_mileage,last_service_mileage,tireList).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage + 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Rorschach_with_carrigan_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - nubbinBatteryLife - 1)
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Rorschach_with_carrigan_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

    def test_tyre_cause_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        tireList = [0, 0, 0, wearValueCarriganTire]
        self.assertTrue(CarFactory.create_Rorschach_with_carrigan_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

class test_car_factory_rorschach_octoprime_tires(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertFalse(CarFactory.create_Rorschach_with_octoprime_tires(today, last_service_date, current_mileage,last_service_mileage, tireList).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage + 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Rorschach_with_octoprime_tires(today, last_service_date, current_mileage,last_service_mileage, tireList).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - nubbinBatteryLife - 1)
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Rorschach_with_octoprime_tires(today, last_service_date, current_mileage,last_service_mileage, tireList).needs_service())

    def test_tyre_cause_service(self):
        last_service_date = today
        current_mileage = willoughbyEngineMileage - 1
        last_service_mileage = 0
        tireList = [wearValueOctoprimeTire,wearValueOctoprimeTire,wearValueOctoprimeTire,wearValueOctoprimeTire]
        self.assertTrue(CarFactory.create_Rorschach_with_octoprime_tires(today, last_service_date, current_mileage,last_service_mileage, tireList).needs_service())


class test_car_factory_thovex_carrigan_tires(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage-1
        last_service_mileage = 0
        tireList = [0,0,0,0]
        self.assertFalse(CarFactory.create_Thovex_with_carrigan_tires(today,last_service_date,current_mileage,last_service_mileage,tireList).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage + 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Thovex_with_carrigan_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - nubbinBatteryLife - 1)
        current_mileage = capuletEngineMileage - 1
        last_service_mileage = 0
        tireList = [0,0,0,0]
        self.assertTrue(CarFactory.create_Thovex_with_carrigan_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

    def test_tyre_cause_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage - 1
        last_service_mileage = 0
        tireList = [0, 0, 0, wearValueCarriganTire]
        self.assertTrue(CarFactory.create_Thovex_with_carrigan_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

class test_car_factory_thovex_octoprime_tires(unittest.TestCase):

    def test_engine_should_not_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage-1
        last_service_mileage = 0
        tireList = [0,0,0,0]
        self.assertFalse(CarFactory.create_Thovex_with_octoprime_tires(today,last_service_date,current_mileage,last_service_mileage,tireList).needs_service())

    def test_engine_cause_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage + 1
        last_service_mileage = 0
        tireList = [0, 0, 0, 0]
        self.assertTrue(CarFactory.create_Thovex_with_octoprime_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

    def test_battery_cause_service(self):
        last_service_date = today.replace(year=today.year - nubbinBatteryLife - 1)
        current_mileage = capuletEngineMileage - 1
        last_service_mileage = 0
        tireList = [0,0,0,0]
        self.assertTrue(CarFactory.create_Thovex_with_octoprime_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())

    def test_tyre_cause_service(self):
        last_service_date = today
        current_mileage = capuletEngineMileage - 1
        last_service_mileage = 0
        tireList = [wearValueOctoprimeTire,wearValueOctoprimeTire,wearValueOctoprimeTire,wearValueOctoprimeTire]
        self.assertTrue(CarFactory.create_Thovex_with_octoprime_tires(today, last_service_date, current_mileage, last_service_mileage,tireList).needs_service())


