from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from Battery.spindler_battery import SpindlerBattery
from Battery.nubbin_battery import NubbinBattery
#from datetime import datetime

class CarFactory(Car):
    def create_Calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date))

    def create_Glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date))

    def create_Palindrome(current_date, last_service_date, warning_light_is_on):
        return Car(SternmanEngine(warning_light_is_on),SpindlerBattery(current_date, last_service_date))

    def create_Rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date))

    def create_Thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date))
