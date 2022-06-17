from tires.Tires import Tires

CarriganTireWearReq = 0.9

class CarriganTires(Tires):
    def __init__(self, tire_readings):
        self.tire_readings = tire_readings
        self.wearReq = CarriganTireWearReq

    def needs_service(self):
        return not all(i < self.wearReq for i in self.tire_readings)