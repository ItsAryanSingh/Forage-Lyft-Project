from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from Battery.spindler_battery import SpindlerBattery
from Battery.nubbin_battery import NubbinBattery
from tires.octoprime_tires import OctoprimeTires
from tires.carrigan_tires import CarriganTires

class CarFactory(Car):
    @staticmethod
    def create_Calliope_with_octoprime_tires(current_date, last_service_date, current_mileage, last_service_mileage,tireList):
        return Car(CapuletEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date),OctoprimeTires(tireList))

    @staticmethod
    def create_Glissade_with_octoprime_tires(current_date, last_service_date, current_mileage, last_service_mileage,tireList):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date),OctoprimeTires(tireList))

    @staticmethod
    def create_Palindrome_with_octoprime_tires(current_date, last_service_date, warning_light_is_on,tireList):
        return Car(SternmanEngine(warning_light_is_on),SpindlerBattery(current_date, last_service_date),OctoprimeTires(tireList))

    @staticmethod
    def create_Rorschach_with_octoprime_tires(current_date, last_service_date, current_mileage, last_service_mileage,tireList):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date),OctoprimeTires(tireList))

    @staticmethod
    def create_Thovex_with_octoprime_tires(current_date, last_service_date, current_mileage, last_service_mileage,tireList):
        return Car(CapuletEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date),OctoprimeTires(tireList))
#
    @staticmethod
    def create_Calliope_with_carrigan_tires(current_date, last_service_date, current_mileage, last_service_mileage, tireList):
        return Car(CapuletEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date),CarriganTires(tireList))

    @staticmethod
    def create_Glissade_with_carrigan_tires(current_date, last_service_date, current_mileage, last_service_mileage, tireList):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date),CarriganTires(tireList))

    @staticmethod
    def create_Palindrome_with_carrigan_tires(current_date, last_service_date, warning_light_is_on, tireList):
        return Car(SternmanEngine(warning_light_is_on), SpindlerBattery(current_date, last_service_date),CarriganTires(tireList))

    @staticmethod
    def create_Rorschach_with_carrigan_tires(current_date, last_service_date, current_mileage, last_service_mileage, tireList):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date),CarriganTires(tireList))

    @staticmethod
    def create_Thovex_with_carrigan_tires(current_date, last_service_date, current_mileage, last_service_mileage, tireList):
        return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date),CarriganTires(tireList))


